import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('IMG_5037.JPG',0)
imgR = cv2.imread('IMG_5038.JPG',0)

# disparity settings
numDisparites = 16
SADwindowsize = 21

stereo = cv2.StereoBM(0, ndisparities=numDisparites, SADWindowSize=SADwindowsize)

disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity, 'rainbow')
plt.show()