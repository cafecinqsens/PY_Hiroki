# 1차원 연속형 확률변수 - 분산(variance)

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

x_range = np.array([0,1])

def f(x):
    if x_range[0] <= x <= x_range[1]:
        return 2*x
    else:
        return 0

X = [x_range, f]

def E(X, g=lambda x: x):
    # x_range, f = X
    _, f = X
    def integrand(x):
        return g(x) * f(x)
    return integrate.quad(integrand, -np.inf, np.inf)[0]

# 기댓값 E(X)
mean = E(X)
def integrand(x):
    return (x - mean)**2 * f(x)
print(integrate.quad(integrand, -np.inf, np.inf)[0])


# 변환한 확률변수의 분산
def V(X, g=lambda x: x):
    # x_range, f =X
    _, f = X
    mean = E(X, g)
    def integrand(x):
        return (g(x) - mean) ** 2 * f(x) 
    return integrate.quad(integrand, -np.inf, np.inf)[0]

print(V(X), V(X, lambda x: 2*x+3), 2**2*V(X))