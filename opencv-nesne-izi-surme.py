import cv2
import numpy as np

cap = cv2.VideoCapture("videos/dog.mp4")


while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sens = 15
    lower_white = np.array([0,0,255-sens])
    upper_white = np.array([255-sens,0,255])
    
    mask = cv2.inRange(hsv,lower_white,upper_white)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    mask = cv2.resize(mask, (300,300))
    frame = cv2.resize(frame, (300,300))
    result = cv2.resize(result, (300,300))
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    