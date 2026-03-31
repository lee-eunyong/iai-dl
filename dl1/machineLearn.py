# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:00:02 2026

@author: lcarr
"""
import numpy as np
import matplotlib.pyplot as plt

# x 값 생성 (0 ~ 2π)
x = np.linspace(0, 2*np.ppi, 100)

# 사인 값 계산
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)

# 그래프 꾸미기
plt.title("Cos Wave")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(False)

# 그래프 출력
plt.show()