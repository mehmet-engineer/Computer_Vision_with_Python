import cv2

def optical_size(image,size_type,ratio):
    h,w,_ = image.shape
    if size_type == "büyüt":
        yükseklik = int(h + h * ratio / 100)
        genişlik = int(w + w * ratio / 100)
    elif size_type == "küçült":
        yükseklik = int(h - h * ratio / 100)
        genişlik = int(w - w * ratio / 100)
    else:
        yükseklik = h
        genişlik = w
    size = (genişlik,yükseklik)
    result = cv2.resize(image,size)
    return result

img = cv2.imread("sau.png")
manuel = cv2.resize(img,(400,500))
autoSized = optical_size(img,"küçült",25)

cv2.imshow("original",img)
cv2.imshow("Manuel",manuel)
cv2.imshow("AutoSized",autoSized)
cv2.waitKey()
cv2.destroyAllWindows()

