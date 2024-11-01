import cv2
import numpy as np

image =np.zeros((512,512,3), np.uint8)

# cv2.line(image, (0,0), (512,512), (255,0,0), 5) #en üst sol noktadan en alt sağ noktaya çizgi çeker, (255,0,0) değeri renk bgr değeridir, en sondaki 5 sayısı da kalınlık değeri
# cv2.line(image, (200,0), (512,512), (0,255,0), 5)

cv2.rectangle(image, (300,300), (512,512), (255,0,0), 5)
cv2.rectangle(image, (300,300), (0,0), (96,142,255), -1) #-1 yerine cv2.FIILED de yazılabilir şeklin içini doldurur.



cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()