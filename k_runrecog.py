import cv2
import os
import numpy as np
import k_face_recog as fr

test_img=cv2.imread(r"C:\face_recognize\traning_photo\0\priyanka-chopra-hd-picture.jpg")
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

# faces,faceID=fr.labels_for_training_data("C:\\face_recognize\\traning_photo")
# face_recognizer=fr.train_classifier(faces,faceID)
# face_recognizer.save("training_data.yml")
face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\face_recognize\training_data.yml')
name={0:"nitish",1:"Kat"}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence<45):
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(700,700))
cv2.imshow("this",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
