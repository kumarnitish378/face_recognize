import numpy as np
import time
import sys
import os
import matplotlib.pyplot as plt
import cv2
import math

# s = range(1000)
# print(sys.getsizeof(5)*len(s))
# d = np.arange(1000)
# print(d.size*d.itemsize)
# -----------------------------------------------------------------
# size = 100000
# l1 = range (size)
# l2 = range (size)
# a1 = np.arange(size)
# a2 = np.arange(size)
#
# start = time.time()
# result = [(x,y) for x, y in zip(l1, l2)]
# print((time.time() - start)*1000)
# start = time.time()
# result  = a1+a2
# print((time.time() - start)*1000)
# ----------------------------------------------------
#
# ------------------------reshape of array- and some function-----------------------------
# a = np.array([(1,2,3,4,5,6,7),(4,5,7,5,4,6,5),(4,5,7,50,4,6,5)])
# #print(a.reshape(7,2))
# print(a [0:,3])
# print(a.shape)
# b= np.linspace(1,20,6)
# print(b)
# ------------------------------some predefine function---------------------------
#
# a = np.array([1,2,3,4,5,6])
# print(a.max())
# print(a.min())
# print(a.sum())
# print(a.mean())
# print(a.ravel())
#
# -------------------------------- mathematic fhnction in axis-----------------------
#
# a = np.array([(1,2,3),(4,5,6)])
# print(a.sum(axis=0))
# print(np.sqrt(a))
# print(np.std(a)) #-------------------standererd deviation-------------------
# b = np.array([(1,2,3),(4,5,6)])
# print(a-b)
# print(a+b)
# print(a*b)
# print(a/b)
# print(a%b)
# --------------------------stacking of element -----------------------------
# b = np.array([(1,2,3),(4,5,6)])
# a = np.array([(1,2,3),(4,5,6)])
# #print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(a.ravel())
# --------------------------spacial function in numpy -----------------------
# x = np.arange(0,3*np.pi, 0.1)
# y = np.sin(x)
# y = np.cos(x)
# y = np.tan(x)
# plt.plot(x,y)
# plt.show()
#
# ----------------mathematical log or exponetial function-------------------
#
# ar = np.array([1,2,3])
# print(np.log(ar))
# print(np.log10(ar))
# print(np.log2(ar))
#

image = cv2.imread(r"C:\face_recognize\traning_photo\0\my photo.jpg")
image = cv2.resize(image,(600,400))
print(image.shape)
# pltx = 10
# plty = 10
# while True:
#     if pltx <= 700 and plty <= 800:
#         #image = cv2.rectangle(image, (pltx, plty), (pltx+30, plty+30), (220, 25, 0), 2)
#         image = cv2.resize(image, (pltx, plty))
#     cv2.imshow("edit", image)
#
#     if cv2.waitKey(20) & 0xff == ord('q'):
#         break
#     pltx = pltx+10
#     plty = plty+10
#     if pltx >= 700 or plty >= 800:
#         pltx = 10
#         plty = 10
# image.release()
# cv2.destroyAllWindows()
# image1 = image[40:180,120:230]
# image[55,55] = [250,200,100]
# image = image[55,55]
#lst = []
# for i in image:
#     for j in i:
#         j = j+8
#         lst.append(j)
# image = cv2.rectangle(image, (120,40),(250,200),(120,25,30),5)
# image1 = image+50
image[120:350,80:400] =image[120:350,80:400] - [-50,100,20]
print(image[120:250,40:200].max())
image = cv2.line(image,(10,20),(100,100),(200,0,250),2)
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("orignal",image)
#cv2.imshow("edit",image)
cv2.waitKey(0)
cv2.destroyAllWindows()



