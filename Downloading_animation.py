# downloading animation image

import cv2
import numpy as np
from random import randint
while(True):
    image = cv2.imread(r"C:\face_recognize\Green screen.jpg")
    image2 = image
    cv2.rectangle(image,(49,99),(500,151),(0,0,255),4)
    cv2.putText(image,"hello",(250,90), cv2.FONT_ITALIC,1,(100,2,255),1)
    a = 0
    for i in range (450):
        image[100:150, 50+a:50+i] = [255,26,255]
        a = i
        cv2.imshow("image", image)
        if i != 448:
            cv2.waitKey(51-(int(50*(i/450))+1))
            #print(51-(int(50*(i/450))+1))
        else:
            cv2.waitKey(10)

cv2.destroyAllWindows()
