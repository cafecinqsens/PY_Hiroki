# 5.1 1차원 이산형 확률변수

# 5.1.1 1차원 이산형 확률변수의 정의
# 확률질량 함수
import numpy as np
import matplotlib.pyplot as plt

# 주사위의 정수
x_set = [1, 2, 3, 4, 5, 6]

# 불공정한 주사위의 확률 계산
def f(x):
    if x in x_set:
        return x / 21
    else :
        return 0

# 확률변수가 취할 수 있는 값의 집합과 확률변수의 세트가 확률분포
# 해당 확률분포에 의해 확률변수 X의 동작이 결정

# 확률변수 X가 정의
X = [x_set, f]

# 확률 p_k를 구함
prob = np.array([f(x_k) for x_k in x_set])

# x_k와 p_k의 대응을 사전식으로 표시
print(dict(zip(x_set, prob)))

fig = plt.figure(figsize=(10,6))

ax = fig.add_subplot(111)
ax.bar(x_set, prob)
ax.set_xlabel('value')
ax.set_ylabel('probability')

# 확률은 절대적으로 0 이상을 취함
print('확률 검증 ->', np.all(prob >= 0))

# 확률의 총합은 1임
print('확률의 총합 ->', np.sum(prob))

plt.show()