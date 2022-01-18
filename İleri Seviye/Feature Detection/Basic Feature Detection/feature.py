import cv2
import numpy as np

img = cv2.imread("tuf-gaming.jpg",0)

orb = cv2.ORB_create(nfeatures=800)    #ORB_create() parametresiz de olur
#nfeatures number of features artırılabilir
keyPoints,descriptor = orb.detectAndCompute(img,None)

imgKeyPoints = cv2.drawKeypoints(img,keyPoints,None)
cv2.imshow("key points",imgKeyPoints)

cam = cv2.VideoCapture(0)

while True:
    _,imgCAM = cam.read()
    kare = cv2.cvtColor(imgCAM,cv2.COLOR_BGR2GRAY)

    keyP2,desc2 = orb.detectAndCompute(kare,None)
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(descriptor,desc2,k=2)

    #eşleşmelerin arasındaki mesafe ne kadar az ise o kadar iyi
    goodMatch = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            goodMatch.append([m])

    count = len(goodMatch)        
    imgOut = cv2.drawMatchesKnn(img,keyPoints,kare,keyP2,goodMatch,None,flags=2)
    cv2.putText(imgOut,"{} matches".format(str(count)),(20,250),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.6,[0,0,255])
    cv2.imshow("matching",imgOut)

    if count > 20:
        cv2.imwrite("Detected/20_Matches_found.jpg",imgCAM)
    
    if cv2.waitKey(25) == 27:
        break

cam.release()
cv2.destroyAllWindows()