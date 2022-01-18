import cv2
import numpy as np

frontalFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
resim = cv2.imread("my_face.jpg")
resimGRAY = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

face_locs = frontalFace.detectMultiScale(resimGRAY,1.3,2)
for (x,y,w,h) in face_locs:
    cv2.rectangle(resim,(x,y),(x+w,y+h),[255,0,0],2)

cv2.imshow("MY FACE",resim)
cv2.waitKey()
cv2.destroyAllWindows()