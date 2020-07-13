# 7.1.2 1차원 연속형 확률변수의 지표
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate



# 확률변수 X가 취하는 구간을 x_range로 정의
x_range = np.array([0,1])

# x_range를 정의역으로 하는 밀도함수 구현
# 2를 곱해서 확률의 성질을 만족
def f(x):
    if x_range[0] <= x <= x_range[1]:
        return 2*x
    else:
        return 0

# 불공정한 룰렛의 기댓값
def integrand(x):
    return x * f(x)
print(round(integrate.quad(integrand, -np.inf, np.inf)[0], 3))

# x_range와 f의 세트가 확률분포
X = [x_range, f]

def E(X, g=lambda x: x):
    # x_range, f = X
    _, f = X
    def integrand(x):
        return g(x) * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]
print(round(E(X), 3))

print(round(E(X, g=lambda x: 2*x+3), 3))
