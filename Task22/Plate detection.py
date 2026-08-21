from ultralytics import YOLO
import cv2
from pathlib import Path

image_path = Path(input("Enter vehicle image path: ").strip())
model_path = Path(input("Enter license plate model path: ").strip())

if not image_path.exists():
    print("Error: Vehicle image not found.")
    exit()

if not model_path.exists():
    print("Error: License plate model not found.")
    exit()

image = cv2.imread(str(image_path))

if image is None:
    print("Error: Could not load image.")
    exit()

model = YOLO(str(model_path))

results = model(image, conf=0.40)

output_folder = Path("output/plates")
detected_folder = Path("output/plate_detections")

output_folder.mkdir(parents=True, exist_ok=True)
detected_folder.mkdir(parents=True, exist_ok=True)

plate_count = 0

for result in results:
    for box in result.boxes:
        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        plate_crop = image[y1:y2, x1:x2]

        if plate_crop.size == 0:
            continue

        plate_count += 1

        plate_path = (
            output_folder /
            f"{image_path.stem}_plate_{plate_count}.jpg"
        )

        cv2.imwrite(
            str(plate_path),
            plate_crop
        )

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        label = f"Plate {confidence:.2f}"

        cv2.putText(
            image,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        print(
            f"Plate {plate_count} detected | "
            f"Confidence: {confidence:.2f}"
        )

detected_path = (
    detected_folder /
    f"{image_path.stem}_detected.jpg"
)

cv2.imwrite(
    str(detected_path),
    image
)

print("\nLicense plate detection completed.")
print(f"Total plates detected: {plate_count}")
print(f"Plate crops saved to: {output_folder}")
print(f"Detected image saved to: {detected_path}")
