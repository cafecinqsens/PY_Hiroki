# 확률변수의 변환
import numpy as np

x_set = [1, 2, 3, 4, 5, 6]

# 확률변수 Y를 2X + 3으로 정의 
y_set = np.array([2 * x_k + 3 for x_k in x_set])

def f(x):
    if x in x_set:
        return x / 21
    else :
        return 0

prob = np.array([f(x_k) for x_k in x_set])


# 사전형으로 출력
print(dict(zip(y_set, prob)))