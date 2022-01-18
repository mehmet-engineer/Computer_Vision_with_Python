import cv2
import numpy as np 

#VideoCapture(0) --> PC tanımlı kamerası
#VideoCapture(1) --> USB'ye bağlı harici kamera
#VideoCapture("videom.mp4") --> varolan video dosyası
kamera = cv2.VideoCapture(0)

if kamera.isOpened() == False:
    print("Kamera tanınmadı!")
    exit()

while True:
    red,kare = kamera.read()    #her birim zamanda kameradan görüntü karesi oku
    cv2.imshow("Kamera",kare)   #görüntü karelerini göster
    print(kare)
    
    if red == False:
        print("Kamera açık değil. Görüntü Okunamıyor.")
        break

    key = cv2.waitKey(25)   #hem 25 milisaniye beklet hem de klavyeden bi tuşa basılırsa key değerine at
    if key == ord("q"):     # q tuşuna basılırsa döngüden çık
        break

kamera.release()
cv2.destroyAllWindows()