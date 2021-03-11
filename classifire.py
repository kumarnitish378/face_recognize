import  numpy  as  np
import cv2
import turtle
from random import randint
image = cv2.imread(r"C:\face_recognize\my photo.jpg")
harcascade = r"C:\face_recognize\data\haarcascade_frontalface_default.xml"
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(harcascade)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
recognizer = cv2.face.LBPHFaceRecognizer_create()

for (x,y,w,h) in face:
    cv2.rectangle(gray, (x, y), (x+h, y+w), (200, 20, 10), 3)
    gray = gray[x-100:x + h-80, y+100:y + w+150]
    # gray = gray[x + h:x, y + w:y]
    print(x, y, w, h)

data = []
for i in gray:
    # print(list(i))
    print(list(i), file=open("test.txt", 'w'))
cv2.imshow("hello", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
