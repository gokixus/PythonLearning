import cv2
import numpy as np

img1 = cv2.imread("images/cv2.png")
img2 = cv2.imread("images/d.jpg")

toplam = cv2.addWeighted(img1,0.7,img2,0.3, 0)
cv2.imshow("Resim", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()