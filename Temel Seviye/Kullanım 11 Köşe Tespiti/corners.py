import cv2
import numpy as np

#resim köşelerinin tespiti için gri tonlarında ve float32 hassasiyetinde olmalı
BGRresim = cv2.imread("shapes.jpg")
cv2.imshow("orjinal",BGRresim)
GRAYresim = cv2.cvtColor(BGRresim,cv2.COLOR_BGR2GRAY)
GRAYresim = np.float32(GRAYresim)

tahmini_kose = 25     #resimde tahmini maximum köşe sayısı
tarama_mesafesi = 10    #köşeler arası tarama sıklığı mesafesi
hassasiyet = 0.01  
corners = cv2.goodFeaturesToTrack(GRAYresim,tahmini_kose,hassasiyet,tarama_mesafesi)
#bu fonksiyon tespit edilen köşe koordinatlarını float olarak döndürür
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(BGRresim,(x,y),3,[0,0,255],2)

cv2.imshow("Corners",BGRresim)
cv2.waitKey()
cv2.destroyAllWindows()