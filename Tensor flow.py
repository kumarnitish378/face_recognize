# import tensorflow as tf
# from tensorflow import keras
# import  numpy
import matplotlib.pyplot as plt
import numpy as np
#import matplot as mlt
a = np.array([12,23,33])
b = np.array([45,56,67])
if a.any() == b.any():
    print("matched...")
else:
    print("dont match")
a = [12,23,34,45,56,30,78,89]
width = 0.35
plt.plot(a)
plt.show()
