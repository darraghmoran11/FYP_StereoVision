import cv2
import numpy

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame_video', frame)
    cv2.imshow('frame_video_gray', gray)
    cv2.imshow('frame_video_HSV', HSV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()