# ** URL/robots.txt --> 크롤링 가능 영역 표시된 문서

#%% 필요한 도구 불러오기
import pandas as pd # 엑셀과 유사한 데이터 분석 도구
import requests # 매우 작은 브라우저, 웹사이트의 내용과 정보를 불러올 수 있다.
from bs4 import BeautifulSoup as bs # 웹사이트 html 태그를 파싱하는 도구
import random # 랜덤숫자 생성 --> 사람이 데이터 읽는 것 처럼 일정하지 않게 크롤링하는데 사용
import time
from tqdm import tqdm, trange # 대량 데이터 처리시 진행 상황 표시, ex) 20% 완료
import re # 정규표현식

#%% 정부혁신 국민포럼 페이지 가져오기
pnum = 1
year_month = 201906

base_url = f"https://www.innogov.go.kr/ucms/ogp/sug/list.do?pnum={pnum}&menuNo=300011&cateCd=&status1Cd=&Status2Cd=&searchText=&sugMonthTp={year_month}&orderKey=registDtDesc"
base_url

# %% 원하는 정보 출력해보기
# URL이 있는 태그의 위치: 브라우저의 Inspect 기능을 통해 selector 가져오기
# Copy -> Copy selector를 통해 해당 태그의 위치를 가져옴
response = requests.get( base_url )
response

if response.status_code == 200:
    html = bs(response.text, 'html.parser')

    #소스코드 제대로 가져왔는지 확인
    tags = html.select('#content > div.suggestion_list > ul')[0].find_all('a')
    #print(tags) 
    for tag in tags: 
        print(tag['href']) # 제목 누르면 들어가지는 URL 만 가져오기 

# %% 페이지 번호를 추가해가며 크롤링해 오는 함수
def get_suggestion_list(pnum):
    # print(f'year_month:{year_month}, pnum:{pnum}')
    
    base_url = f"https://www.innogov.go.kr/ucms/ogp/sug/list.do?pnum={pnum}&menuNo=300011&cateCd=&status1Cd=&Status2Cd=&searchText=&sugMonthTp=&orderKey=registDtDesc"
    response = requests.get(base_url)

    if response.status_code == 200: #200이라는 코드는 Okay라는 뜻
        html = bs(response.text, 'html.parser')
        tags = html.select('#content > div.suggestion_list > ul')[0].find_all('a')

        if not tags: #tag 내용 없을 때 suggestion_list 반환
            return(suggestion_list)
        else:
            for tag in tags: 
                suggestion_list.append(tag['href'])
        
        pnum += 1
        get_suggestion_list(pnum) # 페이지 번호 더한 후 재귀호출
        print('\n',pnum)
    else:
        return(suggestion_list)

# %% 함수 사용해서 크롤링
suggestion_list = []
pnum = 1

get_suggestion_list(pnum)
suggestion_list

# %% 제대로 가져왔는지 확인
print(len(suggestion_list))
suggestion_list

# %% 게시물 내용 가져오기
url = '/ucms/ogp/sug/view.do?menuNo=300011&sgId=217&pnum=1'
base_url = f"https://www.innogov.go.kr{url}"
response = requests.get(base_url)

if response.status_code == 200:
    html = bs(response.text, 'html.parser')
    print(html.select('#content > div.vveiw_box1 > dl > dt'))

    title = html.select('#content > div.vveiw_box1 > dl > dt')[0].get_text(strip= True)
    print(title)


# %%
desc = html.select(
    '#content > div.vveiw_box1 > div.vveiw_name > ul > li > dl > dd')
category = desc[0].get_text(strip = True)
print(desc[0].get_text(strip= True))
print(desc[1].get_text(strip= True))
print(desc[2].get_text(strip= True))
print(desc[3].get_text(strip= True))


# %% id 값을 저장해주기 위해 미리 추출해보기
u = 'view.do?menuNo=300011&sgId=150&pnum=1'
u.split('=')[2].split('&')[0]

#%% 목록 리스트에 있는 url을 넘겨주면 내용을 크롤링하는 함수

def get_suggestion_content(url):
    article = []
    base_url = f"https://www.innogov.go.kr/{url}"
    response = requests.get( base_url )

    if response.status_code == 200:
        html = bs(response.text, 'html.parser')
        title = html.select(  #제목을 가져옴
                '#content > div.vveiw_box1 > dl > dt')[0].get_text(strip=True)
        desc  = html.select(  
                '#content > div.vveiw_box1 > div.vveiw_name > ul > li > dl > dd')
        category = desc[0].get_text(strip=True)
        content = html.select('#content > div.vveiw_box1 > div.vveiw_cont > div > pre')[0].get_text(strip=True)
        start = desc[1].get_text(strip=True)
        end = desc[2].get_text(strip=True)
        author = desc[3].get_text(strip=True)
        vote = html.select('#counter')[0].get_text(strip = True) #추천인
        sgld = url.split('=')[2].split('&')[0]

        article.append(sgld)
        article.append(title)
        article.append(category)
        article.append(content)
        article.append(start)
        article.append(end)
        article.append(vote)
        article.append(author)
        print(article)

        time.sleep(random.randint(1,2))
        return article

# %% 각 게시물의 세부내용 가져오기
data = []

#tqdm을 사용해서 어느 정도 가져왔는지 확인
for i, suggestion in tqdm(enumerate(suggestion_list)):
    #list에 있는 게시물에 접근해서 내용을 가져온다
    s = get_suggestion_content(suggestion)
    data.append(s)

# %% data를 DataFrame화 시키기
column_names = ['sgId','title','category','content','start','end','vote','author']
data = pd.DataFrame(data, columns = column_names)
data.head()
#%%
data.tail()

# %%
data['category'].value_counts()
#%%
data.to_csv('suggestion.csv',index=False)
#%%
pd.read_csv('suggestion.csv').head()
#%%
data.shape


# %%
