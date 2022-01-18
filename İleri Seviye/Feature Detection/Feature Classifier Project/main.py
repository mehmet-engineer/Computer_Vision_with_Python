import cv2
import numpy as np
import os

images = []
path = os.getcwd() + "\\Objects"
objects = os.listdir(path)
print(len(objects),"resim algılandı")

orb = cv2.ORB_create()

for obj in objects:
    img = cv2.imread("Objects\\{}".format(obj),0)
    images.append(img)
    
def find_Descriptor(images):
    descList = []
    for img in images:
        keyP,desc = orb.detectAndCompute(img,None)
        descList.append(desc)
    return descList

descList = find_Descriptor(images)

def find_objID(img,descList,threshold):
    keyP_cam,desc_cam = orb.detectAndCompute(img,None)
    matcher = cv2.BFMatcher()
    matchList = []
    for desc in descList:
        matches = matcher.knnMatch(desc,desc_cam, k=2)
        goodMatch = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                goodMatch.append([m])
        matchList.append(len(goodMatch))
    if max(matchList) > threshold:
        id = matchList.index(max(matchList))
        return id
    else:
        return -1

cam = cv2.VideoCapture(0)

while True:
    _,kare = cam.read()
    kareGRAY = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    id = find_objID(kareGRAY,descList,threshold=10)

    if id == -1:
        cv2.putText(kare,"no matches found",(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,[0,0,255])
    else:
        cv2.putText(kare,"{}".format(objects[id]),(50,50),cv2.FONT_HERSHEY_COMPLEX,0.8,[255,0,0])

    cv2.imshow("matching",kare)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()




