import cv2, time
import numpy as np 

kamera = cv2.VideoCapture(0)

while True:
    red,kare = kamera.read()    
    cv2.imshow("Kamera",kare)

    #griTon = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)  

    milisaniye = 25
    key = cv2.waitKey(milisaniye)

    # 1 sn 1000 milisaniye
    FPS = 1000 / milisaniye
    print("FPS = ", FPS)

    if key == 27:   #27 --> ESC 
        break

kamera.release()
cv2.destroyAllWindows()