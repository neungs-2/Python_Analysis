
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
df_seoul = shop_2019[shop_2019['시도명'] == '서울특별시']
#%%
df_31 = df_seoul[df_seoul['상호명'].str.contains('배스킨|던킨')].copy()
df_31
# %%
df_31 = df_31[['상호명','지점명','상권업종대분류명','상권업종중분류명','지번주소','도로명주소',
                '위도', '경도', '시군구명', '행정동명']].copy() #원본 데이터 참조 시 데이터 변경 위험으로 사본 만듬
df_31.columns
# %%
df_31['상호명'].value_counts()

# %%
df_31['브랜드명'] = '' #브랜드명이라는 column 생성
df_31[['상호명','브랜드명']].head()

# %%
df_31.loc[df_31['상호명'].str.contains('배스킨'),'브랜드명'] = '배스킨라빈스'
df_31.loc[df_31['상호명'].str.contains('던킨'), '브랜드명'] = '던킨도너츠'
df_31[['상호명','브랜드명']].head()

# %%
df_31_group_count = df_31['브랜드명'].value_counts()
df_31_group_count

# %%
df_31_ratio = df_31_group_count[0]/df_31_group_count[1]
print('제공된 데이터에서 서울 지역에는 배스킨라빈스/던킨도너츠 의 비율은 {0: 2f} 입니다.'.format(df_31_ratio))

# %%
df_31.info()

# %%
df_31['위도'] = df_31['위도'].astype(float)
df_31['경도'] = df_31['경도'].astype(float)
#pandas로 산점도
df_31.plot.scatter(x='경도',y='위도')

# %%
# seaborn으로 산점도
sns.scatterplot(data=df_31, x='경도', y='위도', hue='브랜드명')

# %%
#Folium 사용 예제
geo_df = df_31.copy()

#지도 초기화 시 중심점 설정
#데이터 중심점 설정을 위해 위/경도 평균값 구하기
map = folium.Map(location=[geo_df['위도'].mean(), geo_df['경도'].mean()],zoom_start= 12)

for n in geo_df.index:
    #팝업에 들어갈 텍스트 지정
    popup_name = geo_df.loc[n, '브랜드명'] + ' - '+ geo_df.loc[n,'도로명주소']
    #브랜드명에 따라 아이콘 색상 지정
    if geo_df['브랜드명'][n] == '던킨도너츠': 
        icon_color = 'pink'
    else:
        icon_color = 'blue'

    folium.Marker([geo_df.loc[n,'위도'], geo_df.loc[n, '경도']],
                  popup = popup_name, 
                  icon= folium.Icon(color=icon_color)).add_to(map)

map

# %%
map = folium.Map(location=[geo_df['위도'].mean(), geo_df['경도'].mean()], zoom_start= 12, tiles= 'Stamen Toner')

for n in geo_df.index:
    #팝업에 들어갈 테스트 지정
    popup_name = geo_df['브랜드명'][n] + ' - ' + geo_df['도로명주소'][n]
    # 브랜드명에 따라 아이콘 색상을 달리해서 찍어줍니다.
    if geo_df['브랜드명'][n] == '던킨도너츠' :
        icon_color = 'red'
    else:
        icon_color = 'blue'    
    
    # folium.features.CircleMarker 오류가 날 경우 --> folium.vector_layer.CircleMarker
    folium.CircleMarker(
        location=[geo_df['위도'][n], geo_df['경도'][n]],
        radius=3,
        popup=popup_name,
        color= icon_color,
        fill=True,
        fill_color=icon_color
    ).add_to(map)


map

# %%
