import cv2
import numpy as np
from pyzbar import pyzbar

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    code = pyzbar.decode(img)

    myData = ""

    for barcode in code:
        myData = barcode.data.decode("utf-8")
        print(myData)
        points = np.array([barcode.polygon],np.int32)
        points = points.reshape((-1,1,2))
        cv2.polylines(img,[points],True,[0,0,255],3)
        points2 = barcode.rect
        cv2.putText(img,"recognized",(points2[0],points2[1]),cv2.FONT_HERSHEY_COMPLEX,1,[0,255,0])

    cv2.putText(img,myData,(20,20),cv2.FONT_HERSHEY_PLAIN,1.5,[255,0,0])

    cv2.imshow("kamera",img)
    if cv2.waitKey(20) == 27:
        break

cam.release()
cv2.destroyAllWindows()