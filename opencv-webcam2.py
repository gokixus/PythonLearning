import cv2

cam = cv2.VideoCapture(0) # kendi cam'imizi açmak için 0 yazdık

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Görüntü sonlandırıldı.")
        break
    
cam.release()
cv2.destroyAllWindows()