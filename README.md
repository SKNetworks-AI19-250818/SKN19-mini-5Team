### SKN19-mini-5Team
EDA / ML mini project 5Team

# 도쿄 숙소값 예측 프로젝트

### 🙋 팀 소개
| 이름    | 김범섭 |  박도연  |  이상혁  |  이승원   |
| ------- | -------|----------|----------|---------- |
| git |   [](https://github.com/WhatSupYap)   |[](https://github.com/pdyeon999)  | [](https://github.com/sangpiri)    |    [](https://github.com/seungwon-sw)      |



### 2. 프로젝트 개요
- 프로젝트 명: 도쿄 예비 여행객들을 위한 숙소값 예측
- 프로젝트 소개: 에어비앤비에서 제공하는 도쿄 숙소 리스트를 기반으로 숙소 조건과 가격의 관계를 분석함
- 프로젝트 목표: 숙소 조건과 가격의 유의미한 관계를 포착하고, 나아가 조건별 숙소값을 예측


- 에어비앤비에서 제공하는 데이터셋 분석으로 예약 가능 여부와 상관없이 숙소의 조건에 따른 가격 예측 가능


### 3. 기술 스택
| 분야 |	기술 |
|------|---------|
|언어 |  python 3.12|
|개발 환경|	Jupyter Notebook| 
|데이터 처리|	Pandas, #013243|
|시각화|	Matplotlib (pyplot), Seaborn|
|버전 관리|github|


### 4. WBS
|분류|상세업무|시작일|종료일|
|---|---|---|---|
|기획|1-1. 데이터셋 탐색 |09.15|09.16|
|기획|1-2. 주제 선정 |09.16|09.16|
|EDA|2-1. 데이터 구조 및 기초 통계 확인 |09.16|09.18|
|EDA|2-2. 결측치 및 이상치 탐색 |09.16|09.18|
|EDA|2-3. 시각화를 통한 컬럼별 탐색 |09.16|09.18|
|EDA|2-4. 컬럼 선정 |09.18|09.18|
|EDA|2-5. 데이터 정제 및 전처리 |09.18|09.20|


### 📑 데이터셋
- 파일명: `tokyo_listings.csv.gz`
- 주요 칼럼: 숙소별 room type, 침실 개수, 1박당 가격 등
- 데이터 출처: [Airbnb](https://insideairbnb.com/)


### 6. EDA
**0. 프로젝트 방향 선정**
    - 숙소값에 큰 영향을 미치는 날짜별 가격 데이터를 조회
    - 성수기에 따른 추가 가격은 에어비앤비 측에서 미제공
    - 

**1. 데이터 로드**
```
df = pd.read_csv('./data/listings.csv.gz', compression='gzip')
```

**2. 데이터 구조 및 기초 통계 확인**
    - 불필요한 칼럼 1차 제거

    - 데이터의 구조를 파악하기 위해 컬럼 정보와 데이터 타입을 확인한다.
    - 데이터의 기본 통계 정보를 출력하여 각 변수의 분포와 특성을 살펴본다.
    - df.head(), df.tail(), df.info(), df.describe() 등의 함수를 사용한다.
    
    
**3. 결측치 및 이상치 탐색**
    1. 숙소 조건 칼럼(bathrooms, bedrooms, beds) 결측치 처리
    1-1. 숙소 조건 칼럼 이상치 처리
    2. price 결측치 처리
    2-1. price 이상치 처리
    3. 
    - 결측치(NaN) 값이 존재하는지 확인하고, 이를 처리하는 방법을 결정한다.
    - 데이터에 존재하는 이상치(Outlier)를 탐지하고, 이를 어떻게 처리할지 결정한다.
    - df.isnull().sum(), df.boxplot() 등의 함수를 활용한다.
    
**4. 데이터 시각화를 통한 탐색**

    1-1) 각 특성 컬럼과 가격 컬럼의 상관관계 도출을 위한 시각화
<img width="1990" height="1990" alt="image" src="https://github.com/user-attachments/assets/f98a4fe1-aeb5-442e-9017-65d8b2f1ef10" />

    1-2) 지역별 가격 관계 시각화
<img width="1790" height="790" alt="image" src="https://github.com/user-attachments/assets/908d9c70-ea96-4176-94aa-ff34eee18ebb" />

    1-3) 룸 타입별 가격 관계 시각화
<img width="1790" height="790" alt="image" src="https://github.com/user-attachments/assets/41741568-f418-45c1-a7bc-52e83ed4674d" />

```
- 수치형 컬럼
  - 수치형 컬럼의 산점도를 봤을 때는 상관관계를 파악하기 어려우나, 선형회귀선을 보면 선형관계를 도출할 수 있음
  - 많은 수용가능인원, 많은 화장실 개수, 많은 침실 개수, 많은 침대 개수, 많은 1년 내의 리뷰 개수, 높은 평점이 높은 가격과 선형관계가 있는 것으로 보아 일반적 통념에 부합
   
- 범주형 컬럼
  - 범주형 컬럼은 범주값이 많아 price를 x축으로 설정 및 수평형 박스플롯을 그린 후, 중위값 상위 순서대로 정렬
  - 중위값과 평균값 비교를 위해 평균값도 빨간점으로 표기
  - 선호되는 특정 지역의 가격이 높은 것을 확인할 수 있었음
  - 단순히 특정 룸만 대여하는 것보다 전체를 대여하는 것이 가격이 높음을 확인할 수 있으며, 룸을 공유하는 것이 가격이 가장 낮은 것으로 보아 일반적 통념에 부합함
```

    2) 리뷰 평점 관련 칼럼 간 heatmap 도출
<img width="939" height="709" alt="image" src="https://github.com/user-attachments/assets/dad157a6-bea1-4a60-a27d-5b71c0114cc2" />

    3) 숙소 위치별 가격 관찰
<img width="974" height="697" alt="image" src="https://github.com/user-attachments/assets/3ad0af07-f3ef-4598-970d-dc1060a63662" />

    4) 각 특성 컬럼과 price의 상관관계 도출을 위한 시각화
<img width="788" height="668" alt="image" src="https://github.com/user-attachments/assets/015fb5d7-b731-4792-823b-51c36823809e" />

        1) 사용 컬럼 : 총 리뷰 수, 12개월 리뷰 수, 30일 리뷰 수, 작년 1년 리뷰 수, 첫 리뷰 날짜, 마지막 리뷰 날짜, 첫 리뷰 후 지난 시간, price

        2) 시각화 내용 : 사용 컬럼과 가격의 상관계수 히트맵
        
        3) 시각화 목적 : 사용 컬럼과 가격의 상관관계 분석

  

<img width="1352" height="1447" alt="image" src="https://github.com/user-attachments/assets/ce7eae7c-2717-42b2-ba13-d3988e7ed84a" />

        1) 사용 컬럼 : 총 리뷰 수, 12개월 리뷰 수, 30일 리뷰 수, 작년 1년 리뷰 수, 첫 리뷰 날짜, 마지막 리뷰 날짜, 첫 리뷰 후 지난 시간, price

        2) 시각화 내용 : 사용 컬럼과 가격의 산점도
  
        3) 시각화 목적 : 컬럼의 분포 및 상관 관계 시각적 확인
  

<img width="774" height="654" alt="image" src="https://github.com/user-attachments/assets/a1b822c3-c3e2-49c7-8cf3-2b99b5b35696" />

        1) 사용 컬럼 : 로그화 된(총 리뷰 수, 12개월 리뷰 수, 30일 리뷰 수, 작년 1년 리뷰 수), 첫 리뷰 날짜, 마지막 리뷰 날짜, 첫 리뷰 후 지난 시간, price, 로그화 된 price
  
        2) 시각화 내용 : 사용 컬럼과 가격의 상관계수 히트맵
  
        3) 시각화 목적 : 로그화 된 컬럼과 가격의 상관관계 분석


    5) amenities - 숙소 편의시설 칼럼
        
        1) 편의시설 개수별 가격 평균
<img width="1619" height="523" alt="image" src="https://github.com/user-attachments/assets/870ee7e2-93f7-437c-97cd-c9148fbc30a2" />

        2) 카테고리화 이후 가격 평균
<img width="1619" height="544" alt="image" src="https://github.com/user-attachments/assets/97e22fb9-b58b-46f4-acfb-31dcc8bdedaa" />


    
    
**5. 데이터 정제 및 전처리**
    
    1) review_scores_rating 제외 평점 관련 칼럼 모두 제거
    
    2) 위도, 경도 칼럼 제거
    
    3) 범주형 데이터 라벨 인코딩 후 상관관계 heatmap
<img width="784" height="658" alt="image" src="https://github.com/user-attachments/assets/07267193-8b0b-4d6e-b629-c1eb0780140d" />
