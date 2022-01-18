import cv2
import numpy as np

img = cv2.imread("circles.jpg")
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.blur(imgGRAY,(3,3))
imgCanny = cv2.Canny(imgBlurred,60,60)

#imgBlurred ya da Canny üzerinde denenebilir
circles = cv2.HoughCircles(imgBlurred, cv2.HOUGH_GRADIENT, 1, 20,
                            minRadius=2, maxRadius=130,
                            param1=50, param2=30)

circles = np.uint16(np.around(circles))   #integer'a çevir

for circle in circles:
    for x,y,r in circle:
        cv2.circle(img, (x,y), r, [0,0,255], 2)
        cv2.circle(img, (x,y), 2, [0,0,0], 2)

cv2.imshow("img",img)

cv2.waitKey()
cv2.destroyAllWindows()