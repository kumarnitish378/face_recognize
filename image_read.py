import cv2
import numpy as np
path = r"C:\face_recognize\my photo.jpg"
#image = cv2.imread(path)
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
check, frame = video.read()
cascade_path = r"C:\Users\Nitish sharma\Downloads\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
for (x ,y ,w, h) in face:
    print(x,y,w,h)
    roi_gray = gray[y:y+h, x:x+w]
    img_item = "capture_face2.png"
    cv2.imwrite(img_item, roi_gray)
print("complete")