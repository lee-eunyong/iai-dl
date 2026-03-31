# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:55:40 2026

@author: lcarr
"""

import matplotlib.pyplot as plt
import numpy as np


def step_function(x):
    return np.array(x>0, dtype=int)

def sigmoid(x):
    return 1 / (1+ np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)

y = step_function(x)

z = np.arange(-5.0, 5.0, 0.1)

w = sigmoid(z)


plt.plot(x, y)
plt.plot(z, w)

plt.title("Heaviside Step & sigmoid Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.grid()

plt.show()
    