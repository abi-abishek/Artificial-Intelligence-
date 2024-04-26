import cv2

import imutils

img = cv2.imread('new.jpg')

resizedImg = imutils.resize(img, width=100)

cv2.imshow('OriginalImage2.jpg', img)
cv2.imshow('Resized.jpg', resizedImg)

cv2.imwrite('resizedImgae2.jpg', resizedImg)