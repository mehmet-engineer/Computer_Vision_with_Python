import cv2
import numpy as np

resim = cv2.imread("sau.png")

büyük = cv2.pyrUp(resim)   #2 kat büyüt
küçük = cv2.pyrDown(resim)   #2 kat küçült

cv2.imshow("1",büyük)
cv2.imshow("2",küçük)
cv2.imshow("orjinal",resim)

cv2.waitKey()
cv2.destroyAllWindows()