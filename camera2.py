import cv2
import time
t1 = time.time()
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
a=0
b=20
path1 = r"C:\face_recognize\traning_photo"
cascade_path = r"C:\face_recognize\data\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
while True:
    t2 = time.time()
    t = t2 - t1
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, (y + h)), (220, 25, 220), 2)
        roi = frame[y:y + h, x:x + w] #region of face or only face
    cv2.imshow("edit",frame)
    if cv2.waitKey(20) & 0xff == ord('q') or t >= 30:
        time.sleep(0.5)
        break
    a = a + 1
    b = b+4
video.release()
cv2.destroyAllWindows()
