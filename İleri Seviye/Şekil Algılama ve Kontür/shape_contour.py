import cv2
import numpy as np

def getContours(img):
    contours,_ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area>300:
            cv2.drawContours(img2,contour,contourIdx=-1,color=[255,0,0],thickness=3)
            #contourIndex -1 olursa tüm şekilleri dahil et demektir
            length = cv2.arcLength(contour,True)  #yay uzunluğu yani çevre hesabı
            cornerPoints = cv2.approxPolyDP(contour,0.02*length,True)   #0.02 ayarlanabilir
            cornerCount = len(cornerPoints)
            x,y,w,h = cv2.boundingRect(cornerPoints)
            cv2.rectangle(img2,(x,y-15),(x+w,y+h),[0,255,0],2)
            if cornerCount == 3:
                cv2.putText(img2,"Ucgen",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
            elif cornerCount == 4:
                h = float(h)
                w = float(w)
                ratio = w/h
                if ratio > 0.8 and ratio < 1.2:
                    cv2.putText(img2,"Kare",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
                else:
                    cv2.putText(img2,"Dikdortgen",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])
            else:
                cv2.putText(img2,"Daire",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,[0,0,0])

img = cv2.imread("shapes.png")
cv2.imshow("original",img)
img2 = img.copy()
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGR_blur = cv2.GaussianBlur(imgGRAY,(11,11),2)
imgCanny = cv2.Canny(imgGR_blur,100,200)
getContours(imgCanny)

cv2.imshow("Output",img2)
cv2.waitKey()
cv2.destroyAllWindows()

