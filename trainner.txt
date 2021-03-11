import cv2
from PIL import Image
import numpy as np
import os
import pickle
path1 = r"C:\face_recognize\traning_photo"

cascade_path = r"C:\Users\Nitish sharma\Downloads\haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
recognizer = cv2.face.LBPHFaceRecognizer_create()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, path1)
y_labels = []
x_train = []
current_id = 0
label_id = {}
for root, dir , files in os.walk(image_dir):
    for file in files:
        if file.endswith("png")or file.endswith("PNG") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            #print(label, path)
            if not label in label_id:
                label_id[label] = current_id
                current_id +=1
            id_ = label_id[label]
            #print(label_id)
            # y_labels.append(label)
            # x_train.append(path)
            pil_image = Image.open(path).convert("L") #gray scale
            size = (550,550)
            pil_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(pil_image,"uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for (x, y ,w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append((id_))

# print(y_labels)
# print(x_train)
with open("labels.pickle","wb") as f:
    pickle.dump(label_id, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")