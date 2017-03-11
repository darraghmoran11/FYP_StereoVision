import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('left.png',0)
imgR = cv2.imread('right.png',0)

# disparity settings
minDisparity = 96
numDisparites = 5
SADwindowsize = 600
P1 = 2400
P2 = 20
disp12MaxDiff = 16
preFilterCap = 1
uniquenessRatio = 100
speckleWindowSize = 20
speckleRange = 0
fullDP = false;

stereo = cv2.StereoSGBM(0, minDisparity, numDisparites, SADwindowsize, P1, P2, disp12MaxDiff, preFilterCap, uniquenessRatio, speckleWindowSize, speckleRange, fullDP)

disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity, 'gist_heat')
plt.show()