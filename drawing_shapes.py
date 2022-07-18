import cv2 as cv
import numpy as np

img = np.zeros((512, 980, 3), np.uint8)
# print(img)

# img[:] = 0, 255, 0    # coloring image

# drawing a line
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)  # (h, w) i.e. (img.shape[1], img.shape[0])
# drawing a rectangle
cv.rectangle(img, (0, 0), (300, 300), (0, 0, 255), 5)
cv.circle(img, (400, 400), 30, (255, 0, 255), 4)
cv.putText(img, "Learning OpenCV", (200, 400), cv.FONT_HERSHEY_SIMPLEX, 10, (250, 0, 0), 3)     # fontScale is the same as font size

cv.imshow("Image object", img)

while True:
    if cv.waitKey(0) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
