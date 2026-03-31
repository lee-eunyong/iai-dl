# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:17:59 2026

@author: lcarr
"""
import numpy as np

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    """
    if tmp <= 0:
        return 0
    else:
        return 1
   
def NAND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1
    
    
def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1
    
    
if __name__ == '__main__':
    rtn1 = NAND(0,0)
    rtn2 = OR(0,0)
    rtn = AND(rtn1,rtn2)
    print(f"{rtn}")
    rtn1 = NAND(1,0)
    rtn2 = OR(1,0)
    rtn = AND(rtn1,rtn2)
    print(f"{rtn}")
    rtn1 = NAND(0,1)
    rtn2 = OR(0,1)
    rtn = AND(rtn1,rtn2)
    print(f"{rtn}")
    rtn1 = NAND(1,1)
    rtn2 = OR(1,1)
    rtn = AND(rtn1,rtn2)
    print(f"{rtn}")