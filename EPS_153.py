# 6.2 이항분포(binominal distribution)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 이항분포를 넘파이로 구현
# nCx를 구할 때에는 scipy.special에 있는 comb 함수 사용

from scipy.special import comb

def Bin(n, p):
    x_set = np.arange(n+1)
    def f(x):
        if x in x_set:
            return comb(n, x) * p**x * (1-p)**(n-x)
        else:
            return 0
    return x_set, f

# 사전정의 항목
linestyle = ['-', '--',':']


def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])

def V(X, g=lambda x: x):
    x_set, f = X
    mean = E(X, g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])

def check_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    assert np.all(prob >= 0), 'minus probability'
    prob_sum = np.round(np.sum(prob), 6)
    assert prob_sum == 1, 'sum of probability(prob_sum)'
    print(f'expected value {E(X):.4}')
    print(f'variance{(V(X)): .4}')

def plot_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.bar(x_set, prob, label='prob')
    ax.vlines(E(X), 0, 1, label='mean')
    ax.set_xticks(np.append(x_set, E(X)))
    ax.set_ylim(0, prob.max()*1.2)
    ax.legend(loc='upper right', labels=['mean', 'prob'])

    plt.show()

# Bin(10, 0.3)을 따르는 확률변수 X를 작성

n = 10
p = 0.3
X = Bin(n, p)

check_prob(X)

plot_prob(X)