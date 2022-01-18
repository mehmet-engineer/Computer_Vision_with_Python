import cv2

img = cv2.imread("street.jpg")

descriptor = cv2.HOGDescriptor()
descriptor.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
rects,weights = descriptor.detectMultiScale(img,padding=(7,7),scale=1.2)

for x,y,w,h in rects:
    cv2.rectangle(img,(x,y),(x+w,y+h),[0,0,255],2)

cv2.imshow("image",img)

cv2.waitKey()
cv2.destroyAllWindows()