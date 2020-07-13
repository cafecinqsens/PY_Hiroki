# 확률변수의 변환


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# 분포함수를 G(y)라 하고 파이썬으로 구현
y_range = [3, 5]

def g(y):
    if y_range[0] <= y <= y_range[1]:
        return (y-3)/2
    else:
        return 0


def G(y):
    return integrate.quad(g, -np.inf, y)[0]

ys = np.linspace(y_range[0], y_range[1], 100)
fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(111)

ax.plot(ys, [g(y) for y in ys], label='g(y)', color='gray')
ax.plot(ys, [G(y) for y in ys], label='G(y)', color='gray')

ax.hlines(0, 2.8, 5.2, alpha=0.3)
ax.vlines(ys.max(), 0, 1, linestyles=':', color='gray')

ax.set_xticks(np.arange(2.8, 5.2, 0.2))
ax.set_xlim(2.8, 5.2)
ax.set_ylim(-0.1, 1.1)

ax.legend()

plt.show()