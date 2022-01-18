import cv2
import numpy as np

resim = np.ones((500,600,3))

string = "Mehmet"
loc = (150,200)    #sol alt köşesinin konumu
scale = 2
color = [0,0,0]
cv2.putText(resim,string,loc,cv2.FONT_ITALIC,scale,color)

cv2.imshow("resim",resim)
cv2.waitKey()
cv2.destroyAllWindows()