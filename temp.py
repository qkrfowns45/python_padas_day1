# -*- coding: utf-8 -*-
# pandas 불러오기
import pandas as pd
 
dict_data = {'a' : 1,'b' : 2,'c' : 3}

#판다스 Series() 함수로 사전을 Series로 변환해서 sr에 저장
sr = pd.Series(dict_data)

print(type(sr))
print('\n')

print(sr) 


list_data = ['2021-11-03',3.14,'abc',100,True]
st = pd.Series(list_data)
print(st)

idx = st.index
val = st.values
print(idx)
print(val)

#2차원 배열로 저장하는 DataFrame

exam_data = {'이름' : ['서준', '우현' , '인아'],
             '수학' : [90,80,70],
             '영어' : [98,89,95],
             '음악' : [85,95,100],
             '체육' : [100,90,90]}

df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print('\n')

df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준' , '체육'] = 100
print(df)
print('\n')

df.loc['서준',['음악', '체육']] = 50
print(df)
print('\n')

#DataFrame 행과 열 바꾸기
exam_data2 = {'이름' : ['서준', '우현' , '인아'],
             '수학' : [90,80,70],
             '영어' : [98,89,95],
             '음악' : [85,95,100],
             '체육' : [100,90,90]}

df2 = pd.DataFrame(exam_data2)
print(df2)
print('\n')

df2 = df2.transpose()
print(df2)
print('\n')

df2 = df2.T
print(df2)
print('\n')







