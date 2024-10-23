import cv2

image = cv2.imread("images/lenna.png")
cv2.imshow("Original", image)
cv2.waitKey(0)

cv2.line(image, (0,0), (512,512), (0,0,255), 3)
cv2.imshow("Line", image)
cv2.waitKey(0)

cv2.rectangle(image,(100,100), (200,200), (255,0,0),cv2.FILLED) #FILLED kısmı eklenirse içini doldurur.
cv2.imshow("Rectangle",image)
cv2.waitKey(0)

cv2.circle(image,(100,100),45,(0,255,0),10)
cv2.imshow("Circle",image)
cv2.waitKey(0)

cv2.putText(image,"Omer Senol",(100,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(100,100,100))
cv2.imshow("Metin",image)
cv2.waitKey(0)