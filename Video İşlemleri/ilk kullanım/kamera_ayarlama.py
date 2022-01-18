import cv2

cam = cv2.VideoCapture(0)

cam_brightness = cam.get(10)
new_brightness = cam.set(10, 150)

"""
#       key value
cam.set(3 , 640  ) # width        
cam.set(4 , 480  ) # height       
cam.set(10, 120  ) # brightness     min: 0   , max: 255 , increment:1  
cam.set(11, 50   ) # contrast       min: 0   , max: 255 , increment:1     
cam.set(12, 70   ) # saturation     min: 0   , max: 255 , increment:1
cam.set(13, 13   ) # hue         
cam.set(14, 50   ) # gain           min: 0   , max: 127 , increment:1
cam.set(15, -3   ) # exposure       min: -7  , max: -1  , increment:1
cam.set(17, 5000 ) # white_balance  min: 4000, max: 7000, increment:1
cam.set(28, 0    ) # focus          min: 0   , max: 255 , increment:5
"""