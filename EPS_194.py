 # 7.2.2 2차원 연속형 확률변수
 # 기대값

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import warnings

# 적분에 관한 warning을 출력하지 않는다
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

x_range = [0, 2]
y_range = [0, 1]


def f_xy(x, y):
    if 0 <= y <= 1 and 0<= x-y <=1:
        return 4 * y * (x -y)
    else:
        return 0
    
def integrand(x, y):
    return x * f_xy(x, y)

XY = [x_range, y_range, f_xy]

# x와 밀도함수의 곱을 x와 y로 적분하여 구할 수 있음
print(integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0])


# X, Y의 함수 g(X, Y)의 기댓값을 정의할 수 있음
def E(XY, g):
    # x_range, y_range, f_xy = XY
    _, _, f_xy = XY
    def integrand(x, y):
        return g(x, y) * f_xy(x, y)
    return integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]

mean_X = E(XY, lambda x, y: x)
mean_Y = E(XY, lambda x, y: y)

print(mean_X, mean_Y)



# 2차원 연속형 확률변수에서도 기댓값의 선형성 성립
# E(2X + 3Y) = 2E(X) + 3E(Y)
a, b = 2, 3
print(E(XY, lambda x, y : a * x + b * y ), a * mean_X + b * mean_Y)
