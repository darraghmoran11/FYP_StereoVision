import numpy as np
import cv2
from matplotlib import pyplot as plt

def changeValue():
    print "DisparityRange:", ndi
    print "BlockSize:", sws
    pass
    
imgL = cv2.imread('tsukuba_l.png')
imgR = cv2.imread('tsukuba_r.png')

#cv2.namedWindow('imgL', cv2.WINDOW_NORMAL)
#cv2.namedWindow('imgR', cv2.WINDOW_NORMAL)

cv2.namedWindow('disparity', cv2.WINDOW_AUTOSIZE)

dr = 'DisparityRange'
bs = 'BlockSize'
disp = 'disparity'

ndi = dr
sws = bs

startND = 16 #Start value for ndisparities
startWD = 5 #Start value for SADWindowSize

endND = 272 #End value for ndisparities
endWD = 255 #End value for ndisparities

#ndisparitiesRange = endND - startND
#interval =  ndisparitiesRange/16

#Creates the trackbar for the ndisparites and SADWindowSize variables
cv2.createTrackbar(dr, disp, startND, endND, changeValue)
cv2.createTrackbar(bs, disp, startWD, endWD, changeValue)

while(cv2.waitKey(1) & 0xFF != ord('q')):

    #Convert the video feed to grayscale
    gray_left = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    #Shows the camera frames in grayscale
    cv2.imshow('Left Image', gray_left)
    cv2.imshow('Right Image', gray_right)

    #Adds the trackbar to disparity frame
    ndi=cv2.getTrackbarPos(dr, disp)
    sws=cv2.getTrackbarPos(bs, disp)
    
    if sws%2==0:
        sws+=1
        
    if sws<startWD:
        sws=5

    if not ndi%16==0:
        ndi=(ndi/16)*16

    #Determine the stereo block matching algorithm for the variables given
    stereo = cv2.StereoBM(0, ndi, sws)

    #Prints out the value of the variables
    print "DisparityRange:", ndi
    print "BlockSize:", sws
    
    #Computes the disparity from the two video feeds
    disparity = stereo.compute(gray_left, gray_right)

    #Disparity needs to be converted to match the format of the camera video feeds
    cvuint8 = cv2.convertScaleAbs(disparity)

    #Displays the disparity map
    cv2.imshow('disparity', cvuint8)
    #print "frame left:",frame_left.dtype
    #print "frame right:",frame_right.dtype
    #print "Disparity:",cvuint8.dtype
    # When everything done, release the capture


#plt.imshow(disparity, 'gist_heat')
#plt.show()