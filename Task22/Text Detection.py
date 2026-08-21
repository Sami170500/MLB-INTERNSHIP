import cv2
import csv
import json
from pathlib import Path
from rapidocr_onnxruntime import RapidOCR

plate_path = Path(input("Enter preprocessed plate image path: ").strip())

if not plate_path.exists():
    print("Error: Plate image not found.")
    exit()

image = cv2.imread(str(plate_path))

if image is None:
    print("Error: Could not load plate image.")
    exit()

ocr = RapidOCR()
result, _ = ocr(image)

texts = []
confidences = []

if result:
    for item in result:
        text = item[1].strip()
        confidence = float(item[2])

        if text:
            texts.append(text)
            confidences.append(confidence)

recognized_text = " ".join(texts)

if confidences:
    average_confidence = (sum(confidences) / len(confidences)) * 100
else:
    average_confidence = 0.0

if not recognized_text or average_confidence < 40:
    recognized_text = "Unreadable"
    status = "Unreadable"
else:
    status = "Readable"

output_folder = Path("output/text_extraction")
output_folder.mkdir(parents=True, exist_ok=True)

result_folder = output_folder / plate_path.stem
result_folder.mkdir(parents=True, exist_ok=True)

ocr_result = {
    "plate_image": plate_path.name,
    "plate_text": recognized_text,
    "confidence": round(average_confidence, 2),
    "status": status
}

json_path = result_folder / "ocr_result.json"

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(ocr_result, file, indent=4)

csv_path = output_folder / "all_plate_results.csv"
file_exists = csv_path.exists()

with open(csv_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["plate_image", "plate_text", "confidence", "status"]
    )

    if not file_exists:
        writer.writeheader()

    writer.writerow(ocr_result)

print("\n================================")
print("       PLATE TEXT EXTRACTION")
print("================================")
print(f"Plate Image : {plate_path.name}")
print(f"Plate Text  : {recognized_text}")
print(f"Confidence  : {average_confidence:.2f}%")
print(f"Status      : {status}")
print("\nSaved:")
print(f"JSON : {json_path}")
print(f"CSV  : {csv_path}")
print("================================")
