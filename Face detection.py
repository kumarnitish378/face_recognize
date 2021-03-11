import cv2
import time
t1 = time.time()
import numpy as np
import matplotlib.pyplot as plt
#video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
path1 = r"C:\face_recognize\traning_photo\0\priyanka-chopra-full-hd-image.jpg"
frame = cv2.imread(path1)
cascade_path = r"C:\face_recognize\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)
red = []
green = []
blue = []
print(frame)
for (x, y, w, h) in faces:
    #frame = cv2.rectangle(frame, (x, y), (x + w, (y + h)), (220, 25, 220), 2)
    roi = frame[y:y + h, x:x + w]
roi2 = roi+60
for i in roi2:
    for j in i:
        red.append(j[0])
        green.append(j[1])
        blue.append(j[2])
cv2.imshow("image",roi)
#cv2.imshow("image1",roi2)
cv2.waitKey(0)
cv2.destroyAllWindows()
red_avg = 0
green_avg = 0
blue_avg = 0
for i in range(len(red)):
    red_avg = red_avg+red[i]
    green_avg = green_avg+green[i]
    blue_avg = blue_avg + blue[i]
print(red_avg/10000)
print(green_avg/10000)
print(blue_avg/10000)
color = [red_avg,green_avg,blue_avg]
plt.plot(color)
plt.show()
