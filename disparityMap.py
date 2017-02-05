import numpy as np
import cv2
from matplotlib import pyplot as plt

capLeft = cv2.VideoCapture(0)  # sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
capRight = cv2.VideoCapture(1)  # sets cap2 as the second camera

while (True):  # while the cameras are working this while loop will be initialized
    # creates the frames for each camera
    ret, frameLeft = capLeft.read()
    ret, frameRight = capRight.read()

    grayLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

    # Shows the content each camera is recording
    cv2.imshow("frame 1", frameLeft)
    cv2.imshow("frame 2", frameRight)

    #Plots the disparity Map
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL, imgR)
    plt.imshow(disparity, 'gray')
    plt.show()

    # if loop to break the camera feed when completed. The waitKey determines the number of frames
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Stops the cameras from recording once connection is broken
capLeft.release()
capRight.release()
cv2.destroyAllWindows()  # The two frames are then shut down
