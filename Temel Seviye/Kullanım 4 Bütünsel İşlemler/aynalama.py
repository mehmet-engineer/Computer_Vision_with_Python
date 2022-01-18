import cv2
import numpy as np

resim1 = cv2.imread("araba.png")
boy, genişlik, kanal = resim1.shape

resim2 = cv2.flip(resim1,0)   #vertical
resim3 = cv2.flip(resim1,1)   #horizantal

cv2.imshow("Orjinal",resim1)
cv2.imshow("Dikey Ayna",resim2)
cv2.imshow("Dusey Ayna",resim3)
cv2.waitKey()
cv2.destroyAllWindows()