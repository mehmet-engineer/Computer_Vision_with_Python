import cv2

video = cv2.VideoCapture("people_walking.mp4")
Bodies = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    _,kare = video.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    body_locs = Bodies.detectMultiScale(kareGRAY,1.1,4)

    for (x,y,w,h) in body_locs:
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)

    cv2.imshow("video",kare)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()