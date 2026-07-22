import cv2
import numpy as np
img = cv2.imread("pic5.jpeg")
if img is None:
    print("Image not found!")
    exit()
orignel=img.copy()    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 30, 100)
kernel = np.ones((7,7), np.uint8)
closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(
    closing,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
largest = max(contours, key=cv2.contourArea)
cv2.drawContours(orignel, [largest], -1, (0,255,0), 3)
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)
cv2.imshow("Closing", closing)
cv2.imshow("Detected Boundary",orignel )
cv2.imwrite("Outputs/pic5.jpeg",orignel)
cv2.waitKey(0)
cv2.destroyAllWindows()
