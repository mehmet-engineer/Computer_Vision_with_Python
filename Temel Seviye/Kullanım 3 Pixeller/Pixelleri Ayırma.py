import cv2
import numpy as np

resim = cv2.imread("resim.png")

B,G,R = cv2.split(resim)
birleştir = cv2.merge((B,G,R))

cv2.imshow("Birlestirilmis Orjinal",birleştir)
cv2.imshow("Blue Tonlar",B)
cv2.imshow("Green Tonlar",G)
cv2.imshow("Red Tonlar",R)

cv2.waitKey()
cv2.destroyAllWindows()