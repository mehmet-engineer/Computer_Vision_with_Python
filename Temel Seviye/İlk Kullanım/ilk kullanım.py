import cv2

#resmi dijital numpy dizisine çevirerek oku
#resim = cv2.imread("logo.png",0)   --> 0 parametresi resmi gri tonlarında okur

resim = cv2.imread("logo.png")
cv2.imshow("Pencere",resim)

img_info = resim.shape   # 568 x 270 genişlik ve boy, 3 (RGB) renk kanallı
img_pixels = resim.size    # genişlik x boy = pixel_sayısı

cv2.imwrite("logo_yeni.png",resim)   #save kaydetme

key = cv2.waitKey()
# resim açıkken herhangi bir tuşa basılana kadar beklet
# hangi tuşa basılırsa o tuş karakterinin onluk (decimal) int çıktısını verir

if key == 27:
    print("ESC ye basıldı.")

if key == ord("q"):   #q tuşunu decimal'e çevir
    print("q ye basıldı.")

cv2.destroyAllWindows()