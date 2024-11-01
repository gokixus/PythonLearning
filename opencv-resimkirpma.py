import cv2

img = cv2.imread("images/kizkulesi.png")
print(img)

kirpilmisResim1 = img[0:400,0:400] #[y_start:y_end, x_start:x_end]
kirpilmisResim2 = img[100:400,0:400]
cv2.imshow("Tam Resim", img)
cv2.imshow("Kirpilmis Resim 1", kirpilmisResim1)
cv2.imshow("Kirpilmis Resim 2", kirpilmisResim2)



cv2.waitKey(0)
cv2.destroyAllWindows()