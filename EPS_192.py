# 7.2.1 2차원 연속형 확률변수의 정의

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# 파이썬 표준라이브러리에 있는 functools의 partial 함수
# partial은 인수의 일부를 고정한 새로운 함수를 만들 수 있는 함수
# partial(f_xy, x)라고 하면 함수 f_xy의 인수 x, y 중 x가 고정되고, 인수가 y만으로 된 함수가 반환됨


from functools import partial


x_range = [0, 2]
y_range = [0, 1]

def f_xy(x, y):
    if 0 <= y <= 1 and 0<= x-y <=1:
        return 4 * y * (x -y)
    else:
        return 0

def f_X(x):
    return integrate.quad(partial(f_xy, x), -np.inf, np.inf)[0]

def f_Y(y):
    return integrate.quad(partial(f_xy, y=y), -np.inf, np.inf)[0]

X = [x_range, f_X]
Y = [y_range, f_Y]


xs = np.linspace(*x_range, 100)
ys = np.linspace(*y_range, 100)

fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(xs, [f_X(x) for x in xs], color='gray')
ax2.plot(ys, [f_Y(y) for y in ys], color='gray')

ax1.set_title('X_marginal desity function')
ax2.set_title('Y_marginal desity function')

plt.show()