#%%*********************** 10 minuates to Pandas ***********************

import pandas as pd
import numpy as np

#%% ****************** Syntax ******************
# DataFrame ?��?��
df = pd.DataFrame(
        {"a" : [4,5,6],
         "b" : [7,8,9],
         "c" : [10, 11, 12]},
        index = [1,2,3]           
)
df
#%% DataFrame?��?�� ?��?�� row, column, �? 불러?���?
print(df[["a","c"]],'\n', df.loc[2],'\n')
print(df.loc[3,"a"],'\n')
print(df.loc[[1,2],['a','c']],'\n')

#%% ?��?�� 개의 Index�? ?��?�� DataFrame ?��?��
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
# ?��?�� 값과 비교?�� 값만 �??��?��?�� �?
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')
print(df['b']!=7,'\n')
print(df[df['b']!=7],'\n')

#%%중복?�� ?��?�� ?���?
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

#%% isin() ?��?��값이 ?��?�� ?���? T/F
#   isnull()/notnull() null ?���? T/F
print(df.a.isin([5,6])) # a?��?�� 5 ?��?�� 6 ?��?�� ?���?
print(df['a'].isin([5,6]),'\n') #같�?? 결과

print(pd.isnull(df))
print(df['b'].isnull())
print(df['b'].isnull().sum(),'\n') #null �? 개수

print(pd.notnull(df))
print(df.notnull().sum())

# and, or, not, xor, any, all  -->DataFrame?��?�� ?��?�� 불�??
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

# %% '?��규표?��?��'?�� ?��?��?��?�� ?���? �??��?���?
print(df.filter(regex='_')) #_�? ?��?��
print(df.filter(regex='length$')) #length�? ?��?��?��
print(df.filter(regex='^sepal')) #sepal�? ?��?��?��?��
df.filter(regex='^(?!species).*') #(?!species)문자�? ?��?���? �? 빼고 �??��????��

# %% �??�� ?��?��?�� 불러?���?
df.loc[2:4,'sepal_width':'petal_length'] #(a:b)?��, (c:d)?�� 불러?���?
df.iloc[-5:,[1,3]] #(a:b-1)?��, (c,d-1)?�� 불러?���?
# %% sepal_length�? 5보다 ?�� ?��?��?��?�� length, width ?��?�� 불러?���?
df.loc[df.sepal_length > 5, ['sepal_length','sepal_width']]


# %%  ********************** Summarize Data **************************
df.shape #(?��,?��) 개수
len(df) #?�� 개수
df.head(3)

# %% Row 종류??? ?��?�� ?��?��?�� 개수 *?��?��?��
df['species'].value_counts()
df['sepal_length'].value_counts()
df['species'].nunique()   #Row 종류 ?�� 

# %% ?��치형 ?��?��?�� ?��계값
df.describe()  #?��치형 ?��?���? ?��?��?��
df.describe(include = 'all') # 모두 ?��?��
df.describe(include = [np.object]) #범주?��(?)�?
df.describe(include = [np.number]) #?��치형�? == describe()


# %% ?��?�� ?��계량
df.sum() #?��
df['sepal_length'].sum() #?��?�� column�? (?��?��?�� ?��?��)
df.count() #개수
df.median() #중앙�?
df.min() #최소
df.max() #최�??
df.mean() #?���?
df.var() #분산
df.std() #?���??���?
df['petal_width'].quantile([0.25,0.75]) #1,3분위?��
df['species'].apply(lambda x: x[:3]) #?��?���? ?��?��?�� �? --> �??��?��보기

# %% apply(function) 

print(df['species'].apply(lambda x: x[0])) #괄호 ?��?�� ?��?�� ?��?��
df['species_3'] = df['species'].apply(lambda x: x[:3])
df
#%%
def smp(x):
        x = x[-3:] #?��?��?�� 3번째까�???�� 문자�? �??��?��?�� ?��?��
        return x

df['species-3'] = df['species'].apply(smp)
df


# %% ************************ Make New Columns ************************ 
# ?��로운 column 만들�?
df = pd.DataFrame({'A':range(1,11),'B': np.random.randn(10)})
print(df)

df.assign(ln_A = lambda x: np.log(x.A) ) #?��로운 column ?��?��
df['ln_A'] = np.log(df.A) #?��?�� assign 코드?�� ?��?��?�� 코드

# %% ?��?��?�� ?��?��?���? 카테고리�? ?��?��?���? --> 범주?��
print(pd.qcut(range(5), 3, labels=["good","medium",'bad']))
pd.qcut(df.B,3,labels=['good','medium','bad'])
# %% ?��/?�� 기�?? 최�??/최소�? 
print(df.max(axis=1)) #row?�� 최�??�?
print(df.max(axis=0)) #column?�� 최�??�?
print(df.min(axis=1)) #row?�� 최소�?
print(df.min(axis=0)) #column?�� 최소�?

# %% ?��계치�? �??��?��?�� 값을 �??��?���?
df['A'].clip(lower = -1, upper=5)

# %% ?��???�? ?��?���?
df['B'].abs()


# %% ********************* Reshaping Data *********************

# Value(�?)?�� ?��?��
print(df.sort_values('ln_A')) # Column?�� Row 값들?�� ?��름차?�� ?��?��
print(df.sort_values('ln_A',ascending =False)) # Column?�� Row 값들?�� ?��림차?�� ?��?��
#%% ?���? 바꾸�?
df = df.rename(columns = {'A2':'A1'}) # Column �? 바꾸�?
df = df.rename(index = {0:12,2:47,4:99}) # Row �? = index 바꾸�?
print(df)
#%% index(row_name)?�� ?��?��
df.sort_index()
#%% index�? Column?�� / ?��?��?�� 초기?��
print(df.reset_index()) # index�? 초기?��
df.reset_index(drop=True) #?��?��?�� 초기?��
#%% Column ?��?��
df.drop(columns = ['A1'])

# %% *****Tidy Data

df = pd.DataFrame({'A':{0:'a',1:'b',2:'c'},
                   'B':{0:1, 1:3, 2:5},
                   'C':{0:2, 1:4, 2:6}
                   })

df
#%% Colmn?�� Row?�� ?��켜서 ?��치기 -->melt()
pd.melt(df, id_vars=['A'], value_vars = ['B','C']) # A Column 기�???���? Row�? ?��치기
#%%
pd.melt(df, value_vars = ['A','B','C'])
# %% �?경한 ?��?��?�� ?���? 바꾸�?
pd.melt(df, value_vars = ['A','B','C']).rename(columns = {'variable':'VAR','Value':'VAL'})

# %% melt?�� ?�� --> pivot()
df2 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                    'bar': ['A','B','C','A','B','C'],
                    'baz':[1, 2, 3, 4, 5, 6]
                    })
df2.pivot(index = 'foo', columns = 'bar', values = 'baz')
#%% index 리셋?��?�� �?
df3 = df2.pivot(index = 'foo', columns = 'bar', values = 'baz').reset_index()
# %% melt ?��?��
df3.melt(id_vars=['foo'], value_vars=['A','B','C'])
# %% df3�? foo??? bar�? ?��?��?���?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar'])

# %% ?��?�� ?��?��?�� 컬럼 �? 바꾸�?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar']).rename(columns = {'value':'baz'})

# %% concat?�� ?��?��?�� ?��?��?�� ?��치기

#?��?��?�� s1,s2?��?��
s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])
print(s1,'\n',s2)
# %% s1, s2 ?��치기
print(pd.concat([s1,s2], ignore_index=True))
print(pd.concat([s1,s2],keys = ['s1','s2'])) #key ?��?��
pd.concat([s1,s2],keys = ['s1','s2'], names = ['Series name','Row ID']) #column name 붙이�?

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
#%% df1�? df3 ?��치기
pd.concat([df1,df3])
#%% join ?��?�� ?��치기
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

# %% 중복?�� �?(index)�? ?��?���? �?증하?�� �?
pd.concat([df5, df6], verify_integrity=True)
# %% ?��?���? ?���? ?�� 개의 dataframe ?��치기
pd.concat([df1,df3])
