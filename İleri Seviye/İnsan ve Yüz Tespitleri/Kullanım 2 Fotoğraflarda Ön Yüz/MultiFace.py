import cv2
import numpy as np

frontalFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
resim1 = cv2.imread("crowded.jpg")
resim2 = cv2.imread("family.jpg")
resim1GRAY = cv2.cvtColor(resim1,cv2.COLOR_BGR2GRAY)
resim2GRAY = cv2.cvtColor(resim2,cv2.COLOR_BGR2GRAY)

face_locs = frontalFace.detectMultiScale(resim1GRAY,1.1,3)
for (x,y,w,h) in face_locs:
    cv2.rectangle(resim1,(x,y),(x+w,y+h),[255,0,0],2)

face_locs = frontalFace.detectMultiScale(resim2GRAY,1.3,3)
for (x,y,w,h) in face_locs:
    cv2.rectangle(resim2,(x,y),(x+w,y+h),[255,0,0],2)

cv2.imshow("Kalabalik",resim1)
cv2.imshow("Family",resim2)
cv2.waitKey()
cv2.destroyAllWindows()