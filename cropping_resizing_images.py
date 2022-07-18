import cv2 as cv

img = cv.imread("images/image2.jpg")
print(img.shape)    # prints (h, w, channel) of the image

# resize image
resize_img = cv.resize(img, (300, 300))    # specify (width, height)

# cropped image
cropped_img = img[0:200, 200:500]

cv.imshow("Original Image", img)
cv.imshow("Resized image", resize_img)
cv.imshow("Cropped Image", cropped_img)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
