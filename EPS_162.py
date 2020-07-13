import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


linestyles = ['-', '--',':']

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

x_set = np.arange(1, 15)

for p, ls in zip([0.2, 0.5, 0.8], linestyles):
    rv = stats.geom(p)
    ax.plot(x_set, rv.pmf(x_set), label=f'p:{p}', ls=ls, color='gray')

ax.set_xticks(x_set)
ax.legend()

plt.show()