import cv2 as cv
import numpy as np
img =  cv.imread('C:/Users/User 2/Desktop/cats.jpg')
cv.imshow('Meow', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

##LAPLACIAN
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


##SOBEL
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel', sobel)

cv.waitKey(0)


