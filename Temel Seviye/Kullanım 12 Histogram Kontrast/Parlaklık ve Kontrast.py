import cv2
import numpy as np

cam = cv2.VideoCapture(1)
cam.set(3,1280)        
cam.set(4,720)

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Contrast","TrackBars",0,3,empty)
cv2.createTrackbar("Brightness","TrackBars",0,99,empty)


while True:
    red,img = cam.read()

    alpha = cv2.getTrackbarPos("Contrast","TrackBars")
    beta = cv2.getTrackbarPos("Brightness","TrackBars")

    # alpha contrast control (1.0-3.0)
    # beta brightness control (0-100)

    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    cv2.imshow("Kamera",img)

    key = cv2.waitKey(25)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()