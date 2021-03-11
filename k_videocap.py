import cv2,numpy,time
import cv2
import os
import numpy as np
import k_face_recog as fr

#faces,faceID=fr.labels_for_training_data("C:\\Users\\Acer\\Documents\\train")
#face_recognizer=fr.train_classifier(faces,faceID)
#face_recognizer.save("training_data.yml")
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\face_recognize\training_data.yml')
name={0:"Nitish",1:"Kat"}

video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):
    ret,imgd=video.read()
    faces_detected, gray_img = fr.faceDetection(imgd)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(imgd,(x, y),(x+w,y+h),(255,0,0),thickness=7)

    resized_img=cv2.resize(imgd,(700,700))
    # cv2.imshow("Door lock",resized_img)
    # cv2.waitKey(10)
    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray=gray_img[y:y+h,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        # print("confidence:",confidence)
        # print("label:",label)
        fr.draw_rect(imgd,face)
        predicted_name=name[label]
        if(confidence<90):
            fr.put_text(imgd,predicted_name,x,y)

    resized_img=cv2.resize(imgd,(700,700))
    cv2.imshow("Door lock",resized_img)

    if cv2.waitKey(10)==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

#video=cv2.VideoCapture(0)
#check,frame=video.read()
#print(check)
#cv2.imshow("imgcap",frame)
#print(frame)
#time.sleep(3)
#cv2.waitKey(0)
#video.release()
