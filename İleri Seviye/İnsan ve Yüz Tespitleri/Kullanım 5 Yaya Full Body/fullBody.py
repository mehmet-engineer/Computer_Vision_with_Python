import cv2

Body = cv2.CascadeClassifier("haarcascade_fullbody.xml")
resim = cv2.imread("street.jpg")
resimGRAY = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

body_locs = Body.detectMultiScale(resimGRAY,1.1,5)
for (x,y,w,h) in body_locs:
    cv2.rectangle(resim,(x,y),(x+w,y+h),[255,0,0],2)

cv2.imshow("Beden",resim)
cv2.waitKey()
cv2.destroyAllWindows()