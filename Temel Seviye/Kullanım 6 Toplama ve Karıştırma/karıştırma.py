import cv2
import numpy as np

resim1 = cv2.imread("sam.jpg")
resim2 = cv2.imread("iph.jpg")
#resim matrislerinin toplanabilmesi için pixel boyutları aynı olmalı!

resim3 = cv2.add(resim1,resim2)                       # %50 ye %50
resim4 = cv2.addWeighted(resim1,0.2,resim2,0.8, 0)    # %20 ye %80 oranında

cv2.imshow("Esit Agirlikli Toplama",resim3)
cv2.imshow("Belirli Agirikli Toplama",resim4)
cv2.waitKey()
cv2.destroyAllWindows()