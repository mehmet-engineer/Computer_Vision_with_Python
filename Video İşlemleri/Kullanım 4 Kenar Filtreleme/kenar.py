import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    red,kare = kamera.read()

    laplacian = cv2.Laplacian(kare,cv2.CV_64F)
    #cv2.imshow("Filtre1 Laplacian",laplacian)

    sobel_dikey = cv2.Sobel(kare,cv2.CV_64F,1,0, ksize=5)
    sobel_yatay = cv2.Sobel(kare,cv2.CV_64F,0,1, ksize=5)
    #cv2.imshow("Filtre2.1 Sobel Dikey",sobel_dikey)
    #cv2.imshow("Filtre2.2 Sobel Yatay",sobel_yatay)

    #basit canny metodu;
    #ayrıntılar çıkmasın sadece kenerlar belli olsun diye azcık blurladık
    blur = cv2.GaussianBlur(kare,(1,1),0)
    canny = cv2.Canny(blur,80,200)
    #alt eşik değeri --> 100
    #üst eşik değeri --> 200

    #daha belirgin kenarlar için canny;
    imgGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    imgGRAY_blur = cv2.GaussianBlur(imgGRAY,(7,7),1)
    imgCanny = cv2.Canny(imgGRAY_blur,90,200)
    kernel = np.ones((5,5))     #ayarlanabilir
    img1 = cv2.dilate(imgCanny,kernel, iterations=2)     #diolation -> kenarları kalınlaştırır
    out = cv2.erode(img1,kernel, iterations=1)         #en sağlıklı sonuç out (önce 2x dilate sonra 1x erode)

    cv2.imshow("Belirgin canny",out)
    cv2.imshow("Filtre3 Canny",canny)

    key = cv2.waitKey(25)
    if key == 27:
        break

kamera.release()
cv2.destroyAllWindows()