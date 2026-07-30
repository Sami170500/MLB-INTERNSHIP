import cv2
from ultralytics import YOLO
model = None
def load_model():
    global model
    model = YOLO("best.pt")


def load_image():
    image_path = input("Enter image path: ")
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return None, None
    return image, image_path


def detect_parking(image):
    results = model(image)
    occupied = 0
    vacant = 0
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]
        print(f"Class: {cls}, Label: {label}, Confidence: {conf:.2f}")
        if label.lower() == "space-occupied":
            color = (0, 0, 255)
            occupied += 1
        elif label.lower() == "space-empty":
            color = (0, 255, 0)
            vacant += 1
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

        cv2.putText(
            image,
            f"{label} {conf:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )

    return image, occupied, vacant

def show_statistics(image, occupied, vacant):
    total = occupied + vacant
    cv2.putText(image, f"Occupied: {occupied}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.putText(image, f"Vacant: {vacant}", (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
  
    cv2.putText(image, f"Total: {total}", (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)


def save_output(image):

    output_name = input("Enter output file name (without extension): ")
    cv2.imwrite(f"Output/{output_name}.jpg", image)
    print("Image saved successfully.")


def display_image(image):
    cv2.imshow("Smart Parking Lot Occupancy Analyzer", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():

    load_model()
    image, image_path = load_image()
    if image is None:
        return
    image, occupied, vacant = detect_parking(image)
    show_statistics(image, occupied, vacant)
    save_output(image)
    display_image(image)

if __name__ == "__main__":
    main()
