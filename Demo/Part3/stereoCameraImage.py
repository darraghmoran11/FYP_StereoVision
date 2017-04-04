import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('imgL.png',0)
imgR = cv2.imread('imgR.png',0)

#cv2.namedWindow('imgL', cv2.WINDOW_NORMAL)
#cv2.namedWindow('imgR', cv2.WINDOW_NORMAL)

# disparity settings
stereo = cv2.StereoBM(0, ndisparities=16, SADWindowSize=15)

disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity, 'gist_heat')
plt.show()