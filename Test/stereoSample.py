import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('tsukuba_l.png',0)
imgR = cv2.imread('tsukuba_r.png',0)

number_of_image_channels = 2

minDisparity = 0
numDisparities = 16
SADWindowSize = 21
P1 = 8*number_of_image_channels*SADWindowSize*SADWindowSize
P2 = 32*number_of_image_channels*SADWindowSize*SADWindowSize
disp12MaxDiff = 1
preFilterCap = 31
uniquenessRatio = 5
speckleWindowSize = 0
speckleRange = 1
fullDP = False

#cv2.namedWindow('imgL', cv2.WINDOW_NORMAL)
#cv2.namedWindow('imgR', cv2.WINDOW_NORMAL)

# disparity settings
stereo = cv2.StereoSGBM(minDisparity, numDisparities, SADWindowSize, P1, P2, disp12MaxDiff, preFilterCap, uniquenessRatio, speckleWindowSize, speckleRange, fullDP)

#print "imgL: ", imgL.dtype
#print "imgR: ", imgR.dtype
#print "disparity: ", disparity.dtype

disparity = stereo.compute(imgL,imgR)
cvuint8 = cv2.convertScaleAbs(disparity)
plt.imshow(cvuint8, 'gist_heat')
plt.show()