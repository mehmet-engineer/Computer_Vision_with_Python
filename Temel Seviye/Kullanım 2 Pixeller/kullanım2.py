import cv2
import numpy as np

resim = cv2.imread("resim.png")

pixel = resim[100,200]    
#pixel konumunu girerek o konumdaki pixelin renk listesini aldık
print(resim[100,200])

#sadece belli renk değerlerini alma
b,g,r = cv2.split(resim)

#pixelin rengini değiştirme
for i in range(500):
    resim[500,i] = [255,255,255]

parça = resim[0:400,0:400]   #resim[x1:x2,y1,y2]

#pixel çoklu değiştirme
parça2 = resim[500:600,0:400]
resim[0:100,0:400] = parça2

cv2.imshow("Penceremiz",resim)
cv2.imshow("Parca",parça)

cv2.waitKey()
cv2.destroyAllWindows()