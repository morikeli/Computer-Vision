# Learning opencv with python, displaying images
import cv2 as cv

img = cv.imread("images/image2.jpg")
cv.imshow("Image 1", img)   # window title, image to be displayed

while True:
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
