import cv2
import numpy as np 

img_original = cv2.imread("coins.jpg")
img_original = cv2.resize(img_original,(640,440))
cv2.imshow("orjinal",img_original)
img = cv2.blur(img_original,(5,5))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2",img)

_,thresh = cv2.threshold(img,75,255,cv2.THRESH_BINARY)
cv2.imshow("img3 thresh maskesi",thresh)

#erosion ve opening küçültür
#diolation ve closing genişletir
kernel = np.ones((6,6), dtype=np.uint8)
erosion = cv2.erode(thresh,kernel, iterations=1)
diolation = cv2.dilate(thresh,kernel, iterations=1)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel,iterations=2)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations=2)

cv2.imshow("img4 erosyon",erosion)
cv2.imshow("img5 diolasyon",diolation)
cv2.imshow("img6 opening",erosion)
cv2.imshow("img7 closing",diolation)
     
cv2.waitKey()
cv2.destroyAllWindows()