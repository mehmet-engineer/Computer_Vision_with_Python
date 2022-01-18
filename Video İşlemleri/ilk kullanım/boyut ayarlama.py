import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

#kameramın özellikleri;
cam_genişlik = kamera.get(3)   #640
cam_yükseklik = kamera.get(4)   #480
cam_fps = kamera.get(5)        #30 FPS

#sağlıksız büyütme;
#kamera.set(3,500)   video pencere boyu
#kamera.set(4,700)   video pencere genişliği

#optik büyütme;
def optical_size(frame,percent):
    yükseklik = int(frame.shape[0] * percent / 100)
    genişlik = int(frame.shape[1] * percent / 100)
    size = (genişlik,yükseklik)  #tuple
    result = cv2.resize(frame,size, interpolation = cv2.INTER_AREA)
    return result

while True:
    red,kare = kamera.read()

    kare2 = optical_size(kare,75)
    cv2.imshow("Resize",kare2)
    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(25)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()


