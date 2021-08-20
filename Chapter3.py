import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)
 
imgResize = cv2.resize(img, (300,227))
 
imgCropped = img[0:500,100:700]


cv2.imshow("Image", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)