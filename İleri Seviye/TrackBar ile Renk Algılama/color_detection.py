import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",0,179,empty)
cv2.createTrackbar("Sat min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat max","TrackBars",0,255,empty)
cv2.createTrackbar("Val min","TrackBars",0,255,empty)
cv2.createTrackbar("Val max","TrackBars",0,255,empty)

img = cv2.imread("rose.png")  
img = cv2.resize(img,(400,550))
cv2.imshow("original",img)

while True:
    
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    hueMin = cv2.getTrackbarPos("Hue min","TrackBars")
    hueMax = cv2.getTrackbarPos("Hue max","TrackBars")
    satMin = cv2.getTrackbarPos("Sat min","TrackBars")
    satMax = cv2.getTrackbarPos("Sat max","TrackBars")
    valMin = cv2.getTrackbarPos("Val min","TrackBars")
    valMax = cv2.getTrackbarPos("Val max","TrackBars")

    lower = np.array([hueMin,satMin,valMin])   
    upper = np.array([hueMax,satMax,valMax])
    maske = cv2.inRange(imgHSV,lower,upper)

    result = cv2.bitwise_and(img,img, mask=maske)
    cv2.imshow("Result",result)

    cv2.imshow("hsv",imgHSV)
    cv2.imshow("Maske",maske)
    
    if cv2.waitKey(5) == 27:
        break

cv2.destroyAllWindows()