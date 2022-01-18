import cv2
import numpy as np 

img = cv2.imread("resim.jpg")
resim = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread("parca.jpg")
parca = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
w,h = parca.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED']

output = cv2.matchTemplate(resim,parca,cv2.TM_CCOEFF)
min_val, max_val, min_location, max_location = cv2.minMaxLoc(output)

top_left = max_location
bottom_right = (top_left[0] + h, top_left[1] + w)
cv2.rectangle(img,top_left,bottom_right,[0,0,255],2)

cv2.imshow("img",img)
cv2.imshow("template",template)

cv2.waitKey()
cv2.destroyAllWindows()