import cv2
import numpy as np
img = cv2.imread("ImageS/Triangle.png")
if img is None:
    print("Image not found!")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Total Contours Found: {len(contours)}\n")
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if area < 200:
        continue
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
    corners = len(approx)
    x, y, w, h = cv2.boundingRect(approx)
    ratio = w / float(h)
    circularity = 0
    if perimeter != 0:
        circularity = (4 * np.pi * area) / (perimeter * perimeter)
    if corners == 3:
        shape = "Triangle"

    elif corners == 4:

        if 0.95 <= ratio <= 1.05:
            shape = "Square"
        else:
            shape = "Rectangle"

    elif circularity >= 0.85:
        shape = "Circle"

    elif corners == 5:
        shape = "Pentagon"

    elif corners == 6:
        shape = "Hexagon"

    else:
        shape = "Polygon"

    print(f"Shape {i+1}")
    print(f"Detected Shape : {shape}")
    print(f"Corners        : {corners}")
    print(f"Area           : {area:.2f}")
    print(f"Perimeter      : {perimeter:.2f}")
    print(f"Aspect Ratio   : {ratio:.2f}")
    print(f"Circularity    : {circularity:.2f}")
    print("-" * 35)
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img,
                shape,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2)
cv2.imshow("Binary Image", binary)
cv2.imshow("Shape Detection", img)
cv2.imwrite("Output/Triangle.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
