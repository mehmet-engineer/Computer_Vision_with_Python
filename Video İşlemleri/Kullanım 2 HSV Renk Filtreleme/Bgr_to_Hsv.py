import cv2
import numpy as np

blue = int(input("Mavi değeri girin: "))
green = int(input("Yeşil değeri girin: "))
red = int(input("Kırmızı değeri girin: "))

renk = np.uint8([[[blue,green,red]]])
hsv = cv2.cvtColor(renk,cv2.COLOR_BGR2HSV)

print()
print("HSV: ", hsv)