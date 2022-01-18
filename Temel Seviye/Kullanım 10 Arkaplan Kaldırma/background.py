import cv2
import numpy as np

resim = cv2.imread("resim.png")
h,w,_ = resim.shape
arkaplan = np.zeros((h,w), np.uint8)

backModel = np.zeros((1,65), dtype=np.float64)   #standart kodlar
frontModel = np.zeros((1,65), dtype=np.float64)

bolge = (0,0,w-1,h-1)  #arkaplan kaldırma işleminin bölgeyle sınırlandırılması

#resimdeki pixellerin renk farklarını inceler, arkaplan matrisinin içinde;
#ön objenin pixellerine 1 ve 3 değerini, arkaplan olduğunu tespit ederse  0 ve 2 değerini atar.
cv2.grabCut(resim,arkaplan,bolge,backModel,frontModel,5,cv2.GC_INIT_WITH_RECT)

#arkaplan matrisindeki 0 ve 2'leri 0 yap, geri kalanı 1 olsun.
mask2 = np.where((arkaplan == 0) | (arkaplan == 2), 0, 1).astype(np.uint8)

# mask2 tek kanallı oldu değeri sadece 0 ve 1 lerden oluşuyor, kontrol edebilirsin;
"""for x in range(mask2.shape[0]):
       for y in range(mask2.shape[1]):
           print("satır:{} - sütun:{} - değer:{}".format(x,y,mask2[x,y]))"""

#mask2(tek kanallı) ve resim(3 kanallı) 321x800 matrisinde
#vektörel çarpım için mask2'nin transpozunu alıyoruz
resim = resim * mask2[:,:,np.newaxis]
# 0 ile çarpılan pixel arkaplan halini alır (siyah)
# 1 ile çarpılan pixel korunur ve nesne ön plana çıkar

cv2.imshow("arkaplan",mask2)
cv2.imshow("resim",resim)
cv2.waitKey()
cv2.destroyAllWindows()