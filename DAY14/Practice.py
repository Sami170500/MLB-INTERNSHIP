import cv2
img=cv2.imread("helmet.jpg")
cv2.imshow("Helmet",img)
print(img.shape)
import os
print(os.path.getsize("helmet.jpg"))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image',gray)
print(gray.shape)
crop1=img[0:300,0:400]
crop2=img[0:150,0:150]
crop3=img[150:200,150:300]
cv2.imshow("Crop",crop1)
cv2.imshow('crop2',crop2)
cv2.imshow("crop3",crop3)
rot1=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rot2=cv2.rotate(img,cv2.ROTATE_180)
rot3=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("rot1",rot1)
cv2.imshow("rot2",rot2)
cv2.imshow("rot3",rot3)
hor=cv2.flip(img,1)
ver=cv2.flip(img,0)
both=cv2.flip(img,-1)
cv2.imshow('hor',hor)
cv2.imshow("ver",ver)
cv2.imshow('both',both)
cv2.waitKey(0)
cv2.destroyAllWindows()
