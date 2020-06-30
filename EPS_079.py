# Section 3.2 32차원 데이터의 시각화
# 
# 3.2.1 산점도(scatter plot) 

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
pd.set_option('precision', 3)

df = pd.read_csv('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/scores_em.csv')
english_scores = np.array(df['english'])
math_scores = np.array(df['mathematics'])

'''
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)


# 산점도

ax.scatter(english_scores, math_scores)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')
'''

# 계수 B0와 B1를 구함
poly_fit = np.polyfit(english_scores, math_scores, 1)
# B0+B1x를 반환하는 함수 작성
poly_1d = np.poly1d(poly_fit)


# x좌표 생성
xs = np.linspace(english_scores.min(), english_scores.max())
# y좌표 생성
ys = poly_1d(xs)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.scatter(english_scores, math_scores, label='score')

ax.plot(xs, ys, color='gray', label=f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')

ax.set_xlabel('english')
ax.set_ylabel('mathematics')

# 범례 표시
ax.legend(loc='upper left')

plt.show()