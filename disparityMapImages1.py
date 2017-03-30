import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('IMG_5037.JPG',0)
imgR = cv2.imread('IMG_5038.JPG',0)

# disparity settings
minDisparity = 96
numDisparites = 16
SADwindowsize = 5
P1 = 0
P2 = 0
disp12MaxDiff = 16
preFilterCap = 1
uniquenessRatio = 100
speckleWindowSize = 20
speckleRange = 0
fullDP = True;

stereo = cv2.StereoSGBM(minDisparity, numDisparites, SADwindowsize, P1, P2, disp12MaxDiff, preFilterCap, uniquenessRatio, speckleWindowSize, speckleRange, fullDP)

disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity, 'gist_heat')
plt.show()