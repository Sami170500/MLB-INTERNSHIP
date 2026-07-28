import cv2
import json
import numpy as np
from ultralytics import YOLO

img = None
image_path = ""
parking_slots = []
car_boxes = []
occupied = 0
vacant = 0

def load_image():

    global img
    global image_path

    image_path = input("Enter Image Path: ")

    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    print("Image Loaded Successfully!")

    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def draw_parking_slots():

    global img
    global parking_slots
    global image_path
    if img is None:
        print("Please load an image first.")
        return
    annotation_path = input("Enter COCO Annotation Path: ")
    with open(annotation_path, "r") as file:
        data = json.load(file)
    image_name = image_path.split("\\")[-1]
    image_id = None


    
    for image in data["images"]:

        if image["file_name"] == image_name:
            image_id = image["id"]
            break
    if image_id is None:
        print("Image not found in annotation file.")
        return
    output = img.copy()
    parking_slots.clear()
    for annotation in data["annotations"]:

        if annotation["image_id"] == image_id:

            x, y, w, h = annotation["bbox"]

            parking_slots.append((int(x), int(y), int(w), int(h)))

            cv2.rectangle(
                output,
                (int(x), int(y)),
                (int(x+w), int(y+h)),
                (0,255,0),
                2
            )

    print("Parking Slots Found:", len(parking_slots))
    cv2.imshow("Parking Slots", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def detect_cars():

    global img
    global image_path
    global car_boxes
    if img is None:
        print("Please load an image first.")
        return

    model_path = input("Enter YOLO Model Path: ")

    model = YOLO(model_path)

    results = model.predict(
        source=image_path,
        conf=0.4,
        save=False
    )
    result = results[0]
    output = result.plot()
    car_boxes.clear()

    for box in result.boxes:

        x1, y1, x2, y2 = box.xyxy[0]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        car_boxes.append((x1, y1, x2, y2))
    print("Cars Detected:", len(car_boxes))
    cv2.imshow("YOLO Car Detection", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def check_occupancy():

    global img
    global parking_slots
    global car_boxes
    global occupied
    global vacant

    if img is None:
        print("Please load an image first.")
        return

    output = img.copy()

    occupied = 0
    vacant = 0

    for slot in parking_slots:
        sx, sy, sw, sh = slot
        occupied_slot = False
        for car in car_boxes:

            x1, y1, x2, y2 = car
            if (x1 < sx + sw and
                x2 > sx and
                y1 < sy + sh and
                y2 > sy):

                occupied_slot = True
                break

        if occupied_slot:

            occupied += 1
            cv2.rectangle(
                output,(sx, sy),(sx + sw, sy + sh),(0, 0, 255),2)

        else:

            vacant += 1
            cv2.rectangle(output,(sx, sy),(sx + sw, sy + sh),(0, 255, 0),2)

    print("Occupied Slots:", occupied)
    print("Vacant Slots:", vacant)
    cv2.imshow("Parking Occupancy", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_statistics():
    global occupied
    global vacant
    total = occupied + vacant
    if total == 0:
        print("No parking slots found.")
        return
    occupancy_percentage = (occupied / total) * 100
    print("\n==PARKING STATISTICS ==")
    print("Total Parking Slots :", total)
    print("Occupied Slots      :", occupied)
    print("Vacant Slots        :", vacant)
    print("Occupancy Percentage:", round(occupancy_percentage,2), "%")    

while True:

    print("\n========== SMART PARKING LOT OCCUPANCY ANALYZER ==========")
    print("1. Load Image")
    print("2. Draw Parking Slots")
    print("3. Detect Cars")
    print("4. Check Occupancy")
    print("5. Display Statistics")
    print("6. Run Complete Pipeline")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_image()

    elif choice == "2":
        draw_parking_slots()

    elif choice == "3":
        detect_cars()

    elif choice == "4":
        check_occupancy()

    elif choice == "5":
        display_statistics()

    elif choice == "6":
        load_image()
        draw_parking_slots()
        detect_cars()
        check_occupancy()
        display_statistics()

    elif choice == "0":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        
