import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('imgL_0.png')
imgR = cv2.imread('imgR_0.png')

grayImgL = cv2.imread('imgL_0.png',0)
grayImgR = cv2.imread('imgR_0.png',0)

# disparity settings
numDisparites = 16
SADwindowsize = 21

stereo = cv2.StereoBM(0, ndisparities=numDisparites, SADWindowSize=SADwindowsize)

cv2.imshow("Left image", imgL)
cv2.imshow("Right image", imgR)
k=cv2.waitKey(0) #timing in ms, keyboard binding function
if k == 27: #wait for esc key interrupt
	cv2.destroyAllWindows() #destroy window and escape from program

disparity = stereo.compute(grayImgL,grayImgR)
plt.imshow(disparity, 'gray')
plt.show()