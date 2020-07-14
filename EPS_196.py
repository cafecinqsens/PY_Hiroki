# 분산
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
    

XY = [x_range, y_range, f_xy]

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

def integrand(x, y):
    return (x- mean_X)**2 * f_xy(x, y)
print(integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0])

def V(XY, g):
    # x_range, y_range, f_xy = XY
    _, _, f_xy = XY
    mean = E(XY, g)
    def integrand(x, y):
        return (g(x, y) - mean) ** 2 * f_xy(x, y)
    return integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]

var_X = V(XY, lambda x, y: x)
var_Y = V(XY, lambda x, y: y)
print(var_X, var_Y)