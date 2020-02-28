#%%
import warnings
warnings.filterwarnings('ignore') #warning 메시지 제거
warnings.filterwarnings('ignore', 'This pattern has match groups')
warnings.filterwarnings('ignore', 'The iterable function was deprected in Matplotlib')

#%%
import pandas as pd
import numpy as np
import seaborn as sns
import folium

%matplotlib inline # 노트북 안에서 그래프를 표시하기 위해

#%%
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

plt.rc('font',family='Malgun Gothic') # Window의 한글 폰트 설정
plt.rc('axes', unicode_minus=False)

set_matplotlib_formats('retina')

# %%
shop_2019 = pd.read_csv('C:/Users/gnlee/Desktop/상가(상권)정보_201912/상권데이터.csv', encoding = 'UTF-8')
shop_2019.head()
# %%
shop_2019.shape

# %%
coffee = shop_2019[shop_2019['상권업종소분류명'].str.contains('커피')]
coffee.shape
# %%
coffee.columns
# %%
print(coffee['상호명'].unique().shape)
coffee.loc[coffee['상호명'].str.contains('스타벅스'), '상호명'].unique()
# %%
print(coffee['시도명'].isnull().sum())
# %%
print(coffee['시도명'].value_counts())
coffee['시군구명'].unique()
# %%
coffee['상권업종중분류명'].value_counts()

# %%
shop_2019[:1000].plot.scatter(x='경도', y='위도', grid= 'True')

# %%
df_seoul = shop_2019.loc[shop_2019['시도명'].str.startswith('서울')].copy()
df_seoul['상권업종대분류명'].value_counts()
# %%
df_seoul.describe(include= np.object)
# %%
df_seoul[['위도','경도']].describe(include= np.number)

# %%
sns.countplot(data= df_seoul, y='상권업종대분류명')
# %%
df_food = df_seoul.loc[df_seoul['상권업종대분류명'].str.contains('음식')]
df_food
# %% #궁금해서 해봤는데 위에 코드랑 같은 결과
df_food = df_seoul[df_seoul['상권업종대분류명'].str.contains('음식')]
df_food

# %%
sns.countplot(data= df_food, y='상권업종중분류명')

# %%
df_fast_food = df_food[df_food['상권업종중분류명'] == '패스트푸드']
print(df_fast_food.shape)
df_fast_food['상호명'].unique()
# %%
