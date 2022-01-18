import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("colored.jpg")

#Resmin RGB histogram dağılımları;
R_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
G_hist = cv2.calcHist([img],channels=[1],mask=None,histSize=[256],ranges=[0,256])
B_hist = cv2.calcHist([img],channels=[2],mask=None,histSize=[256],ranges=[0,256])

fig,axes = plt.subplots(1,2, figsize=(16,8))
fig.suptitle("HİSTOGRAMLAR")

axes[0].set_title("Eski Histogram Dağılımı")
axes[0].plot(R_hist,color="red")
axes[0].plot(G_hist,color="green")
axes[0].plot(B_hist,color="blue")

new_img = img.copy()
new_img[:,:,0] = cv2.equalizeHist(new_img[:,:,0])
new_img[:,:,1] = cv2.equalizeHist(new_img[:,:,1])
new_img[:,:,2] = cv2.equalizeHist(new_img[:,:,2])

resimler = np.hstack((img,new_img))
cv2.imshow("resimler",resimler)

R_hist = cv2.calcHist([new_img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
G_hist = cv2.calcHist([new_img],channels=[1],mask=None,histSize=[256],ranges=[0,256])
B_hist = cv2.calcHist([new_img],channels=[2],mask=None,histSize=[256],ranges=[0,256])

axes[1].set_title("Eşitlenmiş Histogram Dağılımı")
axes[1].plot(R_hist,color="red")
axes[1].plot(G_hist,color="green")
axes[1].plot(B_hist,color="blue")

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()