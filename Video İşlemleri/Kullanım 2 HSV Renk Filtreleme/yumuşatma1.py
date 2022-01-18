import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

while True:
    red,kare = kamera.read()    
    
    cv2.imshow("Kamera",kare)

    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    lower = np.array([100,80,80])   
    upper = np.array([140,255,255])
    maske = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(kare,kare, mask=maske)
    cv2.imshow("Mavi Renk Filtresi",result)

    #kare filtre oluşturma;
    kernel = np.ones((15,15), dtype=np.float32) / 225
    smoothed = cv2.filter2D(result,-1,kernel)
    cv2.imshow("Smoothed",smoothed)

    blur = cv2.GaussianBlur(result, (15,15), 0)
    cv2.imshow("Gaussian Blur",blur)

    median = cv2.medianBlur(result,15)
    cv2.imshow("Median Blur",median)

    bilateral = cv2.bilateralFilter(result,15,75,75)
    cv2.imshow("Bilateral Filtre",bilateral)    

    key = cv2.waitKey(25)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()