# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:07:59 2026

@author: lcarr
"""

import matplotlib.pyplot as plt
from matplotlib.image import  imread

img = imread('./images/a.png')

plt.imshow(img)
plt.show()