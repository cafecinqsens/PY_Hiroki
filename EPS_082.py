# 3.2.3 히트맵
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
pd.set_option('precision', 3)

df = pd.read_csv('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/scores_em.csv')
english_scores = np.array(df['english'])
math_scores = np.array(df['mathematics'])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

c = ax.hist2d(english_scores, math_scores, bins=[9, 8], range=[(35, 80), (55, 95)])
ax.set_xlabel('english')
ax.set_ylabel('mathematics')

ax.set_xticks(c[1])
ax.set_yticks(c[2])

# 컬러 바 표시

fig.colorbar(c[3], ax=ax)

plt.show()