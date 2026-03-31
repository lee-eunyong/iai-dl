# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:00:12 2026

@author: lcarr
"""
# import sigmoid as sg
import matplotlib.pyplot as plt
import numpy as np

def relu(x):
    return np.maximum(0,x)
    
x = np.arange(-5.0, 5.0, 0.1)

y = relu(x)
# y = sg.sigmoid(x)

plt.plot(x, y)

plt.title("Heaviside ReLU Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-1, 5) # y축의 범위 지정
plt.grid()

plt.show()