import cv2
import numpy as np 

kamera = cv2.VideoCapture(1)

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Thresh1","TrackBars",0,255,empty)
cv2.createTrackbar("Thresh2","TrackBars",0,255,empty)
cv2.createTrackbar("Area min","TrackBars",100,9000,empty)
kernel = np.ones((4,4))

#üzerine işlem yapılacak img_islem
#görüntülenecek original çıktı IMG_display
def getContours(img_islem,IMG_display):   
    contours,_ = cv2.findContours(img_islem,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>area_min:
            cv2.drawContours(IMG_display,contour,contourIdx=-1,color=[255,0,0],thickness=3)
            length = cv2.arcLength(contour,True)
            cornerPoints = cv2.approxPolyDP(contour,0.02*length,True)
            cornerCount = len(cornerPoints)
            x,y,w,h = cv2.boundingRect(cornerPoints)
            cv2.rectangle(IMG_display,(x,y),(x+w,y+h),[0,255,0],3)
            cv2.putText(IMG_display,"{} gen".format(str(cornerCount)),(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
            cv2.putText(IMG_display,"{} area".format(str(area)),(x,y+20),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])


while True:
    _,img = kamera.read()
    imgBlur = cv2.GaussianBlur(img,(5,5),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    
    thresh1 = cv2.getTrackbarPos("Thresh1","TrackBars")
    thresh2 = cv2.getTrackbarPos("Thresh2","TrackBars")
    area_min = cv2.getTrackbarPos("Area min","TrackBars")
    imgCanny = cv2.Canny(imgGray,thresh1,thresh2)
    dilation = cv2.dilate(imgCanny,kernel,iterations=1)

    getContours(dilation,img)
    cv2.imshow("Output",img)

    if cv2.waitKey(25) == 27:
        break

kamera.release()
cv2.destroyAllWindows()