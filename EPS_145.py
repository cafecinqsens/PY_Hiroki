import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 그래프에서 선의 종류

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

def Bern(p):
    x_set = np.array([0, 1])
    def f(x):
        if x in x_set:
            return p ** x * (1-p) ** (1-x)
        else:
            return 0
    return x_set, f

# Bern(0.3)을 따르는 확률변수 X를 작성
p = 0.3
X = Bern(p)

# 기대값과 분산을 계산
check_prob(X)

# 확률변수 X 그리기
plot_prob(X)

