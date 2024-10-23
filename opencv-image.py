import cv2

image = cv2.imread("images/miuul.png", 0)
cv2.imshow("Ilk resim",image)

key = cv2.waitKey(0)

if(key==27):
    cv2.destroyAllWindows()
elif(key== ord("s")):
     cv2.imwrite("images/miuul2.png",image)
     cv2.destroyAllWindows()