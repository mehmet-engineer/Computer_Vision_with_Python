import cv2
import numpy as np 
#pip install opencv-contrib-python kurulmalı !!

video = cv2.VideoCapture("cars.mp4")

#Alternatif tracker'lar;                   Deneme doğruluğu:
#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()         **
#tracker = cv2.TrackerKCF_create()         ***
#tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerGOTURN_create()
#tracker = cv2.TrackerMOSSE_create()
#tracker = cv2.TrackerCSRT_create()         ***

tracker = cv2.TrackerCSRT_create() 
_,img = video.read()     #ilk referans
bbox = cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)

#nesneyi seçtikten sonra enter'a bas

vid_genişlik = video.get(3)   
vid_yükseklik = video.get(4)
print(vid_yükseklik,vid_genişlik)
    
while True:
    timer = cv2.getTickCount()
    _,img = video.read()

    success,bbox = tracker.update(img)
    durum = True

    if success == True:
        x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
        cv2.rectangle(img,(x,y),(x+w,y+h),[255,0,0],3)
        cv2.putText(img,"Tracking",(30,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
        
    else:
        cv2.putText(img,"Tracking lost",(30,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    fps = int(cv2.getTickFrequency() / (cv2.getTickCount() - timer))
    cv2.putText(img,"FPS: {}".format(str(fps)),(30,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()