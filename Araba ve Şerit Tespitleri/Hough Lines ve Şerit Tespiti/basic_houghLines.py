import cv2, math
import numpy as np

img = cv2.imread("lines.png")
imgDisplay = img.copy()
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(imgGRAY,150,200,apertureSize=3)

#HoughLines(img, Ro veya L uzunluğu, radyan cinsinden açı, minimum oy eşiği)
lines = cv2.HoughLines(canny,1,np.pi/180,110)   #np.pi = 3.14
print(len(lines),"tane line algılandı")

#lines = [[a.   b]...]    a -> (0,0)'dan ro uzaklığı  |  b -> line radyan açısı

if lines is not None:
    for i in lines:  
        ro = i[0][0]
        teta = i[0][1]
        
        # 1 radyan = 57.29 derece
        # if math.degrees(int(teta)) > eşik:  yapılabilir...
        
        x0 = ro * np.cos(teta)
        y0 = ro * np.sin(teta)

        a = np.cos(teta)
        b = np.sin(teta)

        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*a)
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*a)

        cv2.line(img,(x1,y1),(x2,y2),[255,0,0],2)


cv2.imshow("original",img)
cv2.imshow("hough lines",imgDisplay)
cv2.imshow("canny",canny)

cv2.waitKey()
cv2.destroyAllWindows()