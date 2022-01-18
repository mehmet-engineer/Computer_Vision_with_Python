import cv2

img1 = cv2.imread("sag.png")
img2 = cv2.imread("sol.png")

print(img1.shape)
print(img2.shape)

images = [img1,img2]

stitcher = cv2.Stitcher.create()
status,result = stitcher.stitch(images)

print(status)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()