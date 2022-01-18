import cv2
import numpy as np

resim1 = cv2.imread("sam.jpg")
resim2 = cv2.imread("iph.jpg")

i = 0.01
j = 1-i

while True:
    resim_mix = cv2.addWeighted(resim1,i,resim2,j, 0)
    cv2.imshow("Kamera",resim_mix)
    key = cv2.waitKey(50)

    i = i + 0.01
    j = 1-i

    if key == 27 or i > 1:
        break

cv2.destroyAllWindows()