import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("foto_perspective.png")

#öncelikle nesnenin 4 köşe pixel koordinatları lazım
#bunu belirlemek için matplotlib imlecinden yararlanabiliriz;
"""fig,ax = plt.subplots()
image = ax.imshow(img)
plt.show()"""

#nesneye göre tahmini çıktı boyutunu ayarla
width = 520
height = 600

#points (x,y) köşeler: [sol üst, sağ üst, sol alt, sağ alt]    
points1 = np.float32([ [306,211],[626,137],[316,534],[649,470] ])
points2 = np.float32([ [0,0],[width,0],[0,height],[width,height] ])

matrix = cv2.getPerspectiveTransform(points1,points2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("original",img)
cv2.imshow("Perspektiften Duz Foto",imgOutput)

cv2.waitKey()
cv2.destroyAllWindows()