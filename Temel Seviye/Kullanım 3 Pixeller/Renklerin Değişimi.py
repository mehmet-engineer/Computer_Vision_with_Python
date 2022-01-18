import cv2
import numpy as np

resim = cv2.imread("resim.png")

resim[:,:, 0] = 255
cv2.imshow("Blue Degeri Maximum",resim)

#resim[:,:, 1] = 255   green değeri max
#resim[:,:, 2] = 255   red değeri max

#resim[0:200,0:200, 2]  bölgenin red değerini artır

cv2.waitKey()
cv2.destroyAllWindows()