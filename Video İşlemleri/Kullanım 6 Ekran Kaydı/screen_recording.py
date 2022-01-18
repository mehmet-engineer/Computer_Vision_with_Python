import cv2
import pyautogui
import numpy as np

codec = cv2.VideoWriter_fourcc(*"MJPG")
#video formatı --> *"MJPG" = mp4, *"DIVX" = avi, *"X264" = mkv
resolution = (1920,1080)

record = cv2.VideoWriter("screen_recorded.avi",codec, 10, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)  #boş bir pencere oluştur
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    record.write(frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

record.release()
cv2.destroyAllWindows()