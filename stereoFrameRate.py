#!/usr/bin/env python
 
import cv2
import time
 
if __name__ == '__main__' :
 
    # Start default camera
    videoLeft = cv2.VideoCapture(1)
    videoRight = cv2.VideoCapture(2)
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fpsLeft = videoLeft.get(cv2.cv.CV_CAP_PROP_FPS)
        print "Frames per second using videoLeft.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fpsLeft)
    else :
        fpsLeft = videoLeft.get(cv2.CAP_PROP_FPS)
        print "Frames per second using videoLeft.get(cv2.CAP_PROP_FPS) : {0}".format(fpsLeft)
     
    if int(major_ver)  < 3 :
        fpsRight = videoRight.get(cv2.cv.CV_CAP_PROP_FPS)
        print "Frames per second using videoRight.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fpsRight)
    else :
        fpsRight = videoRight.get(cv2.CAP_PROP_FPS)
        print "Frames per second using videoRight.get(cv2.CAP_PROP_FPS) : {0}".format(fpsRight)
 
    # Number of frames to capture
    num_frames = 120;
     
     
    print "Capturing {0} frames".format(num_frames)
 
    # Start time
    start = time.time()
     
    # Grab a few frames
    for i in xrange(0, num_frames) :
        ret, frameLeft = videoLeft.read()

    for i in xrange(0, num_frames) :
        ret, frameRight = videoRight.read()
 
     
    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start
    print "Time taken : {0} seconds".format(seconds)
 
    # Calculate frames per second
    fpsLeft  = num_frames / seconds;
    print "Estimated frames per second : {0}".format(fpsLeft);

    fpsRight  = num_frames / seconds;
    print "Estimated frames per second : {0}".format(fpsRight);
 
    # Release video
    videoLeft.release()
    videoRight.release()