import cv2
import numpy as np 

kamera = cv2.VideoCapture("world.mp4")

while True:
    red,kare = kamera.read()    
    
    cv2.imshow("Kamera",kare)

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    lower = np.array([100,50,50])   
    upper = np.array([140,255,255])
    maske = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(kare,kare, mask=maske)

    median = cv2.medianBlur(result,15)
    cv2.imshow("Median Blur",median)
   

    key = cv2.waitKey(1)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()