# 공분산

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import warnings

warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

x_range = [0, 2]
y_range = [0, 1]

def f_xy(x, y):
    if 0 <= y <= 1 and 0<= x-y <=1:
        return 4 * y * (x -y)
    else:
        return 0

XY = [x_range, y_range, f_xy]

def E(XY, g):
    # x_range, y_range, f_xy = XY
    _, _, f_xy = XY
    def integrand(x, y):
        return g(x, y) * f_xy(x, y)
    return integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]

def V(XY, g):
    # x_range, y_range, f_xy = XY
    _, _, f_xy = XY
    mean = E(XY, g)
    def integrand(x, y):
        return (g(x, y) - mean) ** 2 * f_xy(x, y)
    return integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]
 

def Cov(XY):
    # x_range, y_range, f_xy = XY
    _, _, f_xy = XY
    mean_X = E(XY, lambda x, y: x)
    mean_Y = E(XY, lambda x, y: y)
    def integrand(x, y):
        return (x-mean_X) * (y-mean_Y) * f_xy(x, y)
    return integrate.nquad(integrand, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]

var_X = V(XY, lambda x, y: x)
var_Y = V(XY, lambda x, y: y)

cov_xy = Cov(XY)


print(cov_xy)
a, b = 2, 3
print(V(XY, lambda x, y: a*x+b*y))

print(a**2 * var_X+ b**2 * var_Y + 2*a*b * cov_xy)
print(cov_xy / np.sqrt(var_X * var_Y))
