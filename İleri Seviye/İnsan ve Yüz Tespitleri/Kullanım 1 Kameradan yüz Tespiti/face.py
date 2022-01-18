import cv2
import numpy as np

frontalFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
kamera = cv2.VideoCapture(0)

while True:
    _,kare = kamera.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    #daha iyi bir sonuç için ayarlanabilir;
    scale = 1.3     #nesne ölçeği
    neighbor = 4     #nesnelerin birbirine yakınlığı
    face_locs = frontalFace.detectMultiScale(kareGRAY,scale,neighbor)
    #[[x1,y1,x2,y2]]  x1,y1 --> yüzün sol üst pixel konumu, x2,y2 --> yüzün genişlik ve boy uzaklığı

    for (x,y,w,h) in face_locs:
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)
    
    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(30)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()