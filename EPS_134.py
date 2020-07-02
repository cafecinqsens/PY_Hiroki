# 주변확률분포

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

prob_x = np.array([f_X(x_k) for x_k in x_set])
prob_y = np.array([f_Y(y_k) for y_k in y_set])

fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.bar(x_set, prob_x)
ax1.set_title('X_marginal probability distibution')
ax1.set_xlabel('X_value')
ax1.set_ylabel('probability')
ax1.set_xticks(x_set)

ax2.bar(x_set, prob_x)
ax2.set_title('Y_marginal probability distibution')
ax2.set_xlabel('Y_value')
ax2.set_ylabel('probability')

plt.show()