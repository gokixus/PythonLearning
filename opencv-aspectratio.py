import cv2

def resizeWithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    dimension = None
    (h, w) = img.shape[:2]
    
    if width is None and height is None:
        return img
    
    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)
        
    else:
        r = width / float(h)
        dimension = (width, int(h*r))
        
    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("images/kizkulesi.png")
img1 = resizeWithAspectRatio(img, width=None, height=480, inter=cv2.INTER_AREA)
cv2.imshow("Resim", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()