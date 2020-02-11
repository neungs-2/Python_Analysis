#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 그래프의 스타일을 지정
plt.style.use('ggplot')

import matplotlib as mpl
mpl.rcParams.update({'font.size':14})

# window의 한글 폰트 설정
plt.rc('font', family = 'Malgun Gothic')

#주피터 노트북 안에서 그래프가 표시되도록 함
%matplotlib inline

# %% 데이터 로드
df = pd.read_csv('suggestion.csv')
df.shape

# %% 데이터 미리보기
df.head()
df.tail(1)
# %% 요약
df.info()
# %%
print(df.describe(include = 'all'))
print('\n',df.describe())
# %%
df['category'].value_counts()

# %% ******************그래프 그리기
#plot 설정
figure,(ax1,ax2) = plt.subplots(1,2)
figure.set_size_inches(20,10)
#카테고리별 제안 수 
sns.countplot(data=df, y='category', ax = ax1)
#카테고리별 평균 투표 수 
sns.barplot(data= df, x = 'vote', y= 'category', ax= ax2)

# %% 
df_vote_200 = df[df['vote'] < 2 ]
df_vote_200
#%%
df.groupby( ['category'] )['vote'].sum().reset_index(
    ).sort_values('vote', ascending= False)

# %% 카테고리별 전체 투표수
df_category_vote = pd.DataFrame(df.groupby(['category'])['vote'].sum()).reset_index().sort_values('vote',ascending= False)
df_category_vote.head()

# %% *************************************기간
# 데이터를 날짜데이터로 치환
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

df[['start','end']].head()

# %% 잘 치환됐는지 확인
df.dtypes
# %%
df['start-date'] = df['start'].dt.date
df['start-month'] = df['start'].dt.year.astype(str)+'-'+df['start'].dt.month.astype(str)
df['start-weekday'] = df['start'].dt.dayofweek
# %%
df[['start-date', 'start-month','start-weekday']].head()

# %%
weekday = {0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
df['weekday'] = df['start-weekday'].map(weekday)
df[['start-month','start-weekday','weekday']]

# %% countplot 그리기
plt.figure(figsize=(20,5))
plt.title('월별 제안 수')
sns.countplot(data=df.sort_values(by='start-date', ascending=True), x = 'start-month')


#%% pointplot 그리기
#point는 평균, 직선은 편차(신뢰구간)
plt.figure(figsize=(20,5))
plt.title('월별 투표 수(제안일 기준)')
sns.pointplot(data=df.sort_values(by='start-date',ascending=True), x='start-month', y='vote')

# %% barplot 그리기
plt.figure(figsize=(20, 5))
plt.title('월별 투표 수(날짜는 제안일 기준)')
sns.barplot(data=df.sort_values(by= 'start-date', ascending= True), x = 'start-month', y='vote')


#%% 
plt.figure(figsize=(20,5))
plt.title('요일별 제안 수')
sns.countplot(data=df.sort_values(by="start-weekday"), x="weekday")

#%% 
plt.figure(figsize=(20,5))
plt.title('요일별 투표 수(제안일 기준)')
sns.barplot(data=df.sort_values(by="start-weekday"), x="weekday", y="vote")

#%% 일자별 Countplot
plt.figure(figsize=(20,5))
plt.title('일자별 제안 수')
plt.xticks(rotation=60, ha='right')
sns.countplot(data=df.sort_values(by="start-date"), x="start-date")


#%%
df_06_10 = df[df['start'] > '2019-06-10']
df_06_10['start-date'].value_counts()

#%%
plt.figure(figsize=(20,5)) #plot size
plt.xticks(rotation=60, ha='right') #rotate: 공간이 없을때 글자를 기울여서 표시, 
plt.title('일자별 투표수(제안일 기준)')
sns.pointplot(data= df.sort_values(by='start-date'), x = 'start-date', y = 'vote')


# %% 2018년 10월만 나타낸 그래프
plt.figure(figsize=(20,5))
plt.xticks(rotation = 60, ha = 'right')
plt.title('2018년 10월 일자별 투표 수 (제안일 기준)')
df_2018_10 = df[(df['start']>= '2018-10-01') & (df['start'] < '2018-11-01')]
sns.pointplot(data = df_2018_10.sort_values(by='start-date'), x='start-date',y='vote')

# %%
df.loc[df['vote']>2000, ['sgId','start','title','category','content']]

#%% 2019년 일자별 투표수
plt.figure(figsize=(20,5))
plt.xticks(rotation=60, ha='right')
plt.title('2019년 일자별 투표수(제안일 기준)')
df_2019 = df[df["start"]>'2018-12-31']
sns.pointplot(data=df_2019.sort_values(by='start-date'), x='start-date', y='vote')


# %% 정규분포도 그리기
from scipy.stats import norm
sns.distplot(df['vote'], fit=norm)

# %% 종료된 제안 수
df[df['end'] < '2019-06-17'].shape
#%% 종료 여부 컬럼 생성, 종료 여부 건 비교
df['close'] = df['end'] < '2019-06-17'
df['close'].value_counts()

# %%
preview_columns = ['sgId','title','category','content','vote','start']
df_top_vote = df.sort_values(by='vote', ascending=False).head(10)
df_top_vote[preview_columns]

# %% 100개 이상 투표를 받은 제안
df_vote_100 = df.loc[df['vote'] > 100, preview_columns]
print('100개 이상 투표를 받은 제안:', len(df_vote_100))
df_vote_100

# %% 건수가 최대인 일반행정 분야의 제안을 투표수 별 정렬
df[df['category'] == '일반행정'].sort_values(by = 'vote', ascending= False).head()


# %%
