import pandas as pd
import numpy as np

df = pd.read_csv('DataSet/scores_em.csv', index_col='student number')

scores = np.array(df['english'])[:10]

# 산포도는 통계에 유의미한 요소
# 산포도의 첫 걸음은 편차(deviation)
# Numpy에는 브로드캐스트라는 기능을 이용하여 배열에 들어있는 숫자 하나하나를 연산하는 기능이 있음

mean = np.mean(scores)
deviation = scores - mean
print(deviation)
# 점수 scores에서 평균 mean을 빼면 편차 deviation이 나오게 된다.

another_scores = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean
print(another_deviation)
# 같은 방식으로 다른 점수를 이용하여 평균과 편차를 연산한다.

print(np.mean(deviation))
print(np.mean(another_deviation))
# 항상 편차의 평균은 0

scores_df = pd.DataFrame(
    {'score': scores},
    index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], 
    name='student'))
# 이전에 작업했던 내용을 가져욌다.

summary_df = scores_df.copy()
# scores_df를 복사해서 summary_df 에 저장

summary_df['deviation'] = deviation
# deviation을 summary_df에 deviation을 만들고 저장함

print(summary_df)
print(summary_df.mean())

'''
= 참고 =
- 산포도라는 의미에서 -14점이든 +14점 모두 동일한 것으로 바라봄
- 편차의 평균이 항상 0이 되는 점을 벗어나기 위해 편차의 제곱을 사용
- 이를 우리는 분산(variance)이라고 함
'''

print(np.mean(deviation ** 2))
# **에 다음 나온 수는 승수를 말함

print(np.var(scores))
# Numpy 패키지에서는 var()를 사용
# 판다스에도 있지만 가급적 넘파이에서 사용할 것을 권장(넘파이는 표본분산이고 판다는 불편분산임, 불편분산은 추측통계에서 역할을 함)
# 표 데이터로 만들기 -> 판다스, 데이터의 연산 -> 넘파이, (아직 나오지 않았지만) 데이터 시각화 -> 맷플롯립



print(scores_df.var())
# 판다스에서 다루는 분산은 넘파이에서 다루는 분산과 차이가 있음
# 판다스 -> 불편분산, 넘파이 -> 표본분산
# var 매서드 인수 ddof=0를 이용하여 표본분산으로 계산가능 


summary_df['square of deviation']=np.square(deviation)
# 분산 값을 'square of deviation' 열에 저장
print(summary_df)


print(summary_df.mean())

print(np.sqrt(np.var(scores, ddof=0)))
# ddof=0 -> 표본분산

print(np.std(scores, ddof=0))
# 표준편차

print(np.max(scores) - np.min(scores))
# 범위(range)

# 사분면 범위
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
scores_IQR = scores_Q3 - scores_Q1
print(scores_IQR)

# 데이터 지표 정리 - 51페이지
print(pd.Series(scores).describe())


# Section 2.3 데이터의 정규화
# 2.3.1 표준화

z = (scores - np.mean(scores)) / np.std(scores)
print(z)

print(round(np.mean(z)), round(np.std(z, ddof=0)))




