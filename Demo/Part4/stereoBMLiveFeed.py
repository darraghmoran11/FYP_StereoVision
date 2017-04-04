import numpy as np
import cv2
import time

def changeValue():
    print "DisparityRange:", ndi
    print "BlockSize:", sws
    pass

#Capture the camera video feeds
cap_left = cv2.VideoCapture(1)
cap_right = cv2.VideoCapture(2)

#Create the windows that the cameras and disparity feed will be  displayed on
cv2.namedWindow('left_Webcam', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('right_Webcam', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('disparity', cv2.WINDOW_AUTOSIZE)

dr = 'DisparityRange'
bs = 'BlockSize'
disp = 'disparity'

ndi = dr
sws = bs

startND = 16 #Start value for ndisparities
startWD = 5 #Start value for SADWindowSize

endND = 272 #End value for ndisparities
endWD = 255 #End value for ndisparities

#ndisparitiesRange = endND - startND
#interval =  ndisparitiesRange/16

#Creates the trackbar for the ndisparites and SADWindowSize variables
cv2.createTrackbar(dr, disp, startND, endND, changeValue)
cv2.createTrackbar(bs, disp, startWD, endWD, changeValue)

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.

if int(major_ver)  < 3 :
    fpsLeft = cap_left.get(cv2.cv.CV_CAP_PROP_FPS)
    print "Frames per second using cap_left.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fpsLeft)
else :
    fpsLeft = cap_left.get(cv2.CAP_PROP_FPS)
    print "Frames per second using cap_left.get(cv2.CAP_PROP_FPS) : {0}".format(fpsLeft)

if int(major_ver)  < 3 :
    fpsRight = cap_right.get(cv2.cv.CV_CAP_PROP_FPS)
    print "Frames per second using cap_right.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fpsRight)
else :
    fpsRight = cap_right.get(cv2.CAP_PROP_FPS)
    print "Frames per second using cap_right.get(cv2.CAP_PROP_FPS) : {0}".format(fpsRight)

# Number of frames to capture
num_frames = 50;


print "Capturing {0} frames".format(num_frames)

# Start time
start = time.time()

# Grab a few frames
for i in xrange(0, num_frames) :
    ret, frameLeft = cap_left.read()

for i in xrange(0, num_frames) :
    ret, frameRight = cap_right.read()


# End time
end = time.time()

# Time elapsed
seconds = end - start

while(cv2.waitKey(1) & 0xFF != ord('q')):
    #Camera video feeds asigned to appropriate frames
    ret1, frame_left = cap_left.read()
    ret2, frame_right = cap_right.read()

    #Convert the video feed to grayscale
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

    #Shows the camera frames in grayscale
    cv2.imshow('left_Webcam', gray_left)
    cv2.imshow('right_Webcam', gray_right)

    #Adds the trackbar to disparity frame
    ndi=cv2.getTrackbarPos(dr, disp)
    sws=cv2.getTrackbarPos(bs, disp)
    
    if sws%2==0:
        sws+=1
        
    if sws<startWD:
        sws=5

    if not ndi%16==0:
        ndi=(ndi/16)*16

    #Determine the stereo block matching algorithm for the variables given
    stereo = cv2.StereoBM(0, ndi, sws)

    #Prints out the value of the variables
    print "DisparityRange:", ndi
    print "BlockSize:", sws
    
    #Computes the disparity from the two video feeds
    disparity = stereo.compute(gray_left, gray_right)

    #Disparity needs to be converted to match the format of the camera video feeds
    cvuint8 = cv2.convertScaleAbs(disparity)

    #Displays the disparity map
    cv2.imshow('disparity', cvuint8)

    f = 0.4 #focal length
    b = 8.4 #baseline value
    a = f * b

    D = a/disparity

    #print "frame left:",frame_left.dtype
    #print "frame right:",frame_right.dtype
    #print "Disparity:",cvuint8.dtype
    # When everything done, release the capture

print "Time taken : {0} seconds".format(seconds)

fpsLeft  = num_frames / seconds;
print "Estimated frames per second : {0}".format(fpsLeft);

fpsRight  = num_frames / seconds;
print "Estimated frames per second : {0}".format(fpsRight);

print "Depth Matrix: ", D

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()