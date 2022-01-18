import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)
nesne = cv2.imread("nesne.png",0)   #nesne gri tonunda alınır
w,h = nesne.shape

while True:
    red,kare = kamera.read()    
    griKare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    #pixelleri baştan sona tara ve nesne ile eşleştir
    #eşleştirme sonucunda her bir pixelin eşleşme oranını döndür
    match_value = cv2.matchTemplate(griKare,nesne,cv2.TM_CCOEFF_NORMED)
    esik = 0.5

    #eşleşen pixellerin x ve y koordinatını al eşleşmeyenleri sil
    #yani resimden sadece eşleşen bölgenin koordinatlarını al
    location = np.where(match_value > esik)

    #bölgenin ilk kordinatını al
    #loc değeri nesnenin sol üst değeri (x,y) = (loc[0],loc[1])
    for loc in zip(*location[::-1]):   
        cv2.rectangle(kare,loc,(loc[0]+h,loc[1]+w), (255,0,0), 1)
        cv2.putText(kare,"nesne",(loc[0],loc[1]+w+20),cv2.FONT_ITALIC,1,[255,0,0])

    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(25)

    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()