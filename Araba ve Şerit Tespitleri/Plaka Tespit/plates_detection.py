import cv2

img = cv2.imread("number plates.jpg")
imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plateIMG = img

cascade1 = "haarcascade_licence_plate_rus_16stages.xml"
cascade2 = "haarcascade_russian_plate_number.xml"

nPlateCascade = cv2.CascadeClassifier(cascade1)
numberPlates = nPlateCascade.detectMultiScale(imgGRAY,1.1,4)
for (x,y,w,h) in numberPlates:
    area = w*h
    if area>200:
        cv2.rectangle(img,(x,y),(x+w,y+h),[255,0,0],2)
        plateIMG = img[y:y+h,x:x+w]

cv2.imshow("Plaka",img)

if cv2.waitKey() == ord("s"):
    cv2.imwrite("plate.jpg",plateIMG)

cv2.destroyAllWindows()