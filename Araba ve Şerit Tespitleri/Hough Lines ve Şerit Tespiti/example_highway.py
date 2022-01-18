import cv2
import numpy as np

img = cv2.imread("car_cam.jpg")
img = cv2.resize(img,(1280,720))
imgDisplay = img.copy()
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.blur(imgGRAY,(3,3))
canny = cv2.Canny(imgBlurred,200,250,apertureSize=3)

Way_corners = np.array([[(10,700),(400,410),(900,410),(1350,700)]],dtype=np.int32)
mask = np.zeros_like(imgGRAY)   #resmi tamamen 0'lara benzetir siyah yapar
cv2.fillPoly(mask,Way_corners,255)    #maskenin içindeki köşeleri verilen alanı 255 yap
masked_way = cv2.bitwise_and(canny,mask)
cv2.imshow("masked",masked_way)

#houghLinesP
lines = cv2.HoughLinesP(masked_way,2,np.pi/180,120,minLineLength=20,maxLineGap=50)

height,width = masked_way.shape
empty_black = np.zeros((height,width,3),dtype=np.uint8)

if lines is not None:
    for line in lines:  
        for x1,y1,x2,y2 in line:
            cv2.line(imgDisplay,(x1,y1),(x2,y2),[255,0,0],5)

#cv2.imshow("original",img)
cv2.imshow("hough lines",imgDisplay)
#cv2.imshow("canny",canny)

cv2.waitKey()
cv2.destroyAllWindows()