import cv2
import numpy as np 

kamera = cv2.VideoCapture(0)

cam_width = kamera.get(3)   #640
cam_boy = kamera.get(4)     #480
cam_fps = kamera.get(5)     #30 FPS

#video formatını ayarlama --> *"MJPG" = mp4, *"DIVX" = avi, *"X264" = mkv
format = cv2.VideoWriter_fourcc(*"DIVX")
kayıt = cv2.VideoWriter("my_video.avi",format, 15, (640,480) )

while True:
    red,kare = kamera.read()    
    cv2.imshow("Kamera",kare)

    kayıt.write(kare)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

kayıt.release()
kamera.release()
cv2.destroyAllWindows()