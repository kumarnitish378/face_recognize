import cv2
import os
import numpy as np
#import faceRecognition as fr

#This module contains all common functions that are called in tester.py file


#Given an image below function returns rectangle for face detected alongwith gray scale image
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale
    face_haar_cascade=cv2.CascadeClassifier(r'C:\face_recognize\data\haarcascade_frontalface_default.xml')#Load haar classifier
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.30,minNeighbors=5)#detectMultiScale returns rectangles
    return faces,gray_img

#Given a directory below function returns part of gray_img which is face alongwith its label/ID
def labels_for_training_data(directory):
    faces=[]
    faceID=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")#Skipping files that startwith .
                continue

            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path)#loading each image one by one
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image
            if len(faces_rect)!=1:
               continue #Since we are assuming only single person images are being fed to classifier
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from grayscale image
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID


#Below function trains haar classifier and takes faces,faceID returned by previous function as its arguments
def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer

#Below function draws bounding boxes around detected face in image
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=3)

#Below function writes name of person for detected label
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),4)


def camera_photo():
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    check, frame = video.read()
    print(check)
    #print(frame)
    cv2.imshow("camera", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    frame =cv2.resize(frame,(500,500))
    return frame


#This module takes images  stored in diskand performs face recognition
#test_img=cv2.imread(r'F:\FaceRecognition-master\TestImages\team_kangana_ranaut_50967958_414722855965531_8510623847343776491_n.jpg')#test_img path
#test_img = cv2.imread(r'C:\Users\Nitish sharma\Desktop\image\traning_photo\0\my photo.jpg')
#test_img = cv2.imread(r'C:\Users\Nitish sharma\Desktop\image\traning_photo\0\WIN_20200119_15_12_41_Pro.jpg')
test_img = camera_photo()
faces_detected,gray_img=faceDetection(test_img)


print("faces_detected:",faces_detected)


#Comment belows lines when running this program second time.Since it saves training.yml file in directory
#faces,faceID=fr.labels_for_training_data('trainingImages')   "changed"
#faces,faceID = labels_for_training_data(r'C:\Users\Nitish sharma\Desktop\image\traning_photo')
#face_recognizer=train_classifier(faces,faceID)
#face_recognizer.write('trainingData.yml')
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r"F:\FaceRecognition-master\trainingData.yml")


#Uncomment below line for subsequent runs
# face_recognizer=cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs

name={0:"nitish sharma",1:"Kangana"}#creating dictionary containing names for each label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    print("confidence:",confidence)
    print("label:",label)
    draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>90):#If confidence more than 37 then don't print predicted face text on screen
        continue
    put_text(test_img,predicted_name,x,y)

resized_img=cv2.resize(test_img,(1366,768))
cv2.imshow("face dtecetion tutorial",resized_img)
cv2.imshow("face dtecetion tutorial",test_img)
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows

