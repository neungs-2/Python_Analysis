import pandas as pd

# DataFrame 생성
df = pd.DataFrame(
        {"a" : [4,5,6],
         "b" : [7,8,9],
         "c" : [10, 11, 12]},
        index = [1,2,3]           
)

# DataFrame에서 해당 row, column, 값 불러오기
print(df[["a","c"]],'\n', df.loc[2],'\n')
print(df.loc[3,"a"],'\n')
print(df.loc[[1,2],['a','c']],'\n')

# 여러 개의 Index가 있는 DataFrame 생성
df = pd.DataFrame(
        {'a': [4,5,6,6],
         'b': [7,8,9,9],
         'c': [10,11,12,12]},
        index = pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2),('e',3)],
            names=['n', 'v']
        )
)

print(df,'\n')

#특정 값과 비교한 값만 가져오는 법
print(df[df.a <= 5],'\n')
print(df[df['b'] <= 8],'\n')

#중복된 행을 제거
df = df.drop_duplicates()
print(df)