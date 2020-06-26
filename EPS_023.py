import pandas as pd

df = pd.read_csv('DataSet/sport_test.csv', index_col='학생번호')

print(df.shape)

'''
= 참고 =
- 결과값은 (10, 5)가 나오는데 10행 5열의 데이터 프레임을 말함
- 다른 레퍼런스에서는 행과 열을 레코드(recodes)와 칼럼(columns)이라고도 표현함
- 레코드는 로우(rows)라고 표현하기도 함

- 통계에서는 각 엘리먼트 간의 관계성에 주목하는 것이 특징임
'''