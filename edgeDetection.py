import cv2
import numpy as np

capLeft = cv2.VideoCapture(0) #sets cap1 as the first camera (0 is the default laptop camera which isn't being used)
capRight = cv2.VideoCapture(1) #sets cap2 as the second camera

while (True):

    ret, frameLeft = capLeft.read()
    ret, frameRight = capRight.read()
    hsv = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frameRight, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frameLeft, frameLeft, mask=mask)

    cv2.imshow('Original Left', frameLeft)
    cv2.imshow('Original Right', frameRight)
    edgesLeft = cv2.Canny(frameLeft, 100, 200)
    edgesRight = cv2.Canny(frameRight, 100, 200)
    cv2.imshow('Edges Left', edgesLeft)
    cv2.imshow('Edges Right', edgesRight)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capLeft.release()
capRight.release()
cv2.destroyAllWindows()