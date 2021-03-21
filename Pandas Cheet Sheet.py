#%%*********************** 10 minuates to Pandas ***********************

import pandas as pd
import numpy as np

#%% ****************** Syntax ******************
# DataFrame ?ƒ?„±
df = pd.DataFrame(
        {"a" : [4,5,6],
         "b" : [7,8,9],
         "c" : [10, 11, 12]},
        index = [1,2,3]           
)
df
#%% DataFrame?—?„œ ?•´?‹¹ row, column, ê°? ë¶ˆëŸ¬?˜¤ê¸?
print(df[["a","c"]],'\n', df.loc[2],'\n')
print(df.loc[3,"a"],'\n')
print(df.loc[[1,2],['a','c']],'\n')

#%% ?—¬?Ÿ¬ ê°œì˜ Indexê°? ?ˆ?Š” DataFrame ?ƒ?„±
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
# ?Š¹? • ê°’ê³¼ ë¹„êµ?•œ ê°’ë§Œ ê°?? ¸?˜¤?Š” ë²?
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')
print(df['b']!=7,'\n')
print(df[df['b']!=7],'\n')

#%%ì¤‘ë³µ?œ ?–‰?„ ? œê±?
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

#%% isin() ?•´?‹¹ê°’ì´ ?¬?•¨ ?—¬ë¶? T/F
#   isnull()/notnull() null ?—¬ë¶? T/F
print(df.a.isin([5,6])) # a?—´?— 5 ?˜?Š” 6 ?¬?•¨ ?—¬ë¶?
print(df['a'].isin([5,6]),'\n') #ê°™ì?? ê²°ê³¼

print(pd.isnull(df))
print(df['b'].isnull())
print(df['b'].isnull().sum(),'\n') #null ê°? ê°œìˆ˜

print(pd.notnull(df))
print(df.notnull().sum())

# and, or, not, xor, any, all  -->DataFrame?—?„œ ?‚¬?š© ë¶ˆê??
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

# %% '? •ê·œí‘œ?˜„?‹'?— ?•´?‹¹?˜?Š” ?—´ë§? ê°?? ¸?˜¤ê¸?
print(df.filter(regex='_')) #_ê°? ?¬?•¨
print(df.filter(regex='length$')) #lengthë¡? ??‚˜?Š”
print(df.filter(regex='^sepal')) #sepalë¡? ?‹œ?‘?•˜?Š”
df.filter(regex='^(?!species).*') #(?!species)ë¬¸ìê°? ?“¤?–´ê°? ê²? ë¹¼ê³  ê°?? ¸????¼

# %% ì§?? • ?°?´?„° ë¶ˆëŸ¬?˜¤ê¸?
df.loc[2:4,'sepal_width':'petal_length'] #(a:b)?–‰, (c:d)?—´ ë¶ˆëŸ¬?˜¤ê¸?
df.iloc[-5:,[1,3]] #(a:b-1)?–‰, (c,d-1)?—´ ë¶ˆëŸ¬?˜¤ê¸?
# %% sepal_lengthê°? 5ë³´ë‹¤ ?° ?°?´?„°?˜ length, width ?—´?„ ë¶ˆëŸ¬?˜¤ê¸?
df.loc[df.sepal_length > 5, ['sepal_length','sepal_width']]


# %%  ********************** Summarize Data **************************
df.shape #(?–‰,?—´) ê°œìˆ˜
len(df) #?–‰ ê°œìˆ˜
df.head(3)

# %% Row ì¢…ë¥˜??? ?•´?‹¹ ?°?´?„° ê°œìˆ˜ *?œ ?š©?•¨
df['species'].value_counts()
df['sepal_length'].value_counts()
df['species'].nunique()   #Row ì¢…ë¥˜ ?ˆ˜ 

# %% ?ˆ˜ì¹˜í˜• ?°?´?„° ?†µê³„ê°’
df.describe()  #?ˆ˜ì¹˜í˜• ?•„?‹ˆë©? ?•ˆ?‚˜?˜´
df.describe(include = 'all') # ëª¨ë‘ ?‚˜?˜´
df.describe(include = [np.object]) #ë²”ì£¼?˜•(?)ë§?
df.describe(include = [np.number]) #?ˆ˜ì¹˜í˜•ë§? == describe()


# %% ?—¬?Ÿ¬ ?†µê³„ëŸ‰
df.sum() #?•©
df['sepal_length'].sum() #?Š¹? • columnë§? (?•„?˜?„ ?™?¼)
df.count() #ê°œìˆ˜
df.median() #ì¤‘ì•™ê°?
df.min() #ìµœì†Œ
df.max() #ìµœë??
df.mean() #?‰ê·?
df.var() #ë¶„ì‚°
df.std() #?‘œì¤??¸ì°?
df['petal_width'].quantile([0.25,0.75]) #1,3ë¶„ìœ„?ˆ˜
df['species'].apply(lambda x: x[:3]) #?•¨?ˆ˜ë¥? ? ?š©?•œ ê°? --> ê²??ƒ‰?•´ë³´ê¸°

# %% apply(function) 

print(df['species'].apply(lambda x: x[0])) #ê´„í˜¸ ?•ˆ?— ?•¨?ˆ˜ ?‚¬?š©
df['species_3'] = df['species'].apply(lambda x: x[:3])
df
#%%
def smp(x):
        x = x[-3:] #?’¤?—?„œ 3ë²ˆì§¸ê¹Œì???˜ ë¬¸ìë¥? ê°?? ¸?˜¤?Š” ?•¨?ˆ˜
        return x

df['species-3'] = df['species'].apply(smp)
df


# %% ************************ Make New Columns ************************ 
# ?ƒˆë¡œìš´ column ë§Œë“¤ê¸?
df = pd.DataFrame({'A':range(1,11),'B': np.random.randn(10)})
print(df)

df.assign(ln_A = lambda x: np.log(x.A) ) #?ƒˆë¡œìš´ column ?ƒ?„±
df['ln_A'] = np.log(df.A) #?œ„?˜ assign ì½”ë“œ?‘ ?™?¼?•œ ì½”ë“œ

# %% ?ˆ«??˜• ?°?´?„°ë¥? ì¹´í…Œê³ ë¦¬ì»? ?°?´?„°ë¡? --> ë²”ì£¼?™”
print(pd.qcut(range(5), 3, labels=["good","medium",'bad']))
pd.qcut(df.B,3,labels=['good','medium','bad'])
# %% ?–‰/?—´ ê¸°ì?? ìµœë??/ìµœì†Œê°? 
print(df.max(axis=1)) #row?˜ ìµœë??ê°?
print(df.max(axis=0)) #column?˜ ìµœë??ê°?
print(df.min(axis=1)) #row?˜ ìµœì†Œê°?
print(df.min(axis=0)) #column?˜ ìµœì†Œê°?

# %% ?„ê³„ì¹˜ë¥? ì§?? •?•´?„œ ê°’ì„ ì§?? •?•´ê¸?
df['A'].clip(lower = -1, upper=5)

# %% ? ˆ???ê°? ?”Œ?š°ê¸?
df['B'].abs()


# %% ********************* Reshaping Data *********************

# Value(ê°?)?„ ? •? ¬
print(df.sort_values('ln_A')) # Column?˜ Row ê°’ë“¤?„ ?˜¤ë¦„ì°¨?ˆœ ? •? ¬
print(df.sort_values('ln_A',ascending =False)) # Column?˜ Row ê°’ë“¤?„ ?‚´ë¦¼ì°¨?ˆœ ? •? ¬
#%% ?´ë¦? ë°”ê¾¸ê¸?
df = df.rename(columns = {'A2':'A1'}) # Column ëª? ë°”ê¾¸ê¸?
df = df.rename(index = {0:12,2:47,4:99}) # Row ëª? = index ë°”ê¾¸ê¸?
print(df)
#%% index(row_name)?„ ? •? ¬
df.sort_index()
#%% indexë¥? Column?™” / ?¸?±?Š¤ ì´ˆê¸°?™”
print(df.reset_index()) # indexë¥? ì´ˆê¸°?™”
df.reset_index(drop=True) #?¸?±?Š¤ ì´ˆê¸°?™”
#%% Column ?‚­? œ
df.drop(columns = ['A1'])

# %% *****Tidy Data

df = pd.DataFrame({'A':{0:'a',1:'b',2:'c'},
                   'B':{0:1, 1:3, 2:5},
                   'C':{0:2, 1:4, 2:6}
                   })

df
#%% Colmn?„ Row?™” ?‹œì¼œì„œ ?¼ì¹˜ê¸° -->melt()
pd.melt(df, id_vars=['A'], value_vars = ['B','C']) # A Column ê¸°ì???œ¼ë¡? Rowë¡? ?¼ì¹˜ê¸°
#%%
pd.melt(df, value_vars = ['A','B','C'])
# %% ë³?ê²½í•œ ?°?´?„° ?´ë¦? ë°”ê¾¸ê¸?
pd.melt(df, value_vars = ['A','B','C']).rename(columns = {'variable':'VAR','Value':'VAL'})

# %% melt?˜ ?—­ --> pivot()
df2 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                    'bar': ['A','B','C','A','B','C'],
                    'baz':[1, 2, 3, 4, 5, 6]
                    })
df2.pivot(index = 'foo', columns = 'bar', values = 'baz')
#%% index ë¦¬ì…‹?•˜?Š” ë²?
df3 = df2.pivot(index = 'foo', columns = 'bar', values = 'baz').reset_index()
# %% melt ?™œ?š©
df3.melt(id_vars=['foo'], value_vars=['A','B','C'])
# %% df3ë¥? foo??? barë¡? ? •? ¬?•˜ê¸?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar'])

# %% ?œ„?˜ ?°?´?„° ì»¬ëŸ¼ ëª? ë°”ê¾¸ê¸?
df3.melt(id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo','bar']).rename(columns = {'value':'baz'})

# %% concat?„ ?™œ?š©?•œ ?°?´?„° ?•©ì¹˜ê¸°

#?°?´?„° s1,s2?ƒ?„±
s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])
print(s1,'\n',s2)
# %% s1, s2 ?•©ì¹˜ê¸°
print(pd.concat([s1,s2], ignore_index=True))
print(pd.concat([s1,s2],keys = ['s1','s2'])) #key ?ƒ?„±
pd.concat([s1,s2],keys = ['s1','s2'], names = ['Series name','Row ID']) #column name ë¶™ì´ê¸?

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
#%% df1ê³? df3 ?•©ì¹˜ê¸°
pd.concat([df1,df3])
#%% join ?•´?„œ ?•©ì¹˜ê¸°
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

# %% ì¤‘ë³µ?œ ê°?(index)ê°? ?ˆ?Š”ì§? ê²?ì¦í•˜?Š” ê²?
pd.concat([df5, df6], verify_integrity=True)
# %% ?˜•?ƒœê°? ?‹¤ë¥? ?‘ ê°œì˜ dataframe ?•©ì¹˜ê¸°
pd.concat([df1,df3])
