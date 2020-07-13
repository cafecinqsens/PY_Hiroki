import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import warnings

# 적분에 관한 warning을 출력하지 않는다
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)

# 확률변수 X가 취하는 구간을 x_range로 정의
x_range = np.array([0,1])

# x_range를 정의역으로 하는 밀도함수 구현
# 2를 곱해서 확률의 성질을 만족
def f(x):
    if x_range[0] <= x <= x_range[1]:
        return 2*x
    else:
        return 0

# x_range와 f의 세트가 확률분포
X = [x_range, f]

# 넘파이의 등간격을 이용하여 구간 내의 100개의 실수를 xs에 저장
xs = np.linspace(x_range[0], x_range[1], 100)

# 그림 사이즈를 가로 10, 세로 6으로 정의하고 fig에 저장 
fig = plt.figure(figsize=(10, 6))

# 하나의 그래프만 그린다는 의미
ax = fig.add_subplot(111)

# 그래프의 데이터는 x축은 xs로 y축은 함축의 기능을 이용하여 xs의 각 원소인 x를 추출하여 f(x)에 대응하는 값으로 설정
# 라벨은 f(x)라고 하고 색상은 회색으로 지정
ax.plot(xs, [f(x) for x in xs], label='f(x)', color='gray')

# vlines(선을 그을 y의 위치, x에 그을 최소값, x에 그을 최댓값, 불투명도)
ax.hlines(0, -0.2, 1.2, alpha=0.3)
# vlines(선을 그을 x의 위치, y에 그을 최소값, y에 그을 최댓값, 불투명도)
ax.vlines(0, -0.2, 2.2, alpha=0.3)

# linestyles -> 수직선에 적용할 라인의 형태
ax.vlines(xs.max(), 0, 2.2, linestyles=':', color='gray')

# 0.4부터 0.6까지 x좌표를 준비
xs = np.linspace(0.4, 0.6, 100)

# xs를 범위로 f(x)와 x축으로 둘러싸인 영역에 색을 적용
ax.fill_between(xs, [f(x) for x in xs], label='prob')

# 그래프 눈금
ax.set_xticks(np.arange(-0.2, 1.3, 0.1))

# 축의 한계 설정
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.2, 2.1)

# 범례 표시
ax.legend()

# 첫 번째 인수는 피적분함수, 두 번째와 세 번째 인수는 적분 범위
print(integrate.quad(f, 0.4, 0.6))

# 연속형 확률변수에서  확률의 성질로서 첫 번째 f(x)가 항상 0 이상의 값을 취함
# 최소값을 구하는 함수를 minimize_scalar를 사용
from scipy.optimize import minimize_scalar

res = minimize_scalar(f)

# f(x) 최솟값을 알기 위해 res 중에 fun이라는 인스턴스에 접근하여 출력
print(res.fun)

# 확률의 성질 두 번째에서 -무한대에서 +무한대까지 적분한 결과가 1이라는 것을 증명 필요
print(integrate.quad(f, -np.inf, +np.inf))

# 불공정한 룰렛에 대한 밀도함수와 확률
# plt.show()

