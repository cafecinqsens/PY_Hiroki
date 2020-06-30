# 4.2 확률 모형

# 4.2.2 확률 분포

# 확률 정의

import numpy as np
import pandas as pd



dice = [1, 2, 3, 4, 5, 6]
prob = [1/21, 2/21, 3/21, 4/21, 5/21, 6/21]
print(np.random.choice(dice, p=prob))

num_trial = 100000
sample = np.random.choice(dice, size=num_trial, p=prob)

print(sample)

freq, _= np.histogram(sample, bins=6, range=(1,7))

df = pd.DataFrame({'frequency': freq, 'relative': freq / num_trial}, index = pd.Index(np.arange(1,7), name ='dice'))
print(df)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax =fig.add_subplot(111)
# 히스토그램 그리기
ax.hist(sample, bins=6, range=(1,7), density=True, rwidth=0.8)
# bins -> 막대영역의 범위, range -> x축의 범위, density -> 데이터 정규화, rwidth -> 바의 너비

ax.hlines(prob, np.arange(1, 7), np.arange(2, 8), colors='gray')
ax.set_xticks(np.linspace(1.5, 6.5, 6))

ax.set_xticklabels(np.arange(1,7))
ax.set_xlabel('dice')
ax.set_ylabel('relative frequency')
plt.show()