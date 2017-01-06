import numpy as np
import cv2

cap = cv2.VideoCapture(2)

frames = []

while True:
    ret,im = cap.read()

    cv2.imshow("frame", im)
    frames.append(im)

    print(cap.read())

    if cv2.waitKey(10) == 27:
        break
frames = np.array(frames)

print im.shape
print frames.shape

cap.release()
cv2.destroyAllWindows()