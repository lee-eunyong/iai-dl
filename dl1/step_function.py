# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:38:40 2026

@author: lcarr
"""

import matplotlib.pyplot as plt
import numpy as np

def step_function(x):
    return np.array(x>0, dtype=int)
    
x = np.arange(-5.0, 5.0, 0.1)

y = step_function(x)

plt.plot(x, y)

plt.title("Heaviside Step Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.grid()

plt.show()