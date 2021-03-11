import cv2
from random import randint
import numpy as np
import time
import matplotlib.pyplot as plt

data = cv2.imread(r"C:\face_recognize\test_image.png")
print(np.shape(data))
print(len(data))
data2 = data
# change color
Pass = input("please enter password ")
if Pass != "nitish":
    for i in range(len(data)):
        for j in range (len(data[0])):
            if i%2 == 0 and j%2 == 0:
                data[i][j] = np.array([255,225,225])
            else:
                data[i][j] = np.array([randint(0,255), randint(0,255), randint(0,255)])
                # data[i][j] = np.array([0,0,0])

    for i in range(len(data)):
        j = i*i
        if j <= 24:
            data[i][j] = np.array([5, 225, 200])
    cv2.imshow("green", data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    cv2.imshow("green1", data2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# print(data[6][6])
# # data[4][5] = np.array([100,5,0])
# cv2.imwrite(r"C:\face_recognize\test_image.png",data)
# cv2.imwrite(r"C:\face_recognize\test_image2.png",data2)
# cv2.imshow("green", data)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

