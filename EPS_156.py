# 이항분포를 scipy.stats에서 구하기

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n = 10

# 그래프 선 스타일 지정
linestyles = ['-', '--',':']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# n을 10으로 고정하고 p값을 변화
x_set = np.arange(n+1)
for p, ls in zip([0.3, 0.5, 0.7], linestyles):
    # 확률변수는 binom으로 구현
    rv = stats.binom(n, p)
    ax.plot(x_set, rv.pmf(x_set), label=f'p:{p}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()

plt.show()