import numpy as np
import cv2
from matplotlib import pyplot as plt

def changeValue():
    print "DisparityRange:", nDi
    print "BlockSize:", sws
    print "disp12MaxDiff: ", dMax
    print "preFilterCap: ", pfc
    print "uniquenessRatio: ", uRat
    print "speckleWindowSize: ", swin
    print "speckleRange", sran
    pass
    
imgL = cv2.imread('imgL.png')
imgR = cv2.imread('imgR.png')

cv2.namedWindow('imgL', cv2.WINDOW_NORMAL)
cv2.namedWindow('imgR', cv2.WINDOW_NORMAL)

cv2.namedWindow('disparity', cv2.WINDOW_AUTOSIZE)

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

startND = 16 #Start value for ndisparities
startWD = 5 #Start value for SADWindowSize

endND = 272 #End value for ndisparities
endWD = 255 #End value for ndisparities

cv2.createTrackbar(md, wnd, 0, 100, changeValue)
cv2.createTrackbar(nd, wnd, startND, endND, changeValue)
cv2.createTrackbar(wd, wnd, startWD, endWD, changeValue)
cv2.createTrackbar(dm, wnd, 16, 160, changeValue)
cv2.createTrackbar(pf, wnd, 31, 100, changeValue)
cv2.createTrackbar(ur, wnd, 5, 15, changeValue)
cv2.createTrackbar(sw, wnd, 0, 200, changeValue)
cv2.createTrackbar(sr, wnd, 1, 2, changeValue)

while(cv2.waitKey(1) & 0xFF != ord('q')):

    #Convert the video feed to grayscale
    gray_left = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    #Shows the camera frames in grayscale
    cv2.imshow('Left Image', gray_left)
    cv2.imshow('Right Image', gray_right)

    #Adds the trackbar to disparity frame
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
    
    if sws%2==0:
        sws+=1
        
    if sws<startWD:
        sws=5

    if not nDi%16==0:
        nDi=(nDi/16)*16

    #Determine the stereo block matching algorithm for the variables given
    stereo = cv2.StereoSGBM(mDi, nDi, sws, P1, P2, dMax, pfc, uRat, swin, sran, fullDP)

    #Prints out the value of the variables
    print "DisparityRange:", nDi
    print "BlockSize:", sws
    
    #Computes the disparity from the two video feeds
    disparity = stereo.compute(gray_left, gray_right)

    #Disparity needs to be converted to match the format of the camera video feeds
    cvuint8 = cv2.convertScaleAbs(disparity)

    #Displays the disparity map
    cv2.imshow('disparity', cvuint8)