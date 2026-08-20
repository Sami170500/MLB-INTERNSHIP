import cv2
import pytesseract
import json
from pathlib import Path
from jiwer import wer, cer

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = input("Enter document image path: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()
name = Path(image_path).stem
output = Path("output")
output.mkdir(exist_ok=True)
annotation_path = input("Enter ground-truth JSON path: ")
with open(annotation_path, "r", encoding="utf-8") as file:
    annotation = json.load(file)

def get_ground_truth(annotation):
    words = []
    for item in annotation["form"]:
        for word in item["words"]:
            text = word["text"].strip()

            if text:
                words.append(text)
    return " ".join(words)

ground_truth = get_ground_truth(annotation)

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised = cv2.bilateralFilter(gray, 9, 60, 60)

    page = cv2.threshold(
        denoised, 190, 255, cv2.THRESH_BINARY
    )[1]

    contours, _ = cv2.findContours(
        page, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    angle = 0

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 10000:
            angle = cv2.minAreaRect(largest)[-1]

            if angle < -45:
                angle = 90 + angle

            if abs(angle) > 45:
                angle = 0

    if abs(angle) > 0.7:
        height, width = denoised.shape[:2]
        center = (width // 2, height // 2)

        matrix = cv2.getRotationMatrix2D(
            center, angle, 1.0
        )

        denoised = cv2.warpAffine(
            denoised,
            matrix,
            (width, height),
            flags=cv2.INTER_CUBIC,
            borderMode=cv2.BORDER_REPLICATE
        )

    clahe = cv2.createCLAHE(
        clipLimit=2.5,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(denoised)

    blurred = cv2.GaussianBlur(
        enhanced, (0, 0), 1.2
    )

    return cv2.addWeighted(
        enhanced, 1.6, blurred, -0.6, 0
    )

def extract_text(image):
    resized = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    return pytesseract.image_to_string(
        resized,
        config="--oem 3 --psm 6"
    )

def detect_text(image):
    scale = 2

    resized = cv2.resize(
        image,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_CUBIC
    )

    data = pytesseract.image_to_data(
        resized,
        output_type=pytesseract.Output.DICT,
        config="--oem 3 --psm 6"
    )

    results = []

    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        confidence = float(data["conf"][i])

        if text and confidence >= 0:
            x = data["left"][i] // scale
            y = data["top"][i] // scale
            w = data["width"][i] // scale
            h = data["height"][i] // scale

            results.append({
                "text": text,
                "coordinates": [x, y, w, h],
                "confidence": round(confidence, 2)
            })

    return results

preprocessed = preprocess(image)

raw_text = extract_text(image)
preprocessed_text = extract_text(preprocessed)

raw_wer = wer(ground_truth, raw_text)
raw_cer = cer(ground_truth, raw_text)

preprocessed_wer = wer(
    ground_truth,
    preprocessed_text
)

preprocessed_cer = cer(
    ground_truth,
    preprocessed_text
)

detections = detect_text(preprocessed)

ocr_image = cv2.cvtColor(
    preprocessed,
    cv2.COLOR_GRAY2BGR
)

for item in detections:
    x, y, w, h = item["coordinates"]
    confidence = item["confidence"]

    cv2.rectangle(
        ocr_image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        ocr_image,
        f"{confidence:.1f}%",
        (x, max(y - 5, 15)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        1
    )

confidences = [
    item["confidence"] for item in detections
]

average_confidence = (
    sum(confidences) / len(confidences)
    if confidences else 0
)

cv2.imwrite(
    str(output / f"{name}_preprocessed.jpg"),
    preprocessed
)

cv2.imwrite(
    str(output / f"{name}_ocr_result.jpg"),
    ocr_image
)

with open(
    output / f"{name}_ocr_result.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("OCR COMPARISON\n\n")
    file.write("GROUND TRUTH:\n")
    file.write(ground_truth)

    file.write("\n\nRAW OCR:\n")
    file.write(raw_text)

    file.write("\n\nPREPROCESSED OCR:\n")
    file.write(preprocessed_text)

    file.write("\n\nACCURACY:\n")
    file.write(f"Raw WER: {raw_wer:.2%}\n")
    file.write(f"Raw CER: {raw_cer:.2%}\n")
    file.write(
        f"Preprocessed WER: {preprocessed_wer:.2%}\n"
    )
    file.write(
        f"Preprocessed CER: {preprocessed_cer:.2%}\n"
    )
    file.write(
        f"\nAverage OCR Confidence: "
        f"{average_confidence:.2f}%\n"
    )

result = {
    "image": name,
    "ground_truth": ground_truth,
    "raw_ocr": raw_text,
    "preprocessed_ocr": preprocessed_text,
    "accuracy": {
        "raw": {
            "WER": round(raw_wer, 4),
            "CER": round(raw_cer, 4)
        },
        "preprocessed": {
            "WER": round(preprocessed_wer, 4),
            "CER": round(preprocessed_cer, 4)
        }
    },
    "average_confidence": round(
        average_confidence, 2
    ),
    "detections": detections
}

with open(
    output / f"{name}_ocr_result.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        result,
        file,
        indent=4,
        ensure_ascii=False
    )

print("\nOCR COMPARISON")
print("\nGROUND TRUTH:")
print(ground_truth)
print("\nRAW OCR:")
print(raw_text)
print("\nPREPROCESSED OCR:")
print(preprocessed_text)
print("\nACCURACY")
print(f"Raw WER: {raw_wer:.2%}")
print(f"Raw CER: {raw_cer:.2%}")
print(f"Preprocessed WER: {preprocessed_wer:.2%}")
print(f"Preprocessed CER: {preprocessed_cer:.2%}")
print(
    f"\nAverage OCR Confidence: "
    f"{average_confidence:.2f}%"
)
print("\nResults saved in:", output)
