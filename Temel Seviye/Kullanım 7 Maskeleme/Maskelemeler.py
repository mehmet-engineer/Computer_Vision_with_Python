import cv2
import numpy as np

arkaplan = cv2.imread("resim.png")
logo = cv2.imread("sau.png")
griLogo = cv2.imread("sau.png",0)
cv2.imshow("original",logo)

#resmi tek kanal (Gri) hale getirme;
#logo_gri = cv2.cvtColor(griLogo,cv2.COLOR_BGR2GRAY)

boy, genişlik = griLogo.shape

#eğer resim sadece iki farklı pixellerden oluşsaydı
#pixelleri şöyle bulabilirdik;
"""liste = []
for i in range(400):
    for j in range(640):
        if griLogo[i,j] not in liste:
            liste.append(griLogo[i,j])"""

min = 100
ret,maske = cv2.threshold(griLogo,min,255,cv2.THRESH_BINARY)
#min değerin üstündeki pixelleri 255 değerinde (beyaz) yap
#min değerin altındakileri de 0 değerinde yap yani siyah yap.

# uyumlu eşik fonksiyonu (arkaplandan ayrışması zor olan nesnelerde kullanılabilir)
maske2 = cv2.adaptiveThreshold(griLogo,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
#11 boyutlu kareler ile 8 constant değerinde eşik ortalamaları al ve maskele
cv2.imshow("maske2",maske2)

#farklı threshold metotları, alternatif denenebilir;
#ret,maske = cv2.threshold(griLogo,min,255,cv2.THRESH_TRUNC)
#ret,maske = cv2.threshold(griLogo,min,255,cv2.THRESH_TOZERO)

mask_inverse = cv2.bitwise_not(maske)   #0'ları 255, 255'leri 0 yap.

#bit_and eşleştirmesi:  -------------------------------------------

bolge = arkaplan[0:boy,0:genişlik]
entegre1 = cv2.bitwise_and(bolge,bolge,mask=maske)
"""Bolge ile maskenin pixel bitlerini AND türünde eşleştir"""
"""beyaz arkaplanı olan maske ile arkaplandaki pixel eşleri için;"""
"""background(10111001) and beyaz(11111111) = sonuç(10111001) yani arkaplan korundu"""
"""background(10111001) and siyah(00000000) = sonuç(00000000) yani siyah nesne korundu"""

entegre2 = cv2.bitwise_and(bolge,bolge,mask=mask_inverse)
"""Eğer siyah arkaplanı olan maske ile bolge eşleştirilirse"""
"""Bu sefer nesne içine arkaplan oluşur"""
# -----------------------------------------------------------------

#Eğer entegre1 ile arkaplanı siyah, kendisi renkli olan resim add ile toplanırsa;
#Siyah pixel 0 değerinde olduğundan eklendiği pixel değerini direk alır
#arkaplan üstüne renkli entegre yapılmış olur.
#renkli_entegre = cv2.add(entegre1,LogoOnBlack)

arkaplan[0:boy,0:genişlik] = entegre1

cv2.imshow("Arkaplan Uzeri siyah Logo",entegre1)
cv2.imshow("Nesne icinde arkaplan",entegre2)
cv2.imshow("Mask",maske)
cv2.imshow("Ters Mask",mask_inverse)
cv2.imshow("Son Hal",arkaplan)

cv2.waitKey()
cv2.destroyAllWindows()