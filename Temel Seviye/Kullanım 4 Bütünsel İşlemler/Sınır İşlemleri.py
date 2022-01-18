import cv2
import numpy as np

resim = cv2.imread("resim.png")

#kenarlardan 100 pixel 4 tarafa aynala
resim2 = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#resmi kenarlardan tekrarla
resim3 = cv2.copyMakeBorder(resim,200,200,200,200,cv2.BORDER_WRAP)

#kenarlardan sabit pixelle uzat
resim4 = cv2.copyMakeBorder(resim,200,200,200,200,cv2.BORDER_CONSTANT,value=[255,255,255])

cv2.imshow("Border Aynalar",resim2)
cv2.imshow("Border Tekrarlama",resim3)
cv2.imshow("Border Uzat",resim4)
cv2.waitKey()
cv2.destroyAllWindows()