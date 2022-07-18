# displaying videos
import cv2 as cv

vid = cv.VideoCapture("images/video.mp4")

while True:
    vid_successful, video_cap = vid.read()
    cv.imshow("Demo Video", video_cap)

    if cv.waitKey(20) & 0xFF == ord('q'):   # the larger the waitKey() value, the slower the video
        break
