# 5.2.2 2차원 이산형 확률변수의 지표

# 기댓값
import numpy as np
import matplotlib.pyplot as plt


x_set = np.arange(2, 13)
y_set = np.arange(1,7)

def f_XY(x, y):
    if 1<= y <=6 and 1<= x - y <= 6:
        return y * (x -y) / 441
    else:
        return 0

def f_X(x):
    return np.sum([f_XY(x, y_k) for y_k in y_set])

def f_Y(y):
    return np.sum([f_XY(y, y_k) for y_k in y_set])

X = [x_set, f_X]
Y = [y_set, f_Y]

np.sum([x_i * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])