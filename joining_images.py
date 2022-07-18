import cv2 as cv
import numpy as np

img = cv.imread("images/image2.jpg")

img_hor = np.hstack((img, img))
img_ver = np.vstack((img, img))

cv.imshow("Horizontal Image", img_hor)
cv.imshow("Vertical Image", img_ver)

while True:
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
