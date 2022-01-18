import cv2
import numpy as np

frontalFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
kamera = cv2.VideoCapture(0)

#yüzü algılayana kadar kamerada yüz ara
while True:
    _,kare = kamera.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    face_rects = frontalFace.detectMultiScale(kareGRAY,1.3,4)
    cv2.imshow("Kamera",kare)
    
    if len(face_rects) > 0 or cv2.waitKey(25) == 27:
        (x,y,w,h) = face_rects[0]
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)
        cv2.imshow("Kamera",kare)
        break

#yüz bölgesini al
(face_x, face_y, w, h) = tuple(face_rects[0])
track_window = (face_x, face_y, w, h)

bolge = kare[face_y:face_y + h, face_x : face_x + w]

hsv_roi = cv2.cvtColor(bolge, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
cv2.normalize(roi_hist , roi_hist ,0 ,255, cv2.NORM_MINMAX)

# takip icin gerekli durdurma kriterleri;
# bu özellikler oluştuğunda takibi durdur
yinele = 5   #hesaplanacak maksimum oge sayısı
eps = 1      #degisiklik
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, yinele, eps)

#Takip için yeni döngüye gir
while True:
    success1, frame = kamera.read()
    
    if success1 == True:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # histogram ve piksel yoğunluğunu karşılaştırma
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)

        success2,track_window = cv2.meanShift(dst, track_window, term_crit)
        
        x,y,w,h = track_window
        
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),5)
        
        cv2.imshow("Takip", img2)
        
        if cv2.waitKey(25) == 27:
            break

kamera.release()
cv2.destroyAllWindows()