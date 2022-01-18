import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

while True:
    timer = cv2.getTickCount()
    _,img = kamera.read()

    fps = int(cv2.getTickFrequency() / (cv2.getTickCount() - timer))
    cv2.putText(img,"FPS: {}".format(str(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) == 27:
        break

kamera.release()
cv2.destroyAllWindows()