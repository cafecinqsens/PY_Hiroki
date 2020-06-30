# Section 3.3 앤스컴의 예

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

anscombe_data = np.load('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/ch3_anscombe.npy')
print('앤스컴의 데이터 ->\n', anscombe_data)
print('인덱스 0의 값 ->\n ', anscombe_data[0])

stats_df = pd.DataFrame(index=['X_mean', 'X_variance', 'Y_mean', 'Y_variance', 'X&Y_correlation', 'X&Y_regression line'])


for i, data in enumerate(anscombe_data):
    dataX = data[:, 0]
    dataY = data[:, 1]

    poly_fit = np.polyfit(dataX, dataY, 1)
    stats_df[f'data{i+1}'] = \
        [f'{np.mean(dataX):.2f}',
        f'{np.var(dataX):.2f}',
        f'{np.mean(dataY):.2f}',
        f'{np.var(dataY):.2f}',
        f'{np.corrcoef(dataX, dataY)[0, 1]:.2f}',
        f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x']
print(stats_df)    


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10), sharex=True, sharey=True)

xs = np.linspace(0, 30, 100)

for i, data in enumerate(anscombe_data):
    poly_fit = np.polyfit(data[:,0], data[:, 1], 1)
    poly_1d = np.poly1d(poly_fit)
    ys = poly_1d(xs)

    # 그리는 영역을 선택
    ax = axes[i//2, i%2]
    ax.set_xlim([4, 20])
    ax.set_ylim([3, 13])

    # 타이틀을 부여

    ax.set_title(f'data{i+1}')
    ax.scatter(data[:,0], data[:,1])
    ax.plot(xs, ys, color='gray')

plt.tight_layout()
plt.show()