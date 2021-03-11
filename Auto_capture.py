import cv2
import time
t1 = time.time()
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    t2 = time.time()
    t = t2 - t1
    check, frame = video.read()
    cv2.imshow("edit", frame)
    if cv2.waitKey(20) & 0xff == ord('q') or t >= 5:
        time.sleep(0.5)
        cv2.imwrite("hello.jpg", frame)
        break

video.release()
cv2.destroyAllWindows()
cv2.imshow("capture",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
