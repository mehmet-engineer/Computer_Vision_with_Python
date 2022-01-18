import cv2
import numpy as np

fotoGRI = cv2.imread("foto.png",0)
hist = cv2.equalizeHist(fotoGRI)

yan_yana = np.hstack((fotoGRI,hist))
cv2.imshow("Histogram Equalization",yan_yana)

cv2.waitKey()
cv2.destroyAllWindows()
