import cv2
import csv
import json
from pathlib import Path
from rapidocr_onnxruntime import RapidOCR


# --------------------------------
# 1. Get preprocessed plate path
# --------------------------------

plate_path = input(
    "Enter preprocessed plate image path: "
).strip()

plate_path = Path(plate_path)


# --------------------------------
# 2. Check image
# --------------------------------

if not plate_path.exists():
    print("Error: Plate image not found.")
    exit()


# --------------------------------
# 3. Load image
# --------------------------------

image = cv2.imread(str(plate_path))

if image is None:
    print("Error: Could not load plate image.")
    exit()


# --------------------------------
# 4. Initialize RapidOCR
# --------------------------------

ocr = RapidOCR()


# --------------------------------
# 5. Run OCR
# --------------------------------

result, _ = ocr(image)


# --------------------------------
# 6. Extract text and confidence
# --------------------------------

texts = []
confidences = []

if result:

    for item in result:

        text = item[1].strip()
        confidence = float(item[2])

        if text:
            texts.append(text)
            confidences.append(confidence)


# --------------------------------
# 7. Combine text
# --------------------------------

recognized_text = " ".join(texts)


# --------------------------------
# 8. Calculate confidence
# --------------------------------

if confidences:

    average_confidence = (
        sum(confidences) / len(confidences)
    ) * 100

else:

    average_confidence = 0.0


# --------------------------------
# 9. Determine readability
# --------------------------------

if not recognized_text:

    recognized_text = "Unreadable"
    status = "Unreadable"

elif average_confidence < 40:

    recognized_text = "Unreadable"
    status = "Unreadable"

else:

    status = "Readable"


# --------------------------------
# 10. Create main output folder
# --------------------------------

output_folder = Path(
    "output/text_extraction"
)

output_folder.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------
# 11. Create unique result folder
# --------------------------------

result_folder = (
    output_folder /
    plate_path.stem
)

result_folder.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------
# 12. Create OCR result
# --------------------------------

ocr_result = {

    "plate_image": plate_path.name,

    "plate_text": recognized_text,

    "confidence": round(
        average_confidence,
        2
    ),

    "status": status
}


# --------------------------------
# 13. Save individual JSON
# --------------------------------

json_path = (
    result_folder /
    "ocr_result.json"
)

with open(
    json_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        ocr_result,
        file,
        indent=4
    )


# --------------------------------
# 14. Save master CSV
# --------------------------------

csv_path = (
    output_folder /
    "all_plate_results.csv"
)

file_exists = csv_path.exists()

with open(
    csv_path,
    "a",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "plate_image",
            "plate_text",
            "confidence",
            "status"
        ]
    )

    if not file_exists:
        writer.writeheader()

    writer.writerow(
        ocr_result
    )


# --------------------------------
# 15. Display result
# --------------------------------

print("\n================================")
print("       PLATE TEXT EXTRACTION")
print("================================")

print(
    f"Plate Image : {plate_path.name}"
)

print(
    f"Plate Text  : {recognized_text}"
)

print(
    f"Confidence  : "
    f"{average_confidence:.2f}%"
)

print(
    f"Status      : {status}"
)

print("\nSaved:")
print(
    f"JSON : {json_path}"
)

print(
    f"CSV  : {csv_path}"
)

print("================================")