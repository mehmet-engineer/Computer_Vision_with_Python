import cv2

back = cv2.createBackgroundSubtractorMOG2()
cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    back_mask = back.apply(frame)
    result = cv2.bitwise_and(frame,frame,mask=back_mask)

    cv2.imshow("mog2",back_mask)
    cv2.imshow("original",result)

    if cv2.waitKey(25) == 27:
        break

cam.release()
cv2.destroyAllWindows()