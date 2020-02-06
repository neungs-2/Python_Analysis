#*********************** 10 minuates to Pandas ***********************

import pandas as pd
import numpy as np

#%% ****************** Syntax ******************
# DataFrame 생성
df = pd.DataFrame(
        {"a" : [4,5,6],
         "b" : [7,8,9],
         "c" : [10, 11, 12]},
        index = [1,2,3]           
)

#%% DataFrame에서 해당 row, column, 값 불러오기
print(df[["a","c"]],'\n', df.loc[2],'\n')
print(df.loc[3,"a"],'\n')
print(df.loc[[1,2],['a','c']],'\n')

#%% 여러 개의 Index가 있는 DataFrame 생성
df = pd.DataFrame(
        {'a': [4,5,6,6],
         'b': [7,8,9,9],
         'c': [10,11,12,12]},
        index = pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2),('e',3)],
            names=['n', 'v']
        )
)

df
#%% ********************  Subset  ********************
# 특정 값과 비교한 값만 가져오는 법
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')
print(df['b']!=7,'\n')
print(df[df['b']!=7],'\n')

#%%중복된 행을 제거
df = df.drop_duplicates()
print(df)

df = pd.DataFrame(
        {'a': [4,5,6,np.nan],
         'b': [7,8,np.nan,9],
         'c': [10,11,12,13]},
        index = pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2),('e',3)],
            names=['n', 'v']
        )
)
print()
print(df,'\n')

#%% isin() 해당값이 포함 여부 T/F
#   isnull()/notnull() null 여부 T/F
print(df.a.isin([5,6])) # a열에 5 또는 6 포함 여부
print(df['a'].isin([5,6]),'\n') #같은 결과

print(pd.isnull(df))
print(df['b'].isnull())
print(df['b'].isnull().sum(),'\n') #null 값 개수

print(pd.notnull(df))
print(df.notnull().sum())

# and, or, not, xor, any, all  -->DataFrame에서 사용 불가
#     &, |, ~, ^, df.any(), df.all()

#%%
import seaborn as sns

df = sns.load_dataset('iris')
#%%
df.head(10)
#%%
df[['sepal_width','sepal_length','species']]
#%%
df.sepal_length

# %% '정규표현식'에 해당되는 열만 가져오기
print(df.filter(regex='_')) #_가 포함
print(df.filter(regex='length$')) #length로 끝나는
print(df.filter(regex='^sepal')) #sepal로 시작하는
df.filter(regex='^(?!species).*') #(?!species)문자가 들어간 것 빼고 가져와라

# %% 지정 데이터 불러오기
df.loc[2:4,'sepal_width':'petal_length'] #(a:b)행, (c:d)열 불러오기
df.iloc[-5:,[1,3]] #(a:b-1)행, (c,d-1)열 불러오기
# %% sepal_length가 5보다 큰 데이터의 length, width 열을 불러오기
df.loc[df.sepal_length > 5, ['sepal_length','sepal_width']]

# %%  *************** Summarize Data ***************
df.shape #(행,열) 개수
len(df) #행 개수
df.head(3)

# %% Row 종류와 해당 데이터 개수 *유용함
df['species'].value_counts()
df['sepal_length'].value_counts()
df['species'].nunique()   #Row 종류 수 

# %% 수치형 데이터 통계값
df.describe()  #수치형 아니면 안나옴
df.describe(include = 'all') # 모두 나옴
df.describe(include = [np.object]) #범주형(?)만
df.describe(include = [np.number]) #수치형만 == describe()


# %% 여러 통계량
df.sum() #합
df['sepal_length'].sum() #특정 column만 (아래도 동일)
df.count() #개수
df.median() #중앙값
df.min() #최소
df.max() #최대
df.mean() #평균
df.var() #분산
df.std() #표준편차
df['petal_width'].quantile([0.25,0.75]) #1,3분위수
df['species'].apply(lambda x: x[:3]) #함수를 적용한 값 --> 검색해보기

# %%
