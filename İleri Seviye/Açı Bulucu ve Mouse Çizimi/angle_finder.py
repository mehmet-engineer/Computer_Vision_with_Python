import cv2
import numpy as np
import math

img = cv2.imread("angles.png")
img = cv2.resize(img,(1080,720))

points_list = []

def mousePoints(event,x,y,flags,parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,[0,0,255],cv2.FILLED)

        size = len(points_list)
        if size != 3 and size != 0:
            pts = tuple(points_list[size-1])
            cv2.line(img,pts,(x,y),[255,0,0],2)

        points_list.append([x,y])
        print(points_list)

def getAngle(points_list):
    x1,y1 = points_list[0]
    x2,y2 = points_list[1]
    x3,y3 = points_list[2]

    m1 = (y2-y1) / (x2-x1)
    m2 = (y2-y3) / (x2-x3)

    tan_alfa = abs( (m1-m2) / (1 + m1*m2) )
    radyan_angle = math.atan(tan_alfa)
    angle = round(math.degrees(radyan_angle))

    return angle

while True:
    cv2.imshow("original",img)
    cv2.setMouseCallback("original",mousePoints)

    if len(points_list) % 3 == 0 and len(points_list) != 0:
        angle = getAngle(points_list)
        points = tuple(points_list[1])
        cv2.putText(img,str(angle),points,cv2.FONT_HERSHEY_DUPLEX,1,[0,0,255])        
        points_list = []

    if cv2.waitKey(1) == ord('c'):   #clear
        points_list = []
        img = cv2.imread("angles.png")
        img = cv2.resize(img,(1080,720))
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()