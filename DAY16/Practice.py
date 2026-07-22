import cv2
import numpy as np
img=cv2.imread("pic1.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
sobel_x=cv2.Sobel(blur,cv2.CV_64F,1,0,3)
sobel_y=cv2.Sobel(blur,cv2.CV_64F,0,1,3)
sobel=cv2.magnitude(sobel_x,sobel_y)
sobel=cv2.convertScaleAbs(sobel)
cv2.imshow("Sobel",sobel)
cv2.imwrite("poutput/sobel.jpeg",sobel)
cv2.waitKey(0)
cv2.destroyAllWindows


import cv2
import numpy as np
img=cv2.imread("pic1.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
laplacian=cv2.Laplacian(blur,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian,alpha=5)
cv2.imshow("laplacian",laplacian)
cv2.imwrite("poutput/laplacian.jpeg",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows


import cv2
import numpy as np
img=cv2.imread("pic1.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
print(img.shape)
canny=cv2.Canny(blur,30,150)
canny=cv2.convertScaleAbs(canny)
cv2.imshow("Canny",canny)
cv2.imwrite("poutput/canny.jpeg",canny)
cv2.waitKey(0)
cv2.destroyAllWindows

import cv2
import numpy as np
img=cv2.imread("pic3.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
erosion=cv2.erode(binary,kernel,iterations=1)
cv2.imshow("gray",gray)
cv2.imshow("binary",binary)
cv2.imshow("erosion",erosion)
cv2.imwrite("poutput/pic3.jpeg",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows

import cv2
import numpy as np
img=cv2.imread("pic7.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,binary=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
dilation=cv2.dilate(binary,kernel,iterations=1)
cv2.imshow("gray",gray)
cv2.imshow("binary",binary)
cv2.imshow("dilate",dilation)
cv2.imwrite("poutput/pic7.jpeg",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows

import cv2
import numpy as np
img = cv2.imread("pic3.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
cv2.imshow("Binary", binary)
cv2.imshow("Opening", opening)
cv2.imwrite("poutput/opening.jpg", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("pic3.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)
close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Binary", binary)
cv2.imshow("Opening", close)
cv2.imwrite("poutput/close.jpg", close)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("pic5.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((3,3), np.uint8)
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Binary", binary)
cv2.imshow("Gradient", gradient)
cv2.imwrite("poutput/gradient.jpg", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("pic6.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((5,5), np.uint8)
tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Binary", binary)
cv2.imshow("Top Hat", tophat)
cv2.imwrite("poutput/tophat.jpg", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np
img = cv2.imread("pic6.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Binary", binary)
cv2.imshow("Top Hat", blackhat)
cv2.imwrite("poutput/blackhat.jpg", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
