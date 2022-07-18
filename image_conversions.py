import cv2 as cv
import numpy as np

img = cv.imread("images/image1.jpg")

# converting image to grayscale.
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# creating a blurred image
blur_img = cv.GaussianBlur(gray_img, (11, 11), 0)   # values of ksize() functions, e.g. ksize(11, 11) must be odd numbers.
# detect edges in the image.
canny_img = cv.Canny(img, 200, 200)     # increasing threshold values decreases the no. of edges in our image.
# dilating a canny image
dilate_img = cv.dilate(canny_img, kernel=np.ones((2, 2), np.uint8), iterations=1)   # increasing the no. of iterations increases the thickness of the
# edges

# eroded image - make edges in a canny image thinner
eroded_img = cv.erode(dilate_img, kernel=np.ones((2, 2), np.uint8), iterations=1)


cv.imshow("Grey image", gray_img)
cv.imshow("Blurred Image", blur_img)
cv.imshow("Canny Image", canny_img)
cv.imshow("Dilated Image", dilate_img)
cv.imshow("Eroded Image", eroded_img)


while True:
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
