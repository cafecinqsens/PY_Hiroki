import pandas as pd
# 판다스 패키지를 불러오고 pd로 축약해서 쓴다. 

df = pd.read_csv('DataSet/sport_test.csv', index_col='학생번호')
# DataSet 폴더에서 sport_test라는 csv파일을 인덱스를 학생번호를 기준으로 삼아 판다스 패키지로 읽어들인다.

print(df)
# index_col을 지우고 프린트하면 값이 테이블 형태가 달라진다.

print(df['악력'])
# 특정 열만 출력하고 싶으면 열 네임을 대괄호를 이용하여 출력하면 된다.

'''
== 참고 ==

변수(variable) -> 값이 정해지지 않는 임의의 기호, 프로그램 영역에서는 줄여서 var이라고 표현함
배열(array) -> 같은 타입(type)으로 이루어진 유한 집합(혹은 데이터 모음), 여기서 각각의 데이터를 엘리먼트(element)라고 하고 각 엘리먼트의 위치를 표현하는 값을 인덱스(index)라고 한다.

판다스 패키지(Pandas Package) -> 통계분석에서 표 데이터를 처리하는 일종의 라이브러리
데이터 프레임(DataFrame) -> 2차원 표 데이터 구조, 2차원 배열이라고도 함, df는 데이터 프레임 구조임
시리즈(Series) -> 1차원 표 데이터 구조, df['악력']은 시리즈 구조임

'''