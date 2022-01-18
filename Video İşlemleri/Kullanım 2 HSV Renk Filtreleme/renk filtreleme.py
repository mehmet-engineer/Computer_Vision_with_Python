import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

#renk filtreleme için HSV (Hue/rengi, Saturation/doygunluk, Value/yoğunluk) daha kullanışlı bir renk uzayıdır
#örneğin açık mavi rengini alabilmek için BGR'da 3 renkle de oynamak zorundayız.
#HSV'de ise hue rengini mavi seçip ve doygunluk değerini de ayarlarsak rahatça açık mavi elde ederiz.

while True:
    red,kare = kamera.read()    
    
    cv2.imshow("Kamera",kare)

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

    #hsv renk skalasında 90 - 140 aralığı mavi değerleridir
    lower = np.array([90,80,80])   
    upper = np.array([140,255,255])
    maske = cv2.inRange(hsv,lower,upper)   #bu aralıktaki değerleri beyaz yap, diğerlerini siyah pixel yap
    cv2.imshow("Maske",maske)

    result = cv2.bitwise_and(kare,kare, mask=maske)
    cv2.imshow("Mavi Renk Filtresi Sonucumuz",result)

    key = cv2.waitKey(25)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()