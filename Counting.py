import os
from time import sleep
from random import randint
import numpy as np
import cv2
import matplotlib.pyplot as plt
#show image
def show_img(img):
    cv2.imshow("blue", img)
    cv2.moveWindow("blue", 700, 150)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()

#color
def color():
    blue = randint(0,255)
    green = randint(0,255)
    red = randint(0,255)
    color = [blue+10,green+10,red+10]
    return color
img = cv2.imread(r"C:\face_recognize\Blue_screen.jpg")
img = cv2.resize(img, (600,400))
x = 0
y = 0

#function for color illution

# while True:
#     for i in range(3):
#         for j in range (4):
#             img[x:x+100,y:y+200] = color()
#             x = x + 100
#             show_img(img)
#         y = y + 200
#         x = 0
#     show_img(img)
#     x = 0
#     y = 0
#     if cv2.waitKey(20) & 0xff == ord('q'):
#         break

#scan each pixel value
#---------------------------------pixel scan-----------------------------
img[0:400,0:600] = [100,0,155]
img = cv2.rectangle(img,(70,50),(200,100),(10,255,20),2)
lst = []
ylst = []
for x in range(400):
    for y in range(600):
        if img[x,y].sum() >= 256:
            lst.append(x)
            ylst.append(y)
        elif x == y :
            img[x:x+5,y:y+5] = [255,0,0]
lst.sort()
print(ylst[0],lst[0])
print(ylst[-1],lst[-1])
print("complete")
show_img(img)
cv2.waitKey(0)
cv2.destroyAllWindows()






