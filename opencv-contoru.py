import cv2

img = cv2.imread("images/contour1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
output = img.copy()

cv2.drawContours(output, contours, -1, (0,255,0), 2)

cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
cv2.imshow("Contours", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
