# 데이터를 하나의 값으로 요약한 지표를 대표값이라고 한다.
# 평균값은 잘 알려진 대표값으로 (모든 데이터의 합계/데이터의 개수)로 계산

import pandas as pd
import numpy as np

df = pd.read_csv('DataSet/scores_em.csv', index_col='student number')

scores = np.array(df['english'])[:10]

print(np.mean(scores))
# 평균값을 연산할 때에는 mean()을 사용
# 판다스에서도 사용하지만 넘파이 패키지의 mean()을 사용하는 것으로 통일



print(np.median(scores))
# 중앙값 -> 데이타를 크기 순서대로 나열할 때 중앙에 위치하는 값
# 중앙값을 연산하기 위햐서 median()을 사용
# 판다스 패키지에도 사용 가능

test = pd.Series([1,1,1,2,2,3])

print(test.mode())
# 최빈값 -> 가장 많이 나타는 값
# 최빈값은 판다스 패키지의 mode()를 사용하여 연산함
