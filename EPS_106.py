# 4.3 추측통계의 확률
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('precision', 3)

df = pd.read_csv('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/ch4_scores400.csv')
scores = np.array(df['score'])

sample_means = [np.random.choice(scores, 20).mean() for _ in range(10000)]



fig = plt.figure(figsize=(10, 6))

ax = fig.add_subplot(111)

ax.hist(sample_means, bins=100, range=(0, 100), density=True)

# 모평균을 세로선으로 표시
ax.vlines(np.mean(scores), 0, 1, 'gray')
ax.set_xlim(50, 90)
ax.set_ylim(0, 0.13)

ax.set_xlabel('scores')
ax.set_ylabel('relative frequency')
plt.show()