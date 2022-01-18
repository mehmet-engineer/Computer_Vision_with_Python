import cv2

video = cv2.VideoCapture("Cars2.mp4")
cars = cv2.CascadeClassifier("cars.xml")

while True:
    _,kare = video.read()
    kare = cv2.resize(kare,(850,500))
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    
    car_locs = cars.detectMultiScale(kareGRAY,1.1,6)

    for (x,y,w,h) in car_locs:
        cv2.rectangle(kare,(x,y),(x+w,y+h),[255,0,0],2)

    cv2.imshow("video",kare)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()