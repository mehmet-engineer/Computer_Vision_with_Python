import cv2
import numpy as np 

kamera = cv2.VideoCapture(1)
lower = np.array([80,90,0])   
upper = np.array([160,255,255])

while True:
    _,img = kamera.read()
    
    img_blurred = cv2.blur(img,(7,7))
    img_hsv = cv2.cvtColor(img_blurred,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv,lower,upper)
    mask = cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask,None,iterations=2)

    #Sadece mavi renkte en büyük konturun alınması -----------------------
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) > 0:
        area_list = []
        for contour in contours:
            area = cv2.contourArea(contour)
            area_list.append(area)

        index = area_list.index(max(area_list))

        cv2.drawContours(img,contours,index,[0,255,255],thickness=3)

        #En büyük Konturu dikdörtgen içine almam için koordinatları ver
        rect = cv2.minAreaRect(contours[index])
        (x,y), (width,height), rotation = rect
        string = "x:{}, y:{}, w:{}, h:{}, rotation:{}".format(np.round(x),
                 np.round(y),np.round(width),np.round(height),np.round(rotation))
        cv2.putText(img,string,(20,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,[255,255,255],2)
        box = cv2.boxPoints(rect)
        box = np.int64(box)

        #bu sefer konturu dikdörtgen halinde göstersin
        cv2.drawContours(img,[box],0,[0,0,255],thickness=3)

        #Konturun merkezini alma
        #Moment --> Yarıçap, alan, ağırlık, pixel yoğunlukları gibi değerleri hesaplar
        M = cv2.moments(contours[index])
        try:
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
            center = (x,y)
            cv2.circle(img,center,5,[0,255,0],-1)
        except ZeroDivisionError:
            pass
        
    cv2.imshow("Output",img)

    if cv2.waitKey(25) == 27:
        break

kamera.release()
cv2.destroyAllWindows()