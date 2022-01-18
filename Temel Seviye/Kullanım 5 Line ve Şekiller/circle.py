import cv2
import numpy as np

resim = cv2.imread("resim.png")

central_point = (400,500)
radius = 100
color = [0,0,220]
thickness = 2

cv2.circle(resim,central_point,radius,color,thickness)

cv2.imshow("Pencere",resim)
cv2.waitKey()
cv2.destroyAllWindows()