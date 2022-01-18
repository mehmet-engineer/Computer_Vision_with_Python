import cv2
import numpy as np

arkaplan1 = np.zeros((500,500,3))
cv2.imshow("Once",arkaplan1)

arkaplan2 = np.ones((500,500,3))

arkaplan3 = np.zeros((500,500,3))

for i in range(500):
    for j in range(500):
        arkaplan3[i,j] = [200,20,0]

cv2.namedWindow("Empty", cv2.WINDOW_NORMAL)  #boş bir pencere oluştur
cv2.resizeWindow("Empty", 480, 270)

empty = np.empty((200,200))
cv2.imshow("bos",empty)

cv2.imshow("2",arkaplan2)
cv2.imshow("3",arkaplan3)

arkaplan1[:] = [255,0,0]
cv2.imshow("Sonra",arkaplan1)

cv2.waitKey()
cv2.destroyAllWindows()