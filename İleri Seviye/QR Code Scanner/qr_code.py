import cv2
import numpy as np
from pyzbar import pyzbar
#pip install pyzbar

img = cv2.imread("qrcode.png")
code = pyzbar.decode(img)

for barcode in code:
    myData = barcode.data.decode("utf-8")
    print(myData)

cv2.waitKey()
cv2.destroyAllWindows()