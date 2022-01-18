import cv2
import numpy as np

cam = cv2.VideoCapture("highway.mp4")
slopes = []

while True:
    _,img = cam.read()
    img = cv2.resize(img,(1280,720))
    imgDisplay = img.copy()
    imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.blur(imgGRAY,(4,4))
    canny = cv2.Canny(imgBlurred,180,250,apertureSize=3)

    Way_corners = np.array([[(10,700),(660,490),(760,490),(1250,700)]],dtype=np.int32)
    mask = np.zeros_like(imgGRAY)   
    cv2.fillPoly(mask,Way_corners,255)    
    masked_way = cv2.bitwise_and(canny,mask)
    cv2.imshow("masked",masked_way)

    lines = cv2.HoughLinesP(masked_way,2,np.pi/180,120,minLineLength=20,maxLineGap=50)

    height,width = masked_way.shape
    empty_black = np.zeros((height,width,3),dtype=np.uint8)

    if lines is not None:
        for line in lines:  
            for x1,y1,x2,y2 in line:
                slope = (y2-y1)/(x2-x1)
                slope = float(slope) * 57.29   # to degree
                if slope > 0:
                    cv2.line(imgDisplay,(x1,y1),(x2,y2),[255,0,0],3)
                else:
                    cv2.line(imgDisplay,(x1,y1),(x2,y2),[0,0,255],3)
                slope = round(slope)
                if slope not in slopes:
                    slopes.append(slope)

    #cv2.imshow("original",img)
    cv2.imshow("hough lines",imgDisplay)
    #cv2.imshow("canny",canny)

    if cv2.waitKey(20) == 27:
        break

print(slopes)
cam.release()
cv2.destroyAllWindows()