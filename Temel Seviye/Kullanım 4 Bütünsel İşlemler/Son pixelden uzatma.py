import cv2
import numpy as np

resim1 = cv2.imread("araba.png")

resim2 = cv2.copyMakeBorder(resim1,0,0,400,0,cv2.BORDER_REPLICATE)

cv2.imshow("Orjinal",resim1)
cv2.imshow("Border Uzatma",resim2)

cv2.imwrite("yeni.png",resim2)

cv2.waitKey()
cv2.destroyAllWindows()