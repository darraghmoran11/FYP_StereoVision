import cv2
import numpy

capLeft = cv2.VideoCapture(1) #sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
capRight = cv2.VideoCapture(0) #sets cap2 as the second camera

while(True):
    # creates the frames for each camera
    ret, frameLeft = capLeft.read()
    ret, frameRight = capRight.read()

    grayL = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

    HSV_L = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2HSV)
    HSV_R = cv2.cvtColor(frameRight, cv2.COLOR_BGR2HSV)

    # Shows the content each camera is recording
    cv2.imshow('frame_video_left', frameLeft)
    cv2.imshow('frame_video_gray_left', grayL)
    cv2.imshow('frame_video_HSV_left', HSV_L)

    cv2.imshow('frame_video_right', frameRight)
    cv2.imshow('frame_video_gray_right', grayR)
    cv2.imshow('frame_video_HSV_right', HSV_R)

    # if loop to break the camera feed when completed. The waitKey determines the number of frames
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capLeft.release()
capRight.release()
cv2.destroyAllWindows()