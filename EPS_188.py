# 7.2 결합밀도함수
# 7.2.1 2차원 연속형 확률변수의 정의

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import warnings

# 적분에 관한 warning을 출력하지 않는다(MacOS에서는 해줄 필요가 없음)
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

# x_range와 y_range 정의
x_range = [0, 2]
y_range = [0, 1]

# 결합확률밀도함수 정의
def f_xy(x, y):
    if 0 <= y <= 1 and 0<= x-y <=1:
        return 4 * y * (x -y)
    else:
        return 0


# 확률변수 (X, Y)의 움직임은 x_range와 y_range와 f_xy에 정의되므로 이를 리스트로 XY로 정의
XY = [x_range, y_range, f_xy]

# 결합밀도함수를 히트맵으로 그리기
xs = np.linspace(x_range[0], x_range[1], 200)
ys = np.linspace(y_range[0], y_range[1], 200)
pd = np.array([[f_xy(x, y) for y in ys] for x in xs])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

c = ax.pcolor(pd)
ax.set_xticks(np.linspace(0, 200, 3), minor=False)
ax.set_yticks(np.linspace(0, 200, 3), minor=False)
ax.set_xticklabels(np.linspace(0, 2, 3))
ax.set_yticklabels(np.linspace(0, 1, 3))
ax.invert_yaxis()
ax.xaxis.tick_top()
fig.colorbar(c, ax=ax)

# 첫 번째 인수는 피적분함수, 두 번째 인수는 x의 적분구간과 y의 적분구간
print(
    integrate.nquad(f_xy, [[-np.inf, np.inf], [-np.inf, np.inf]])[0]    
    )

# 그래프 띄우기
# plt.show()

