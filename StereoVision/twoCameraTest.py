import numpy as np 
import cv2

capLeft = cv2.VideoCapture(1) #sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
capRight = cv2.VideoCapture(2) #sets cap2 as the second camera

while(True): #while the cameras are working this while loop will be initialized
	#creates the frames for each camera 
	ret, frameLeft = capLeft.read()
	ret, frameRight = capRight.read()

	grayLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
	grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

	#Shows the content each camera is recording
	cv2.imshow("frame left", frameLeft)
	cv2.imshow("frame right", frameRight)

	
	#if loop to break the camera feed when completed. The waitKey determines the number of frames 
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

#Shape of image is accessed by img.shape.
#print "Shape of image: ", frameLeft.shape
#print "Shape of image: ", frameRight.shape

#Total number of pixels
#print "Total number of pixels: ", frameLeft.size
#print "Total number of pixels: ", frameRight.size

#Image datatype
#print frameLeft.dtype
#print frameRight.dtype

#Stops the cameras from recording once connection is broken
capLeft.release()
capRight.release()
cv2.destroyAllWindows() #The two frames are then shut down
