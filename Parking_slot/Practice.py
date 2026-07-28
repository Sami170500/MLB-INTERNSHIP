import cv2
import numpy as np
from ultralytics import YOLO
image_path = r"archive\valid\2013-04-11_07_25_01_jpg.rf.01f9517b1756ab4d3a63c3f328e54d30.jpg"
img = cv2.imread(image_path)
if img is None:
    print("Image not found!")
    exit()
print("Image Loaded Successfully!")
cv2.imshow("Original Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
gray = clahe.apply(gray)
cv2.imshow("Grayscale", gray)
blur = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imshow("Gaussian Blur", blur)
edges = cv2.Canny(blur, 80, 180)
cv2.imshow("Edges", edges)
kernel = np.ones((3,3), np.uint8)
closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
cv2.imshow("Closing", closing)
cv2.imshow("Opening", opening)
contours, hierarchy = cv2.findContours(
    opening,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
output = img.copy()

for contour in contours:
    area = cv2.contourArea(contour)
    if area < 500 or area > 15000:
        continue
    x, y, w, h = cv2.boundingRect(contour)
    if w < 8 or h < 20:
        continue
    ratio = h / w
    if ratio < 1.8:
        continue
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) < 4:
        continue
    cv2.drawContours(output, [contour], -1, (0,255,0), 2)
    cv2.rectangle(output, (x,y), (x+w,y+h), (255,0,0), 2)
cv2.imshow("Detected Contours", output)

model = YOLO("best.pt")
results = model.predict(
    source=image_path,
    conf=0.4,
    save=False
)
result = results[0]
yolo_output = result.plot()
cv2.imshow("YOLO Car Detection", yolo_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
