import cv2

smileFace = cv2.CascadeClassifier("haarcascade_smile.xml")
kamera = cv2.VideoCapture(0)

while True:
    _,kare = kamera.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    face_locs = smileFace.detectMultiScale(kareGRAY,1.9,9)

    for (x,y,w,h) in face_locs:
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)

    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(30)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()