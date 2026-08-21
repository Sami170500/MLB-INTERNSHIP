import cv2
from pathlib import Path

plate_path = Path(input("Enter plate image path: ").strip())

if not plate_path.exists():
    print("Error: Plate image not found.")
    exit()

image = cv2.imread(str(plate_path))

if image is None:
    print("Error: Could not load image.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contrast = cv2.convertScaleAbs(
    gray,
    alpha=1.2,
    beta=0
)

filtered = cv2.bilateralFilter(
    contrast,
    5,
    30,
    30
)

blur = cv2.GaussianBlur(
    filtered,
    (0, 0),
    1
)

final_image = cv2.addWeighted(
    filtered,
    1.3,
    blur,
    -0.3,
    0
)

output_folder = Path("output/preprocessed_plates")
output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / f"processed_{plate_path.name}"

cv2.imwrite(
    str(output_path),
    final_image
)

print("\n================================")
print("   PREPROCESSING COMPLETED")
print("================================")

height, width = image.shape[:2]

print(f"Original size: {width} x {height}")
print(f"Saved to: {output_path}")
print("================================")
