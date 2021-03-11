import cv2
import os
import numpy as np
import face_recog as fr

test_img=cv2.imread(r"F:\FaceRecognition-master\TestImages\ddownload.jpg")
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

faces,faceID=fr.labels_for_training_data(r"F:\FaceRecognition-master\trainingImages")
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.save("training_data.yml")
name={1:"Teena",2:"Kat"}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>37):
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(1000,700))
cv2.imshow("this",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
