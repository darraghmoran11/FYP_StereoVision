import numpy as np
import cv2

capLeft = cv2.VideoCapture(0) #sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
capRight = cv2.VideoCapture(1) #sets cap2 as the second camera

while(True):
    # creates the frames for each camera
    ret, frameLeft = capLeft.read()
    ret, frameRight = capRight.read()

    # Shows the content each camera is recording
    cv2.imshow("frame 1", frameLeft)
    cv2.imshow("frame 2", frameRight)

    if not ret:
        break
    k = cv2.waitKey(1)

    # if loop to break the camera feed when completed. The waitKey determines the number of frames
    if k%256 == 27:
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        # SPACE pressed
        imgL_name = "imgL.png"
        cv2.imwrite(imgL_name, frameLeft)
        print("{} written!".format(imgL_name))

   # elif k % 256 ==ord("q"):
        imgR_name = "imgR.png"
        cv2.imwrite(imgR_name, frameRight)
        print("{} written!".format(imgR_name))

capLeft.release()
capRight.release()
cv2.destroyAllWindows() #The two frames are then shut down
