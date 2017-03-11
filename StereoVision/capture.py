import cv2
import numpy as np


def __capture__(capLeft,capRight):
	#index1 = The index of camera 1
	#index2 = The index of camera 2

	while(True):
		#creates the frames for each camera 
		ret, frameLeft = capLeft.read()
		ret, frameRight = capRight.read()

		grayLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
		grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

