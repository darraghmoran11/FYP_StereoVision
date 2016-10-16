import numpy as np 
import cv2

cap1 = cv2.VideoCapture(1) #sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
cap2 = cv2.VideoCapture(2) #sets cap2 as the second camera

while(True): #while the cameras are working this while loop will be initialized
	#creates the frames for each camera 
	ret, frame1 = cap1.read() 
	ret, frame2 = cap2.read()

	#Shows the content each camera is recording
	cv2.imshow("frame 1", frame1)
	cv2.imshow("frame 2", frame2)
	
	#if loop to break the camera feed when completed. The waitKey determines the number of frames 
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

#Stops the cameras from recording once connection is broken
cap1.release()
cap2.release()
cv2.destroyAllWindows() #The two frames are then shut down 