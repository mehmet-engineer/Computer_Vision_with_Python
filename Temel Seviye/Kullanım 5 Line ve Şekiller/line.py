import cv2
import numpy as np

resim = cv2.imread("resim.png")

p1 = (0,50)     # (sütun,satır)
p2 = (200,50)
color = [0,0,200]
thickness = 2
cv2.line(resim,p1,p2,color,thickness)

cv2.imshow("Pencere",resim)
cv2.waitKey()
cv2.destroyAllWindows()