# 분산

import numpy as np

x_set = [1, 2, 3, 4, 5, 6]

def f(x):
    if x in x_set:
        return x / 21
    else :
        return 0

X = [x_set, f]

def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k)*f(x_k) for x_k in x_set])

# 확률변수의 평균 = 기댓값
mean = E(X)

# 분산의 연산
print(np.sum([(x_k-mean)**2*f(x_k) for x_k in x_set]))


# 분산의 함수로 구현

def V(X, g=lambda x: x):
    x_set, f = X
    mean = E(X, g)
    return np.sum([g(x_k-mean)**2*f(x_k) for x_k in x_set])

# 람다를 지정하지 않을 때
print('람다 지정 없음->',V(X))


# 람다를 지정할 때
print(V(X, lambda x: 2*x+3))

# 분산의 공식 증명
print('분산의 공식 증명:', )
