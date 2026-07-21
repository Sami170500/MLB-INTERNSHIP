import cv2
import numpy as np
img=cv2.imread('doc2.jpg')
print(img.shape)
cols,rows=img.shape[:2]
m=np.float32([[1,0,-200],
              [0,1,0]])
translate=cv2.warpAffine(img,m,(cols,rows))
cv2.imshow("orignel",img)
cv2.imshow("translated",translate)
cv2.imwrite("outputs/translate.jpg", translate)
cv2.waitKey(0)
cv2.destroyAllWindows

import cv2
img = cv2.imread("doc2.jpg")
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.convertScaleAbs(img, alpha=1.2, beta=10)
            print("Brightness & Contrast .")

kernel = np.array([
                [0,-1,0],
                [-1,5,-1],
                [0,-1,0]
            ])
            img = cv2.filter2D(img,-1,kernel
            print("Image Sharpened.")
