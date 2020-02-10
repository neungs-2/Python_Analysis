#%%*********************** 10 minuates to Pandas ***********************

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
df
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


#%% *************************  Subset  *************************
# 특정 값과 비교한 값만 가져오는 법
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')
print(df['b']!=7,'\n')
print(df[df['b']!=7],'\n')

#%%중복된 행을 제거
df = df.drop_duplicates()
print(df)
#%%
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


# %%  ********************** Summarize Data **************************
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

# %% apply(function) 

print(df['species'].apply(lambda x: x[0])) #괄호 안에 함수 사용
df['species_3'] = df['species'].apply(lambda x: x[:3])
df
#%%
def smp(x):
        x = x[-3:] #뒤에서 3번째까지의 문자를 가져오는 함수
        return x

df['species-3'] = df['species'].apply(smp)
df


# %% ************************ Make New Columns ************************ 
# 새로운 column 만들기
df = pd.DataFrame({'A':range(1,11),'B': np.random.randn(10)})
print(df)

df.assign(ln_A = lambda x: np.log(x.A) ) #새로운 column 생성
df['ln_A'] = np.log(df.A) #위의 assign 코드랑 동일한 코드

# %% 숫자형 데이터를 카테고리컬 데이터로 --> 범주화
print(pd.qcut(range(5), 3, labels=["good","medium",'bad']))
pd.qcut(df.B,3,labels=['good','medium','bad'])
# %% 행/열 기준 최대/최소값 
print(df.max(axis=1)) #row의 최대값
print(df.max(axis=0)) #column의 최대값
print(df.min(axis=1)) #row의 최소값
print(df.min(axis=0)) #column의 최소값

# %% 임계치를 지정해서 값을 지정해기
df['A'].clip(lower = -1, upper=5)

# %% 절대값 씌우기
df['B'].abs()


# %% ********************* Reshaping Data *********************

# Value(값)을 정렬
print(df.sort_values('ln_A')) # Column의 Row 값들을 오름차순 정렬
print(df.sort_values('ln_A',ascending =False)) # Column의 Row 값들을 내림차순 정렬
#%% 이름 바꾸기
df = df.rename(columns = {'A2':'A1'}) # Column 명 바꾸기
df = df.rename(index = {0:12,2:47,4:99}) # Row 명 = index 바꾸기
print(df)
#%% index(row_name)을 정렬
df.sort_index()
#%% index를 Column화 / 인덱스 초기화
print(df.reset_index()) # index를 초기화
df.reset_index(drop=True) #인덱스 초기화
#%% Column 삭제
df.drop(columns = ['A1'])

# %% *****Tidy Data

df = pd.DataFrame({'A':{0:'a',1:'b',2:'c'},
                   'B':{0:1, 1:3, 2:5},
                   'C':{0:2, 1:4, 2:6}
                   })

df
#%% Colmn을 Row화 시켜서 펼치기 -->melt()
pd.melt(df, id_vars=['A'], value_vars = ['B','C']) # A Column 기준으로 Row로 펼치기
#%%
pd.melt(df, value_vars = ['A','B','C'])
# %% 변경한 데이터 이름 바꾸기
pd.melt(df, value_vars = ['A','B','C']).rename(columns = {'variable':'VAR','Value':'VAL'})

# %% melt의 역 --> pivot()
df2 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                    'bar': ['A','B','C','A','B','C'],
                    'baz':[1, 2, 3, 4, 5, 6]
                    })
df2.pivot(index = 'foo', columns = 'bar', values = 'baz')
#%% index 리셋하는 법
df3 = df2.pivot(index = 'foo', columns = 'bar', values = 'baz').reset_index()
# %% melt 활용
df3.melt(id_vars=['foo'], value_vars=['A','B','C'])
# %% df3를 foo와 bar로 정렬하기
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar'])

# %% 위의 데이터 컬럼 명 바꾸기
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar']).rename(columns = {'value':'baz'})

# %% concat을 활용한 데이터 합치기

#데이터 s1,s2생성
s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])
print(s1,'\n',s2)
# %% s1, s2 합치기
print(pd.concat([s1,s2], ignore_index=True))
print(pd.concat([s1,s2],keys = ['s1','s2'])) #key 생성
pd.concat([s1,s2],keys = ['s1','s2'], names = ['Series name','Row ID']) #column name 붙이기

# %%
df1 = pd.DataFrame([['a',1],['b',2]],
                   columns=['letter', 'number'])

df2 = pd.DataFrame([['c',3],['d',4]],
                   columns=['letter', 'number'])
# %%
pd.concat([df1, df2])
# %%
df3 = pd.DataFrame([['c',3,'cat'],['d',4,'dog']],
                   columns=['letter', 'number','animal'])
df3
#%% df1과 df3 합치기
pd.concat([df1,df3])
#%% join 해서 합치기
df3 = pd.DataFrame([['c',3,'cat'],['d',4,'dof']], columns = ['letter','number','animal'])
print(df3)
pd.concat([df1,df3], join='inner')

# %%
df4 = pd.DataFrame([['bird','polly'],['monkey','george']], columns = ['animal','name'])
df5 = pd.DataFrame([1], index=['a'])
df6 = pd.DataFrame([2], index=['a'])
print(df4,'\n')
print(df5,'\n')
print(df6)

# %% 중복된 값(index)가 있는지 검증하는 것
pd.concat([df5, df6], verify_integrity=True)
# %% 형태가 다른 두 개의 dataframe 합치기
pd.concat([df1,df3])
