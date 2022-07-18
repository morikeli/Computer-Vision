import cv2
import cv2 as cv
import numpy as np
from PIL import Image

img = cv.imread("images/image1.jpg")


def empty_func():
    pass


cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 640, 480)

cv.createTrackbar("Hue min", "Trackbars", 0, 179, empty_func)
cv.createTrackbar("Hue max", "Trackbars", 179, 179, empty_func)
cv.createTrackbar("Saturation min", "Trackbars", 34, 255, empty_func)
cv.createTrackbar("Saturation max", "Trackbars", 255, 255, empty_func)
cv.createTrackbar("Value min", "Trackbars", 24, 255, empty_func)
cv.createTrackbar("Value max", "Trackbars", 162, 255, empty_func)


while True:
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue max", "Trackbars")
    saturation_min = cv.getTrackbarPos("Saturation min", "Trackbars")
    saturation_max = cv.getTrackbarPos("Saturation max", "Trackbars")
    v_min = cv.getTrackbarPos("Value min", "Trackbars")
    v_max = cv.getTrackbarPos("Value max", "Trackbars")

    lower_l = np.array([h_min, saturation_min, v_min])
    upper_l = np.array([h_max, saturation_max, v_max])

    mask = cv.inRange(img_hsv, lower_l, upper_l)
    imgResult = cv.bitwise_and(img, img, mask=mask)
    resize_img = cv2.resize(img, (420, 420))
    vertical_images = np.hstack((resize_img, resize_img, resize_img))

    # cv.imshow("Original Image", img)
    # cv.imshow("HSV", img_hsv)
    cv.imshow("Mask", mask)
    cv.imshow("Image Result", imgResult)
    cv.imshow("Stack Images", vertical_images)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


path = Image.open("images/image1.jpg")
print(f'Height: {path.height}; width: {path.width}')