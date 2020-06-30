import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('precision', 3)

df = pd.read_csv('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/ch4_scores400.csv')
scores = np.array(df['score'])
print(scores[:10])

# Section 4.1 모집단과 표본

# 4.1.1. 표본추출 방법

# 무작위추출
print(np.random.choice([1,2,3], 3))

# 비복원추출
print(np.random.choice([1,2,3], 3, replace=False))

# 난수 시드
np.random.seed(0)
sample = np.random.choice(scores, 20)

print(sample.mean(), scores.mean())

# 여러번의 무작위추출에 따른 표본평균 계산

for i in range(5):
    sample = np.random.choice(scores, 20)
    print(f'{i+1}번째 무작위추출로 얻은 표본평균', sample.mean())
