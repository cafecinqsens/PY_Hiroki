# 5.2.2 2차원 이산형 확률변수의 지표

# 기댓값
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=3)

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

XY = [x_set, y_set, f_XY]

# 수식을 파이썬으로 구현
print(np.sum([x_i * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set]))


# 기댓값을 함수로 구현
def E(XY, g):
    x_set, y_set, f_XY = XY
    return np.sum([g(x_i, y_j)*f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])

mean_X = E(XY, lambda x, y: x)
print('mean_X: ', mean_X)

mean_Y = E(XY, lambda x, y: y)
print('mean_Y: ', mean_Y)

# a, b를 각각 2, 3에 두고 선형성이 성립하는지 확인
a, b = 2, 3

# 람다는 일시적으로 사용하고 버리는 함수를 의미
print(E(XY, lambda x, y: a * x + b * y))
print(a * mean_X + b * mean_Y)

# 분산 = 편차 제곱의 기댓값
print(np.sum([(x_i-mean_X)**2 * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set]))


# 분산을 함수로 구현

def V(XY, g):
    x_set, y_set, f_XY = XY
    mean = E(XY, g)
    return np.sum([(g(x_i, y_j)-mean)**2 * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])


# X와 Y의 분산
var_X = V(XY, lambda x, y: x)
print('분산X:', var_X)
var_Y = V(XY, lambda x, y: y)
print('분산Y:', var_Y)

# 공분산을 파이썬으로 구현
def Cov(XY):
    x_set, y_set, f_XY = XY
    mean_Y = E(XY, lambda x, y: x)
    mean_Y = E(XY, lambda x, y: y)
    return np.sum([(x_i-mean_X)*(y_j-mean_Y)*f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])

cov_xy = Cov(XY)
print('공분산:', cov_xy)

#  V(aX + bY)의 분산과 공분산의 공식 증명
print(V(XY, lambda x, y: a*x + b*y))
print(a**2 * var_X + b**2 * var_Y + 2*a*b * cov_xy)

# 상관계수

print('상관계수: ',cov_xy / np.sqrt(var_X * var_Y))