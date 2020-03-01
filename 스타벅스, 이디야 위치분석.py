#%%
import pandas as pd
import numpy as np
import seaborn as sns
import folium

%matplotlib inline # 노트북 안에서 그래프를 표시하기 위해
#%%
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

plt.rc('font', family= 'Malgun Gothic') #window의 한글폰트 설정
plt.rc('axes', unicode_minus= False)

set_matplotlib_formats('retina')

#%%
shop_2019 = pd.read_csv('C:/Users/gnlee/Desktop/상가(상권)정보_201912/상권데이터.csv', encoding = 'UTF-8')
df_seoul = shop_2019[shop_2019['시도명'] == '서울특별시']
# %%
df_seoul[df_seoul['상호명'].str.contains('스타벅스|starbucks|STARBUCKS')]
# %%
df_seoul[df_seoul['상호명'].str.contains('이디야|ediya|EDIYA')]

# %% 스타벅스, 이디야 매장 데이터 생성
df_cafe = df_seoul[df_seoul['상호명'].str.contains('스타벅스|starbucks|STARBUCKS|이디야|ediya|EDIYA')]
df_cafe.loc[df_cafe['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'),'상호명'].value_counts()

# %% 브랜드명 컬럼 만들기
df_cafe.loc[df_cafe['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'),'브랜드명'] = '스타벅스'
df_cafe.loc[~df_cafe['상호명'].str.contains('스타벅스|starbucks|STARBUCKS'),'브랜드명'] = '이디야'
df_cafe[['상호명','브랜드명']]
# %% 브랜드명이 null인 데이터 있는지 확인
df_cafe.loc[df_cafe['브랜드명'].isnull(),'상호명']

# %%
df_cafe['브랜드명'].value_counts()

#%% 산점도 찍어보기
df_cafe.plot.scatter(x='경도', y='위도')
#%% 산점도 찍어보기
sns.scatterplot(data= df_cafe,x='경도',y='위도')
# %% folium으로 지도에 위치 찍기
geo_df = df_cafe.copy()

map = folium.Map(location=[geo_df['위도'].mean(), geo_df['경도'].mean()], zoom_start=12, tiles='Stamen Toner')

for n in geo_df.index:
    #팝업에 들어갈 텍스트를 지정
    popup_name = geo_df.loc[n, '상호명'] + ' - ' + geo_df.loc[n, '도로명주소']
    #브랜드명에 따라 아이콘 색상을 달리해서 찍어줍니다.
    if geo_df.loc[n,'브랜드명'] == '스타벅스':
        icon_color = 'green'
    else:
        icon_color = 'blue'

    folium.features.CircleMarker(
        location = [geo_df.loc[n,'위도'], geo_df.loc[n,'경도']],
        radius=3,
        popup = popup_name,
        color = icon_color,
        fill = True,
        fill_color = icon_color
    ).add_to(map)

map
# %%
