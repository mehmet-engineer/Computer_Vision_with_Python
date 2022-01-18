import cv2
import numpy as np 

#mavi
lower_M = np.array([86,80,80])   
upper_M = np.array([140,255,255])

#yeşil
lower_Y = np.array([40,80,80])   
upper_Y = np.array([80,255,255])

#kırmızı
lower_K = np.array([160,80,80])   
upper_K = np.array([180,255,255])

kamera = cv2.VideoCapture(1)

while True:
    red,kare = kamera.read()
    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)

    maskeBlue = cv2.inRange(hsv,lower_M,upper_M)
    maskeGreen = cv2.inRange(hsv,lower_Y,upper_Y)
    maskeRed = cv2.inRange(hsv,lower_K,upper_K)

    resultBlue = cv2.bitwise_and(kare,kare, mask=maskeBlue)
    resultGreen = cv2.bitwise_and(kare,kare, mask=maskeGreen)
    resultRed = cv2.bitwise_and(kare,kare, mask=maskeRed)
    
    contours,_ = cv2.findContours(maskeBlue,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        if area>400:
            length = cv2.arcLength(i,True)  
            cornerPoints = cv2.approxPolyDP(i,0.02*length,True)
            cornerCount = len(cornerPoints)
            x,y,w,h = cv2.boundingRect(cornerPoints)
            cv2.rectangle(kare,(x,y-15),(x+w,y+h),[255,0,0],2)
            cv2.putText(kare,"Blue",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,[255,0,0],1)

    contours,_ = cv2.findContours(maskeGreen,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        if area>400:
            length = cv2.arcLength(i,True)  
            cornerPoints = cv2.approxPolyDP(i,0.02*length,True)
            cornerCount = len(cornerPoints)
            x,y,w,h = cv2.boundingRect(cornerPoints)
            cv2.rectangle(kare,(x,y-15),(x+w,y+h),[0,255,0],2)
            cv2.putText(kare,"Green",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,[0,255,0],1)

    contours,_ = cv2.findContours(maskeRed,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        if area>400:
            length = cv2.arcLength(i,True)  
            cornerPoints = cv2.approxPolyDP(i,0.02*length,True)
            cornerCount = len(cornerPoints)
            x,y,w,h = cv2.boundingRect(cornerPoints)
            cv2.rectangle(kare,(x,y-15),(x+w,y+h),[0,0,255],2)
            cv2.putText(kare,"Red",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,[0,0,255],1)

    cv2.imshow("kare",kare)
    if cv2.waitKey(25) == 27:
        break

kamera.release()
cv2.destroyAllWindows()