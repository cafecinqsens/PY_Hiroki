# 누적분포함수(cumulative distribution function, CDF)


import numpy as np

def f(x):
    if x in x_set:
        return x / 21
    else :
        return 0

x_set = [1, 2, 3, 4, 5, 6]


# 누적분포함수의 정의
def F(x):
    return np.sum([f(x_k) for x_k in x_set if x_k <= x])


# 주사위 눈이 3 이하가 되는 확률
print(F(3))