
import numpy as np
# 넘파이 패키지는 수치 계산에 용이함

import pandas as pd

pd.set_option('precision', 3)

df = pd.read_csv('DataSet/scores_em.csv', index_col='student number')

print(df.head())
# 첫 5행만 출력함

scores = np.array(df['english'])[:10]
# 표 데이터에서 english 힝목만 추출해서 10개행만 넘파이 패키지 array 매서드를 이용해서 scores에 저장함

print(scores)

scores_df = pd.DataFrame(
    {'score': scores},
    index=pd.Index(['A','B','C','D','E','F','G','H','I','J'], 
    name='student'))
# 판다스 패키지의 DataFrame 매서드를 통해 score_df에 저장
# 컬럼 네임을 score라고 지정하고 미리 저장한 scores 변수로 연결
# 판다스 패키지의 Index라는 매서르를 이용하여 번호 대신 A~J까지 입력해주고 인덱스 컬럼 명을 student로 지정

print(scores_df)