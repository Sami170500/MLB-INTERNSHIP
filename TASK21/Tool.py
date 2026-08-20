import cv2
import numpy as np
import pytesseract
import json
from pathlib import Path
image_path = input("Enter the document image path: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()

output = Path("output")
name = Path(image_path).stem

def preprocess(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    denoised = cv2.bilateralFilter(
        gray, 9, 60, 60
    )

    page = cv2.threshold(
        denoised, 190, 255, cv2.THRESH_BINARY
    )[1]

    contours, _ = cv2.findContours(
        page,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    angle = 0

    if contours:

        largest = max(
            contours,
            key=cv2.contourArea
        )

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
            center,
            angle,
            1.0
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
        enhanced,
        (0, 0),
        1.2
    )

    sharpened = cv2.addWeighted(
        enhanced,
        1.6,
        blurred,
        -0.6,
        0
    )

    return sharpened


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

    for i in range(len(data["text"])):

        data["left"][i] //= scale
        data["top"][i] //= scale
        data["width"][i] //= scale
        data["height"][i] //= scale

    return data


def get_confidence(image):

    data = detect_text(image)

    scores = []

    for confidence in data["conf"]:

        confidence = float(confidence)

        if confidence >= 0:
            scores.append(confidence)

    if not scores:
        return 0

    return sum(scores) / len(scores)


preprocessed = preprocess(image)

raw_text = extract_text(image)
preprocessed_text = extract_text(preprocessed)

data = detect_text(preprocessed)

ocr_image = cv2.cvtColor(
    preprocessed,
    cv2.COLOR_GRAY2BGR
)

results = []

for i in range(len(data["text"])):

    word = data["text"][i].strip()
    confidence = float(data["conf"][i])

    if word and confidence >= 0:

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        results.append({
            "text": word,
            "coordinates": [x, y, w, h],
            "confidence": round(confidence, 2)
        })

        if confidence >= 50:

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


raw_confidence = get_confidence(image)
preprocessed_confidence = get_confidence(preprocessed)


if preprocessed_confidence > raw_confidence:

    comparison = "Preprocessed image performed better."

elif preprocessed_confidence < raw_confidence:

    comparison = "Raw image performed better."

else:

    comparison = "Both images produced similar results."


cv2.imwrite(
    str(output / f"{name}_preprocessed.jpg"),
    preprocessed
)

cv2.imwrite(
    str(output / f"{name}_ocr_result.jpg"),
    ocr_image
)


with open(
    output / f"{name}_raw_ocr.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(raw_text)


with open(
    output / f"{name}_preprocessed_ocr.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(preprocessed_text)


with open(
    output / f"{name}_ocr_data.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4,
        ensure_ascii=False
    )


with open(
    output / f"{name}_comparison.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(
        "OCR COMPARISON\n"
    )
    file.write(
        "--------------------\n"
    )
    file.write(
        f"Raw Image Confidence: "
        f"{raw_confidence:.2f}%\n"
    )
    file.write(
        f"Preprocessed Image Confidence: "
        f"{preprocessed_confidence:.2f}%\n"
    )
    file.write(
        f"Result: {comparison}\n"
    )

print("\nOCR COMPARISON")
print(f"Raw: {raw_confidence:.2f}%")
print(f"Preprocessed: {preprocessed_confidence:.2f}%")
print(f"Result: {comparison}")
