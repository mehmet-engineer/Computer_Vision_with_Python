import cv2

img = cv2.imread("noise.jpg")
cv2.imshow("original",img)

#ortalama bulanıklaştırma;
Mean_Blurred = cv2.blur(img,ksize=(4,4))

#medyan bulanıklaştırma;
Median_Blurred = cv2.medianBlur(img,ksize=5)

#Gauss gürültüsü için blur;
Gauss_Blurred = cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)

cv2.imshow("Mean_Blurred",Mean_Blurred)
cv2.imshow("Median_Blurred",Median_Blurred)
cv2.imshow("Gauss_Blurred",Gauss_Blurred)

cv2.waitKey()
cv2.destroyAllWindows()