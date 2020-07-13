#%%

# 누적분포함수(cumulative distribution function)
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

# 분포함수를 파이썬으로 구현
def F(x):
    return integrate.quad(f, -np.inf, x)[0]

# 룰렛이 0.4부터 0.6 사이의 값을 취할 확률
print(F(0.6)-F(0.4))

xs = np.linspace(x_range[0], x_range[1], 100)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.plot(xs, [F(x) for x in xs], label='F(x)', color='gray')
ax.hlines(0, -0.1, 1.1, alpha=0.3)
ax.vlines(0, -0.1, 1.1, alpha=0.3)
ax.vlines(xs.max(), 0, 1, linestyles=':', color='gray')

ax.set_xticks(np.arange(-0.1, 1.2, 0.1))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

ax.legend()

plt.show()

# %%
