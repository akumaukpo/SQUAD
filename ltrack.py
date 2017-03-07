from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np


#initialization

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 50
camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640, 480))

#warmup

time.sleep(0.1)

#capture frames

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #truncate first
    
    rawCapture.truncate(0)
    
    image = frame.array

    blur = cv2.blur(image, (3,3))

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, np.array((0, 200, 200)), np.array((20, 255, 255)))

    green_lower = np.array([50,100,100], dtype="uint8") #76,31,4 - for blue
    green_upper = np.array([70,255,255], dtype="uint8") #225, 88, 50 - for blue
   

    thresh = cv2.inRange(blur, green_lower, green_upper)
    thresh2 = thresh.copy()

    #detect contours, store as best_count

    image, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    max_area = 0
    best_cnt = 1

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
            
#find center and draw a circle
            
    M = cv2.moments(best_cnt)
    cx, cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    
    cv2.circle(blur,(cx,cy),10,(0,0,255), -1)

#show the frame
    
    cv2.imshow("Frame", blur)
    cv2.imshow('thresh', thresh2)
    key = cv2.waitKey(1) & 0xFF

#clear stream in preparation for another frame
    
    rawCapture.truncate(0)
  

    if key == ord('e'):
        sys.exit()
               
                 
    
