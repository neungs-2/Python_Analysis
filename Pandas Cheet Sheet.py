#%%*********************** 10 minuates to Pandas ***********************

import pandas as pd
import numpy as np

#%% ****************** Syntax ******************
# DataFrame ??±
df = pd.DataFrame(
        {"a" : [4,5,6],
         "b" : [7,8,9],
         "c" : [10, 11, 12]},
        index = [1,2,3]           
)
df
#%% DataFrame?? ?΄?Ή row, column, κ°? λΆλ¬?€κΈ?
print(df[["a","c"]],'\n', df.loc[2],'\n')
print(df.loc[3,"a"],'\n')
print(df.loc[[1,2],['a','c']],'\n')

#%% ?¬?¬ κ°μ Indexκ°? ?? DataFrame ??±
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
# ?Ή?  κ°κ³Ό λΉκ΅? κ°λ§ κ°?? Έ?€? λ²?
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')
print(df['b']!=7,'\n')
print(df[df['b']!=7],'\n')

#%%μ€λ³΅? ?? ? κ±?
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

#%% isin() ?΄?Ήκ°μ΄ ?¬?¨ ?¬λΆ? T/F
#   isnull()/notnull() null ?¬λΆ? T/F
print(df.a.isin([5,6])) # a?΄? 5 ?? 6 ?¬?¨ ?¬λΆ?
print(df['a'].isin([5,6]),'\n') #κ°μ?? κ²°κ³Ό

print(pd.isnull(df))
print(df['b'].isnull())
print(df['b'].isnull().sum(),'\n') #null κ°? κ°μ

print(pd.notnull(df))
print(df.notnull().sum())

# and, or, not, xor, any, all  -->DataFrame?? ?¬?© λΆκ??
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

# %% '? κ·ν??'? ?΄?Ή?? ?΄λ§? κ°?? Έ?€κΈ?
print(df.filter(regex='_')) #_κ°? ?¬?¨
print(df.filter(regex='length$')) #lengthλ‘? ???
print(df.filter(regex='^sepal')) #sepalλ‘? ????
df.filter(regex='^(?!species).*') #(?!species)λ¬Έμκ°? ?€?΄κ°? κ²? λΉΌκ³  κ°?? Έ????Ό

# %% μ§??  ?°?΄?° λΆλ¬?€κΈ?
df.loc[2:4,'sepal_width':'petal_length'] #(a:b)?, (c:d)?΄ λΆλ¬?€κΈ?
df.iloc[-5:,[1,3]] #(a:b-1)?, (c,d-1)?΄ λΆλ¬?€κΈ?
# %% sepal_lengthκ°? 5λ³΄λ€ ?° ?°?΄?°? length, width ?΄? λΆλ¬?€κΈ?
df.loc[df.sepal_length > 5, ['sepal_length','sepal_width']]


# %%  ********************** Summarize Data **************************
df.shape #(?,?΄) κ°μ
len(df) #? κ°μ
df.head(3)

# %% Row μ’λ₯??? ?΄?Ή ?°?΄?° κ°μ *? ?©?¨
df['species'].value_counts()
df['sepal_length'].value_counts()
df['species'].nunique()   #Row μ’λ₯ ? 

# %% ?μΉν ?°?΄?° ?΅κ³κ°
df.describe()  #?μΉν ??λ©? ???΄
df.describe(include = 'all') # λͺ¨λ ??΄
df.describe(include = [np.object]) #λ²μ£Ό?(?)λ§?
df.describe(include = [np.number]) #?μΉνλ§? == describe()


# %% ?¬?¬ ?΅κ³λ
df.sum() #?©
df['sepal_length'].sum() #?Ή?  columnλ§? (??? ??Ό)
df.count() #κ°μ
df.median() #μ€μκ°?
df.min() #μ΅μ
df.max() #μ΅λ??
df.mean() #?κ·?
df.var() #λΆμ°
df.std() #?μ€??Έμ°?
df['petal_width'].quantile([0.25,0.75]) #1,3λΆμ?
df['species'].apply(lambda x: x[:3]) #?¨?λ₯? ? ?©? κ°? --> κ²???΄λ³΄κΈ°

# %% apply(function) 

print(df['species'].apply(lambda x: x[0])) #κ΄νΈ ?? ?¨? ?¬?©
df['species_3'] = df['species'].apply(lambda x: x[:3])
df
#%%
def smp(x):
        x = x[-3:] #?€?? 3λ²μ§ΈκΉμ??? λ¬Έμλ₯? κ°?? Έ?€? ?¨?
        return x

df['species-3'] = df['species'].apply(smp)
df


# %% ************************ Make New Columns ************************ 
# ?λ‘μ΄ column λ§λ€κΈ?
df = pd.DataFrame({'A':range(1,11),'B': np.random.randn(10)})
print(df)

df.assign(ln_A = lambda x: np.log(x.A) ) #?λ‘μ΄ column ??±
df['ln_A'] = np.log(df.A) #?? assign μ½λ? ??Ό? μ½λ

# %% ?«?? ?°?΄?°λ₯? μΉ΄νκ³ λ¦¬μ»? ?°?΄?°λ‘? --> λ²μ£Ό?
print(pd.qcut(range(5), 3, labels=["good","medium",'bad']))
pd.qcut(df.B,3,labels=['good','medium','bad'])
# %% ?/?΄ κΈ°μ?? μ΅λ??/μ΅μκ°? 
print(df.max(axis=1)) #row? μ΅λ??κ°?
print(df.max(axis=0)) #column? μ΅λ??κ°?
print(df.min(axis=1)) #row? μ΅μκ°?
print(df.min(axis=0)) #column? μ΅μκ°?

# %% ?κ³μΉλ₯? μ§?? ?΄? κ°μ μ§?? ?΄κΈ?
df['A'].clip(lower = -1, upper=5)

# %% ? ???κ°? ??°κΈ?
df['B'].abs()


# %% ********************* Reshaping Data *********************

# Value(κ°?)? ? ? ¬
print(df.sort_values('ln_A')) # Column? Row κ°λ€? ?€λ¦μ°¨? ? ? ¬
print(df.sort_values('ln_A',ascending =False)) # Column? Row κ°λ€? ?΄λ¦Όμ°¨? ? ? ¬
#%% ?΄λ¦? λ°κΎΈκΈ?
df = df.rename(columns = {'A2':'A1'}) # Column λͺ? λ°κΎΈκΈ?
df = df.rename(index = {0:12,2:47,4:99}) # Row λͺ? = index λ°κΎΈκΈ?
print(df)
#%% index(row_name)? ? ? ¬
df.sort_index()
#%% indexλ₯? Column? / ?Έ?±?€ μ΄κΈ°?
print(df.reset_index()) # indexλ₯? μ΄κΈ°?
df.reset_index(drop=True) #?Έ?±?€ μ΄κΈ°?
#%% Column ?­? 
df.drop(columns = ['A1'])

# %% *****Tidy Data

df = pd.DataFrame({'A':{0:'a',1:'b',2:'c'},
                   'B':{0:1, 1:3, 2:5},
                   'C':{0:2, 1:4, 2:6}
                   })

df
#%% Colmn? Row? ?μΌμ ?ΌμΉκΈ° -->melt()
pd.melt(df, id_vars=['A'], value_vars = ['B','C']) # A Column κΈ°μ???Όλ‘? Rowλ‘? ?ΌμΉκΈ°
#%%
pd.melt(df, value_vars = ['A','B','C'])
# %% λ³?κ²½ν ?°?΄?° ?΄λ¦? λ°κΎΈκΈ?
pd.melt(df, value_vars = ['A','B','C']).rename(columns = {'variable':'VAR','Value':'VAL'})

# %% melt? ?­ --> pivot()
df2 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                    'bar': ['A','B','C','A','B','C'],
                    'baz':[1, 2, 3, 4, 5, 6]
                    })
df2.pivot(index = 'foo', columns = 'bar', values = 'baz')
#%% index λ¦¬μ?? λ²?
df3 = df2.pivot(index = 'foo', columns = 'bar', values = 'baz').reset_index()
# %% melt ??©
df3.melt(id_vars=['foo'], value_vars=['A','B','C'])
# %% df3λ₯? foo??? barλ‘? ? ? ¬?κΈ?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar'])

# %% ?? ?°?΄?° μ»¬λΌ λͺ? λ°κΎΈκΈ?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar']).rename(columns = {'value':'baz'})

# %% concat? ??©? ?°?΄?° ?©μΉκΈ°

#?°?΄?° s1,s2??±
s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])
print(s1,'\n',s2)
# %% s1, s2 ?©μΉκΈ°
print(pd.concat([s1,s2], ignore_index=True))
print(pd.concat([s1,s2],keys = ['s1','s2'])) #key ??±
pd.concat([s1,s2],keys = ['s1','s2'], names = ['Series name','Row ID']) #column name λΆμ΄κΈ?

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
#%% df1κ³? df3 ?©μΉκΈ°
pd.concat([df1,df3])
#%% join ?΄? ?©μΉκΈ°
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

# %% μ€λ³΅? κ°?(index)κ°? ??μ§? κ²?μ¦ν? κ²?
pd.concat([df5, df6], verify_integrity=True)
# %% ??κ°? ?€λ₯? ? κ°μ dataframe ?©μΉκΈ°
pd.concat([df1,df3])
