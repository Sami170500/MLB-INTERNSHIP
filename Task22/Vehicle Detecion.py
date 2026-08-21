from ultralytics import YOLO
import cv2
from pathlib import Path


# Get image path from user
image_path = input("Enter image path: ").strip()

image_path = Path(image_path)


# Check image path
if not image_path.exists():
    print("Error: Image not found.")
    exit()


# Load image
image = cv2.imread(str(image_path))

if image is None:
    print("Error: Could not load image.")
    exit()


# Load pretrained YOLOv8 COCO model
model = YOLO("yolov8n.pt")


# COCO vehicle classes
vehicle_classes = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}


# Create a separate output folder for this image
image_output_folder = Path("output") / image_path.stem

detected_folder = image_output_folder / "detected"
vehicle_folder = image_output_folder / "vehicles"

detected_folder.mkdir(parents=True, exist_ok=True)
vehicle_folder.mkdir(parents=True, exist_ok=True)

# Detect vehicles
results = model(
    image,
    conf=0.80,
    classes=[2, 3, 5, 7]
)


vehicle_count = 0


# Process detected vehicles
for result in results:

    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        vehicle_name = vehicle_classes[class_id]

        # Crop vehicle
        vehicle_crop = image[y1:y2, x1:x2]

        if vehicle_crop.size == 0:
            continue

        vehicle_count += 1

        # Save vehicle crop
        crop_path = (
            vehicle_folder /
            f"{vehicle_name}_{vehicle_count}.jpg"
        )

        cv2.imwrite(
            str(crop_path),
            vehicle_crop
        )

        # Draw bounding box on original image
        label = f"{vehicle_name} {confidence:.2f}"

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

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
            f"Vehicle {vehicle_count}: "
            f"{vehicle_name} | "
            f"Confidence: {confidence:.2f}"
        )


# Save image with vehicle detections
detected_path = detected_folder / image_path.name

cv2.imwrite(
    str(detected_path),
    image
)


print("\nVehicle detection and cropping completed.")
print(f"Total vehicles detected: {vehicle_count}")
print(f"Detected image saved to: {detected_path}")
print(f"Vehicle crops saved to: {vehicle_folder}")