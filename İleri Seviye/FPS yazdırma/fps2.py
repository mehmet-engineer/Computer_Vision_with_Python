import cv2
import time
import numpy as np 

kamera = cv2.VideoCapture(0)

previousTime = 0
currentTime = 0

while True:
    _,img = kamera.read()

    currentTime = time.time()

    #2 frame arası geçen zaman;
    #currentTime - previousTime

    try:
        fps = 1 / (currentTime - previousTime)
    except ZeroDivisionError:
        pass
    
    previousTime = currentTime
    fps = int(fps)
    
    cv2.putText(img,"FPS: {}".format(str(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) == 27:
        break

kamera.release()
cv2.destroyAllWindows()