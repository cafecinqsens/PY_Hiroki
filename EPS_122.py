# 5.1.2 1차원 이산형 확률변수의 지표
# 기대값

import numpy as np


# 불공정한 주사위의 정의
x_set = [1, 2, 3, 4, 5, 6]

def f(x):
    if x in x_set:
        return x / 21
    else :
        return 0

# 기댓값 정의 -> 기댓값 = 확률변수의 평균 -> 확률변수가 취하는 값과 그 확률의 곱의 총합
print(np.sum([x_k * f(x_k) for x_k in x_set]))

prob = np.array([f(x_k) for x_k in x_set])

# 100만번(=10의 6승) 무제한 시행(trial)
sample = np.random.choice(x_set, int(1e6), p=prob)
print(np.mean(sample))


# 기댓값 함수 구현
# 람다는 이름없는 함수
# lambda 매개변수 : 표현식
X = [x_set, f]
def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k)*f(x_k) for x_k in x_set])

print(E(X))

# 기댓값의 선형성
print('기댓값의 선형성 ->', 2*E(X)+3)