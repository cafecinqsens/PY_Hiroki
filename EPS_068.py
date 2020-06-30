# Section 3.1 두 데이터 사이의 관계를 나타내는 지표

# 3.1.1 공분산

import numpy as np
import pandas as pd
pd.set_option('precision', 3)


# 점수 가져오기
df = pd.read_csv('/Volumes/JAEGWAN/10.DEV/PYSTAT/PY_Hiroki/DataSet/scores_em.csv')
en_scores = np.array(df['english'])[:10]
ma_scores = np.array(df['mathematics'])[:10]

scores_df = pd.DataFrame({'english': en_scores, 'mathematics': ma_scores}, index=pd.Index(['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I', 'J']))

print(scores_df)


# 공분산 계산

summary_df = scores_df.copy()
summary_df['english_deviation'] =\
    summary_df['english'] - summary_df['english'].mean()
summary_df['mathematics_deviation'] =\
    summary_df['mathematics'] - summary_df['mathematics'].mean()
summary_df['product of deviation'] =\
    summary_df['english_deviation']*summary_df['mathematics_deviation']

print(summary_df)

print(summary_df['product of deviation'].mean())


cov_mat = np.cov(en_scores, ma_scores, ddof=0)

print('공분산의 행렬 ->', cov_mat)

print('공분산 비교 ->', cov_mat[0, 1], cov_mat[1, 0])

print('영어와 수학 분산 ->', cov_mat[0, 0], cov_mat[1, 1])
print('영어와 수학 분산 비교 ->', np.var(en_scores, ddof=0), np.var(ma_scores, ddof=0))


# 영어와 수학의 상관계수
print('영어와 수학의 상관계수 ->', np.cov(en_scores, ma_scores, ddof=0)[0,1] / (np.std(en_scores) * np.std(ma_scores)))
print('넘파이에서의 상관행렬 ->', np.corrcoef(en_scores, ma_scores))
print('판다스에서의 상관계수 ->', scores_df.corr())



