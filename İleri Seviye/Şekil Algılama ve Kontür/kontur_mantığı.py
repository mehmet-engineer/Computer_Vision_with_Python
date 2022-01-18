import cv2
import numpy as np

img = cv2.imread("basic.png")
img_smoothed = cv2.blur(img,(3,3))
img_gray = cv2.Canny(img_smoothed,140,150)
cv2.imshow("original",img_gray)

#Kontur Nedir?
#Aynı renk ve yoğunluğa sahip pixellerin birleştirilmesi
#Birleştirilen bu pixel grubunun kenarlarının çizdirilmesi

"""
contours,hierarchy = cv2.findContours(img_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
# CHAIN_APPROX_NONE --> resimdeki nesnelerin detaylı kontur bilgisi
# RETR_CCOMP --> iç ve dış konturları da bul
# RETR_EXTERNAL --> sadece dış konturlar
# hierarchy --> iç veya konturları gösteren liste verir

for contour in contours:
    cv2.drawContours(img,contour,-1,[0,0,255],thickness=3)
"""

# CHAIN_APPROX_SIMPLE --> resimdeki her bir nesnenin bir tane basit kontur bilgisi
contours,hierarchy = cv2.findContours(img_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv2.drawContours(img,contours,i,[0,0,255],thickness=3)

#NOT: thickness -1 verilirse kontur içi bölgeyi boyar

cv2.imshow("img_display",img)
cv2.waitKey()
cv2.destroyAllWindows()