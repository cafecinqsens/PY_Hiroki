# 확률의 성질
import numpy as np
import matplotlib.pyplot as plt
# X와 Y가 취할 수 있는 값의 집합을 정의
x_set = np.arange(2, 13)
y_set = np.arange(1,7)

# 결합확률함수를 정의
def f_xy(x, y):
    if 1<= y <=6 and 1<= x - y <= 6:
        return y * (x -y) / 441
    else:
        return 0

# 확률변수 (X, Y)의 움직임은 x_set, y_set, f_xy에 의해 정의되므로, 리스트 XY를 선언하여 저장

XY = [x_set, y_set, f_xy]


prob = np.array([[f_xy(x_i, y_j) for y_j in y_set] for x_i in x_set])

mat = np.array([[f_xy(x_i, y_j) for y_j in y_set] for x_i in x_set]).shape()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

c = ax.pcolor(prob)

# 눈금 그리기(.shape[0] -> 행의 갯수, .shape[1] -> 열의 갯수)
ax.set_xticks(np.arange(prob.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(prob.shape[0]) + 0.5, minor=False)

# 눈금 라벨 그리기
ax.set_xticklabels(np.arange(1, 7), minor=False)
ax.set_yticklabels(np.arange(2, 13), minor=False)

# y축 바꾸기
ax.invert_yaxis()

# x축 눈금 위로 바꾸기
ax.xaxis.tick_top()

fig.colorbar(c, ax=ax)

# 확률 0 이상
print(np.all(prob >= 0))

# 확률의 총합 1
print(np.sum(prob))

plt.show()


