import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam_width = cam.get(3)   #640
cam_height = cam.get(4)   #480

#Kameradan üst üste 2 kez hızlıca ilk referansını al
_, frame1 = cam.read()
_, frame2 = cam.read()

while cam.isOpened():
    diff = cv2.absdiff(frame1,frame2)   #bu referanslardan farkları beyaz pixel yap
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Movement was detected", (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)

    image = cv2.resize(frame1, (1280,720))
    cv2.imshow("Result", frame1)

    #referansları değiştir ve döngü oluştur
    frame1 = frame2
    ret, frame2 = cam.read()

    if cv2.waitKey(25) == 27:
        break

cam.release()
cv2.destroyAllWindows()