import cv2
import numpy as np

resim = cv2.imread("resim.png")

point1 = (100,200)    #(sütun,satır)  dikdörtgen sol üst konumu
point2 = (400,500)   #(sütun,satır)  dikdörtgen sağ alt konumu
 
cv2.rectangle(resim,point1,point2,color=[0,0,255],thickness=3)

cv2.imshow("Pencere",resim)
cv2.waitKey()
cv2.destroyAllWindows()