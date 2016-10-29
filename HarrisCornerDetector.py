import cv2
import numpy as np

capLeft = cv2.VideoCapture(0)
capRight = cv2.VideoCapture(2)

while(True):

    ret, frameLeft = capLeft.read()
    ret, frameRight = capRight.read()

    grayLeft = cv2.cvtColor(frameLeft,cv2.COLOR_BGR2GRAY)
    grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

    grayLeft = np.float32(grayLeft)
    grayRight = np.float32(grayRight)

    dstLeft = cv2.cornerHarris(grayLeft,2,3,0.04)
    dstRight = cv2.cornerHarris(grayRight, 2, 3, 0.04)

    #result is dilated for marking the corners, not important
    dstLeft = cv2.dilate(dstLeft,None)
    dstRight = cv2.dilate(dstRight, None)

    # Threshold for an optimal value, it may vary depending on the image.
    frameLeft[dstLeft>0.01*dstLeft.max()]=[0,0,255]
    frameRight[dstRight>0.01*dstRight.max()]=[0,0,255]

    cv2.imshow('dst_frame_left',frameLeft)
    cv2.imshow('dst_frame_right', frameRight)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

capLeft.release()
capRight.release()
cv2.destroyAllWindows()