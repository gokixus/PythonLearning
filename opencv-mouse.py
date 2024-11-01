import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
def draw(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN: # sol fare tuşuna basıldığında çizim başlar.
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: #fare hareket ederken drawing açıksa çizmeye devam eder
        if drawing:
            cv2.circle(img, (x,y), 5, (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP: #sol fale tuşu bırakılığında çizim durur.
        drawing = False
        cv2.circle(img, (x,y), 5, (0,255,0), -1)



img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow("Cizim")
cv2.setMouseCallback("Cizim", draw)
while True:
    cv2.imshow("Cizim", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
