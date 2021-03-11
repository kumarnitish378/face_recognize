import cv2
import os
import time
import math
import matplotlib.pyplot as plt
import numpy as np
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cascade_path = r"C:\Users\Nitish sharma\Downloads\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
color = (255,0,250)
strok = 2
font = cv2.FONT_HERSHEY_SIMPLEX
red = 0
count = 0
def Video():
    pass
    video = []
    for file in os.listdir(r"C:\Users\Nitish sharma\Videos"):
        if ".mp4" in file:
            video.append(r"C:\Users\Nitish sharma\Videos"+"\\"+file)
    return video
pos = 5
while True:
    check, frame = video.read()
    frame = cv2.resize(frame, (1000, 620))
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,(y+h)),(220, 25, 220), 2)
        # roi = frame[y:y + h, x:x + w] #region of face or only face
        # frame[y:y + h + 20, x:x + w + 20] = frame[y:y + h + 20, x:x + w + 20] + [10,15,50]
        # frame[y+h+20:620,0:1000] = [100,10,52]
        a = Video()
        if count == 0:
            x_axis = x
            count = count+1
            Max = len(a)
        if x_axis-x > 100:
            print("motion found")
            os.startfile(a[pos])
            print(a[pos])
            time.sleep(5)
            pos = pos+1
            if pos == Max:
                pos = Max
        elif x-x_axis > 100:
            os.startfile(a[pos])
            print(a[pos])
            pos = pos -1
            time.sleep(5)
            if pos == 0:
                pos = 0
        #print(h,w)
        # cv2.putText(frame,"Nitish", (x, y), font, 1, color, strok, cv2.LINE_AA)
        # x_axis = x+114
        # y_axis = y+114
        # print(h,w,"==",x_axis,y_axis)
        # frame2 = cv2.circle(frame, (x_axis,y_axis), 145, (255, 0, 0), 3)

    #cv2.imshow("video", roi)
    cv2.imshow("edit", frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
video.release()
cv2.destroyAllWindows()



