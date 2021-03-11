import cv2
import numpy as np
import pickle
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trsinner.yml')
labels = {"nitish":0, "kangna":1,"hello":2,"hello":3,"hello":4}
name={0:"nitish sharma",1:"Kangana"}
with open(r"C:\face_recognize\labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cascade_path = r"C:\Users\Nitish sharma\Downloads\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
while True:
    #read video
    check , frame = video.read()
    frame = cv2.resize(frame, (1266, 620))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    #draw rectangle
    for (x, y, w, h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        id_, conf = recognizer.predict(gray)
        print(conf)
        print(name[id_])
        if conf >=35 and conf<=95:
            print(id_)
            print(name[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = name[id_]
            color = (255,0,250)
            strok = 2
            cv2.putText(frame, name, (x,y), font, 1, color, strok, cv2.LINE_AA)
            cv2.putText(frame, str(conf)+name, (x, y), font, 1, color, strok, cv2.LINE_AA)
        img_item = "capture_face1.png"
        cv2.imwrite(img_item, gray)
        color = (255,0,1)
        width = x+w
        height = y+h
        cv2.rectangle(frame,(x, y) , (width, height), color, 5 )

    cv2.imshow("video",frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


print("complete")