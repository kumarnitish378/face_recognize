import cv2
from random import randint
import numpy as np
import time
import matplotlib.pyplot as plt
lst1 = cv2.imread(r"C:\face_recognize\test_color.png")
image = cv2.imread(r"C:\face_recognize\traning_photo\0\IMG-20190501-WA0002.jpg")
# print(image.shape)
lst1 = cv2.resize(lst1, (550, 300))
image = cv2.resize(image, (550, 300))
#                       (colon, row)
print(lst1.shape)

# a = lst2.shape
# print(a)
# # lst2[0:5, 0:a[1]] =  [0,255,255]
# b = lst2[0:150, 0:a[1]]
# lst2[0:150, 150:a[1]] = lst2[150:300, 150:a[1]]
# lst2[150:300, 0:a[1]] = b

print(lst1[0][0])
a = lst1.shape
colon = []
row = []
# for i in range(a[0]):
#     for j in range(a[1]):
#         if list(lst1[i][j]) == [39, 127, 255]:
#             # print("colon: {}, Row: {} = {}".format(i, j,lst1[i][j]))
#             lst1[i,j] = image[i, j ]# [255,2,255]

for i in range(a[0]):
    for j in range(a[1]):
        if list(lst1[i][j]) == [255, 255, 255]:
            # print("colon: {}, Row: {} = {}".format(i, j,lst1[i][j]))
            lst1[i,j] = image[randint(0,299),randint(0,299)]# image[i, j ]-[25,2,10] #lst1[i:i+3,j:j+3]+[25,2,10]


cv2.imshow("green", lst1)
# cv2.imshow("cut", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("....")
