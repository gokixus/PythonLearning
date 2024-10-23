import cv2
import time

cap = cv2.VideoCapture("videos/video.mp4")
    
if cap.isOpened() == False:
    print("Video aktarılamadı.")

while True:
    ret, frame = cap.read()

    if ret == True:
        time.sleep(0.01)
        cv2.imshow("Video",frame)   
    else:
        break
        
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cap.release()