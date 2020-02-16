#%% 
import numpy as np
#%% *************************** Array ***************************
# vector 형태
test = np.array([1, 4, 5, 8],float)
print(test)
print(type(test[3]))
print(test.dtype) 
print(test.shape) #Array 형태 반환

# %%
test = np.array([1, 4, 5, '8'],float)
print(test)
type(test[3])

# %%
test = np.array([1, 4, 5, '8'],str)
print(test)
type(test[3])

# %% matrix형태
matrix = [[1,2,5,8],[1,2,5,8],[1,2,5,8]]
np.array(matrix,int).shape

# %% 3차원 매트릭스 형태
tensor =  [ [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
            [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
            [[1,2,5,8],[1,2,5,8],[1,2,5,8]] ]
np.array(tensor, int).shape

# %% ndim: 몇 차원인지
np.array(tensor, int).ndim
# %% size: 데이터의 총 개수
np.array(tensor, int).size


# %% *********************** reshape ***********************
test_matrix = [[1,2,5,8],[1,2,3,4]]
print(np.array(test_matrix).shape)
print(np.array(test_matrix). reshape(8,))
np.array(test_matrix). reshape(8,).shape

# %% Array의 size 만 같다면 다차원으로 자유롭게 변형가능
np.array(test_matrix).reshape(2,4).shape
# %% -1: size를 기반으로 row개수 선정
np.array(test_matrix).reshape(-1,2).shape
# %%
np.array(test_matrix).reshape(2,2,2)

# %% flatten: 다차원 array를 1차원 array로 변환
test_matrix = [[[1,2,3,4], [1,2,5,7]] ,[[2,4,6,8],[1,3,5,7]]]
np.array(test_matrix).flatten()


# %% ************************** indexing & slicing **************************
# indexing
a = np.array([[1,2,3],[4.5,5,6]],int)
print(a)
print(a[0,0])
print(a[0][0]) 

a[0,0] = 5
print(a)

# %% slicing
a = np.array([ [1,2,3,4,5],[6,7,8,9,10] ], int)
print(a[:,2:])  # row(a:b), column(c:d)
print(a[1,1:3])
print(a[1:3])

# %% *********************** Creation Function
# arange: array의 범위를 지정하여, 값의 list를 생성하는 명령어
a = np.arange(30)
b = np.arange(0,5,0.5) #시작, 끝, step
c = np.arange(30).reshape(5,6)
print(a,type(a))
print(b)
print(c)

# %% 리스트 타입으로 반환
a = np.arange(30).tolist()
print(a, type(a))

# %% zeros: 0으로 가득찬 ndarray생성
np.zeros(shape= (10,), dtype= np.int8)
# %%
np.zeros((2,5))

# %% ones: 1로 가득찬 ndarray 생성
np.ones(shape=(10,), dtype=np.int8)
# %%
np.ones((2,5))

# %% empty: shape만 주어지고 비어있는 ndarray 생성 
#(memory initialization이 되지 않음)
np.empty(shape=(10,), dtype=np.int8)
# %%
np.empty((3,5))

# %% something_like: 기존 ndarray의 shape 크기 만큼 1,0 또는 empty array 반환
test_matrix = np.arange(30).reshape(5,6)
a = np.ones_like(test_matrix)
b = np.zeros_like(test_matrix)
print(a,'\n',b)


# %% idintity: 단위행렬(i 행렬)을 생성함
np.identity(n= 3, dtype= np.int8)
# %%
np.identity(5)

#%% eye: 대각선이 1인 행렬, k값의 시작 index의 변경이 가능
np.eye(N=3, M=5, dtype=np.int8)
# %%
np.eye(3) # identity행렬과 거의 동일
# %%
np.eye(3,5,k=2) #k -> start point


# %% diag: 대각행렬의 값을 추출함
matrix = np.arange(9).reshape(3,3)
np.diag(matrix)
# %%
np.diag(matrix, k=1) # k-> start point


# %% random sampling: 데이터 분포에 따른 sampling으로 array를 생성
# uniform(최저,최고,개수) 인 균등분포
np.random.uniform(0,1,10).reshape(2,5) 

# %% normal(평균,분산,개수) 인 정규분포
np.random.normal(0,1,10).reshape(2,5)

# %% ********************* array operation *********************
test_a = np.array([[1,2,3],[4,5,6]], float)
#shape이 같을때 같은 위치 cell 숫자끼리 연산
print(test_a + test_a)
print(test_a - test_a)
print(test_a * test_a) 

# %% Dot product: Matrix의 기본연산
test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)
test_a.dot(test_b)

# %% transpose / T attribute: 전치행렬
print(test_a,'\n')
print(test_a.transpose(),'\n')
print(test_a.T)
print(test_a.T.dot(test_a))

# %% broadcasting: shape이 다른 배열 간 연산을 지원하는 기능 --> 자동연산
test_matrix = np.array([[1,2,3],[4,5,6]], float)
scalar = 3

print(test_matrix + scalar)
print(test_matrix * scalar)
print(test_matrix / scalar)
print(test_matrix // scalar)
# %%
test_matrix = np.arange(1,13).reshape(4,3)
test_vector = np.arange(10,40,10)
test_matrix + test_vector



# %% Numpy performance

def scalar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar*value)
    return result

iternation_max = 10000000

vector = list(range(iternation_max))
scalar = 2

%timeit scalar_vector_product(scalar, vector) # for loop를 이용한 성능
%timeit [scalar*value for value in range(iternation_max)]
%timeit np.arange(iternation_max)*scalar
#timeit: jupyter 환경에서 코드의 퍼포먼스를 체크하는 함수


# %% *************** comparisons ***************
# All & Any
a = np.arange(10)
print(np.all(a>5), np.all(a<10)) # all 모두가조건에 만족한다면 true
print(np.any(a<0), np.any(a>5)) # any 하나라도 조건에 만족한다면

# %% Comparison operation #1
test_a = np.array([1,3,0], float)
test_b = np.array([5,2,1], float)

print(test_a == test_b)
print((test_a > test_b).any())

# %% Comparison operation #2
a = np.array([1,3,0],float)
np.logical_and(a>0, a<3)
#%% 
b = np.array([True, False, True], bool)
np.logical_not(b)
#%%
c = np.array([False,True,False],bool)
np.logical_or(b,c)


# %%  np.where(condition, TRUE, FALSE)
np.where(a>0, 3, 2)
# %%
a = np.arange(10)
np.where(a>5)  #Index값 반환
#%%
a = np.array([1, np.NaN, np.Inf],float)
np.isnan(a)
#%%
np.isfinite(a)


# %% argmax & argmin
# array내 최대값 또는 최소값의 index를 반환함
a = np.array([1,2,4,5,8,78,23,3])
np.argmax(a), np.argmin(a)

# %% #axis기반
a = np.array([[1,2,4,7], [9,88,6,45], [9,76,3,4]])
print(np.argmax(a, axis=1)) # n번째 열에서
np.argmax(a, axis=0) # n 번째 행에서

# %%
