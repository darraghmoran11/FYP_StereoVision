import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing():
    pass

cap_left = cv2.VideoCapture(1)
cap_right = cv2.VideoCapture(2)

md = 'minDisparity'
nd = 'numDisparities'
wd = 'SADWindowSize'
dm = 'disp12MaxDiff'
pf = 'preFilterCap'
ur = 'uniquenessRatio'
sw = 'speckleWindowSize'
sr = 'speckleRange'
wnd = 'disparity'

mDi = md 
nDi = nd 
sws = wd 
dMax = dm
pfc = pf 
uRat = ur 
swin = sw
sran = sr  

number_of_image_channels = 2

#minDisparity = 0
#numDisparities = 16
#SADWindowSize = 21
#P1 = 8*number_of_image_channels*sws*sws
#P2 = 32*number_of_image_channels*sws*sws
#disp12MaxDiff = 1
#preFilterCap = 31
#uniquenessRatio = 5
#speckleWindowSize = 0
#speckleRange = 1
fullDP = False

# create windows
cv2.namedWindow('left_Webcam', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('right_Webcam', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('disparity', cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar(md, wnd, 0, 100, nothing)
cv2.createTrackbar(nd, wnd, 16, 160, nothing)
cv2.createTrackbar(wd, wnd, 21, 255, nothing)
cv2.createTrackbar(dm, wnd, 16, 160, nothing)
cv2.createTrackbar(pf, wnd, 31, 100, nothing)
cv2.createTrackbar(ur, wnd, 5, 15, nothing)
cv2.createTrackbar(sw, wnd, 0, 200, nothing)
cv2.createTrackbar(sr, wnd, 1, 2, nothing)

while(cv2.waitKey(1) & 0xFF != ord('q')):
    ret1, frame_left = cap_left.read()
    ret2, frame_right = cap_right.read()
    # our operations on the frame come here
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)
    cv2.imshow('left_Webcam', gray_left)
    cv2.imshow('right_Webcam', gray_right)

    mDi = cv2.getTrackbarPos(md, wnd)
    nDi = cv2.getTrackbarPos(nd, wnd)
    sws = cv2.getTrackbarPos(wd, wnd)
    dMax = cv2.getTrackbarPos(dm, wnd)
    pfc = cv2.getTrackbarPos(pf, wnd)
    uRat = cv2.getTrackbarPos(ur, wnd)
    swin = cv2.getTrackbarPos(sw, wnd)
    sran = cv2.getTrackbarPos(sr, wnd)

    P1 = 8*number_of_image_channels*sws*sws
    P2 = 32*number_of_image_channels*sws*sws

    #stereo = cv2.StereoSGBM(minDisparity, numDisparities, SADWindowSize, P1, P2, disp12MaxDiff, preFilterCap, uniquenessRatio, speckleWindowSize, speckleRange, fullDP)
    stereo = cv2.StereoSGBM(mDi, nDi, sws, P1, P2, dMax, pfc, uRat, swin, sran, fullDP)

    disparity = stereo.compute(gray_left, gray_right)
    cvuint8 = cv2.convertScaleAbs(disparity)
    cv2.imshow('disparity', cvuint8)
    #print "frame left:",frame_left.dtype
    #print "frame right:",frame_right.dtype
    #print "Disparity:",cvuint8.dtype
    # When everything done, release the capture

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()