import numpy as np
import cv2
from matplotlib import pyplot as plt


def nothing(x):
    pass
    
cap_left = cv2.VideoCapture(1)
cap_right = cv2.VideoCapture(2)


# create windows
cv2.namedWindow('left_Webcam', cv2.WINDOW_NORMAL)
cv2.namedWindow('right_Webcam', cv2.WINDOW_NORMAL)
cv2.namedWindow('disparity', cv2.WINDOW_NORMAL)

# create trackbars for color change
cv2.createTrackbar('R','cvuint8',0,255,nothing)
cv2.createTrackbar('G','cvuint8',0,255,nothing)
cv2.createTrackbar('B','cvuint8',0,255,nothing)

while(cv2.waitKey(1) & 0xFF != ord('q')):


    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','cvuint8')
    g = cv2.getTrackbarPos('G','cvuint8')
    b = cv2.getTrackbarPos('B','cvuint8')
    s = cv2.getTrackbarPos(switch,'cvuint8')

    ret1, frame_left = cap_left.read()
    ret2, frame_right = cap_right.read()
    # our operations on the frame come here
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)
    cv2.imshow('left_Webcam', gray_left)
    cv2.imshow('right_Webcam', gray_right)
    stereo = cv2.StereoBM(0, ndisparities=16, SADWindowSize=15)
    disparity = stereo.compute(gray_left, gray_right)
    cvuint8 = cv2.convertScaleAbs(disparity)
    cv2.imshow('disparity', cvuint8)
    cv2.waitKey(10)
    print "frame left:",frame_left.dtype
    print "frame right:",frame_right.dtype
    print "Disparity:",cvuint8.dtype
    # When everything done, release the capture
cap_left.release()
cap_right.release()
cv2.destroyAllWindows()