import numpy as np
import cv2

cap = cv2.VideoCapture(0)  # sets cap as the first camera

while (True):  # while the cameras are working this while loop will be initialized
    # creates the frames for each camera
    ret, frame = cap.read()

    grayRight = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Shows the content each camera is recording
    cv2.imshow("frame", frame)

    # if loop to break the camera feed when completed. The waitKey determines the number of frames
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# Stops the cameras from recording once connection is broken
cap.release()
cv2.destroyAllWindows()  # The two frames are then shut down