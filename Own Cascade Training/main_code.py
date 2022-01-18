import cv2

car_cascade = cv2.CascadeClassifier("cascade.xml")
kamera = cv2.VideoCapture("video.mp4")

while True:
    _,kare = kamera.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    scale = 1.2
    neighbor = 6
    locs = car_cascade.detectMultiScale(kareGRAY,scale,neighbor)

    for (x,y,w,h) in locs:
        area = w*h
        if area > 15000:
            cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)
            cv2.putText(kare,"my car",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,[0,255,0],2)
    
    cv2.imshow("Kamera",kare)

    key = cv2.waitKey(1)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()