import cv2

frontalFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes = cv2.CascadeClassifier("haarcascade_eye.xml")
kamera = cv2.VideoCapture(0)

while True:
    _,kare = kamera.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    face_locs = frontalFace.detectMultiScale(kareGRAY,1.3,4)
    eye_locs = eyes.detectMultiScale(kareGRAY,1.5,4)

    for (x,y,w,h) in face_locs:
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)

    for (a,b,c,d) in eye_locs:
        cv2.rectangle(kare,(a,b),(a+c,b+d),[0,0,255],1)

    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(30)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()