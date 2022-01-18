import cv2
import matplotlib.pyplot as plt

img = cv2.imread("foto_perspective.png")

plt.imshow(img)
plt.show()

"""fig,ax = plt.subplots(1,2)
ax[0].imshow(img)
ax[1].imshow(img)
plt.show()"""