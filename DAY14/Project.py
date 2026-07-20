import cv2
import numpy as np
import os
def load():
    path = input("Enter image path: ")
    img = cv2.imread(path)
    if img is not None:
        print("Image Loaded ")
        return img
    else:
        print("Image Not Found")
        exit()

def grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return gray

def resize(img):
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    resized = cv2.resize(img, (width, height))
    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return resized

def rotate(img):
    print("1. Rotate 90°")
    print("2. Rotate 180°")
    print("3. Rotate 270°")

    choice = input("Enter Choice: ")
    if choice == "1":
        rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif choice == "2":
        rotated = cv2.rotate(img, cv2.ROTATE_180)
    elif choice == "3":
        rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        print("Invalid Choice")
        return img
    cv2.imshow("Rotated Image", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rotated

def flip(img):
    print("1. Horizontal")
    print("2. Vertical")
    print("3. Both")
    choice = input("Enter Choice: ")
    if choice == "1":
        flip = cv2.flip(img, 1)
    elif choice == "2":
        flip = cv2.flip(img, 0)
    elif choice == "3":
        flip = cv2.flip(img, -1)
    else:
        print("Invalid Choice")
        return img
    cv2.imshow("Flipped Image", flip)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return flip

def crop(img):
    print("Image Information")
    print("Width :", img.shape[1], "pixels")
    print("Height:", img.shape[0], "pixels")
    x1 = int(input("Enter Start X:"))
    y1 = int(input("Enter Start Y:"))
    x2 = int(input("Enter End X:"))
    y2 = int(input("Enter End Y:"))
    cropped = img[y1:y2, x1:x2]
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return cropped

def draw(img):
    print("\n--- Rectangle ---")
    x1 = int(input("Enter Rectangle Start X: "))
    y1 = int(input("Enter Rectangle Start Y: "))
    x2 = int(input("Enter Rectangle End X: "))
    y2 = int(input("Enter Rectangle End Y: "))
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    print("\n--- Circle ---")
    cx = int(input("Enter Circle Center X: "))
    cy = int(input("Enter Circle Center Y: "))
    radius = int(input("Enter Radius: "))
    cv2.circle(img, (cx, cy), radius, (255, 0, 0), 2)
    print("\n--- Line ---")
    lx1 = int(input("Enter Line Start X: "))
    ly1 = int(input("Enter Line Start Y: "))
    lx2 = int(input("Enter Line End X: "))
    ly2 = int(input("Enter Line End Y: "))
    cv2.line(img, (lx1, ly1), (lx2, ly2), (0, 0, 255), 2)
    print("\n--- Polygon ---")
    n = int(input("Enter Number of Points: "))
    points = []
    for i in range(n):
        print(f"\nPoint {i+1}")
        x = int(input("X: "))
        y = int(input("Y: "))
        points.append([x, y])
    points = np.array(points, np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img, [points], True, (255, 255, 0), 2)
    cv2.imshow("Shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
def addtext(img):
    text = input("Enter Text: ")
    cv2.putText(
        img,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )
    cv2.imshow("Image with Text", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
def save(img):
    filename = input("Enter file name: ")
    cv2.imwrite(f"output/{filename}.jpg", img)
    print("Image saved successfully.")
img = load()
while True:
    print("\n------ IMAGE PROCESSING TOOLKIT ------")
    print("1. Convert to Grayscale")
    print("2. Resize Image")
    print("3. Rotate Image")
    print("4. Flip Image")
    print("5. Crop Image")
    print("6. Draw Shapes")
    print("7. Add Text")
    print("8. Save Image")
    print("9. Display Image")
    print("10. Load New Image")
    print("0. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        img = grayscale(img)
    elif choice == "2":
        img = resize(img)
    elif choice == "3":
        img = rotate(img)
    elif choice == "4":
        img = flip(img)
    elif choice == "5":
        img = crop(img)
    elif choice == "6":
        img = draw(img)
    elif choice == "7":
        img = addtext(img)
    elif choice == "8":
        save(img)
    elif choice == "9":
        cv2.imshow("Current Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == "0":
        print("Thank You")
        break

    elif choice == "10":
      img = load()
    else:
        print("Invalid Choice")
