import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


p = 0.3
# scipy.stats를 사용하여 구현
# 베르누이 함수는 인수로 파라미터 p를 취하고, Bern(p)를 따르는 rv_frozen object를 반환함
# rv_frozen object는 scipy.stats의 확률변수에 해당함
rv = stats.bernoulli(p)

# .pmf()는 확률질량함수(probability mass function)
# pmf 메서드는 인수로 리스트를 넘길 수 있음
print(rv.pmf([0,1]))

# .cdf()는 누적밀도함수(cumulative distribution function)
print(rv.cdf([0, 1]))

# 기댓값이나 분산을 계산 가능
print(rv.mean(), rv.var())