# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:52:00 2026

@author: lcarr
"""

import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    return 1 / (1+ np.exp(-x))
    
x = np.arange(-5.0, 5.0, 0.1)

y = sigmoid(x)

plt.plot(x, y)

plt.title("Heaviside sigmoid Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.grid()

plt.show()