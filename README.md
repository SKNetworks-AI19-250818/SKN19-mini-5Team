### SKN19-mini-5Team
EDA / ML mini project 5Team

# 도쿄 숙소값 예측 프로젝트

### 🙋 팀 소개
| 이름    | 김범섭 |  박도연  |  이상혁  |  이승원   |
| ------- | -------|----------|----------|---------- |
| git |   [WhatSupYap](https://github.com/WhatSupYap)   |[pdyeon999](https://github.com/pdyeon999)  | [sangpiri](https://github.com/sangpiri)    |    [seungwon-sw](https://github.com/seungwon-sw)      |



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
|데이터 처리|	Pandas, NumPy|
|시각화|	Matplotlib, Seaborn|
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

📌 데이터의 기본 컬럼, 결측치, 데이터 타입 등 확인  
<img width="737" height="593" alt="Image" src="https://github.com/user-attachments/assets/ef8db27e-44f9-48a9-a0f8-fc52b4360cd9" />
<br>

📌 데이터의 상위 5행 확인  
<img width="621" height="765" alt="Image" src="https://github.com/user-attachments/assets/d1739e11-2ecd-4629-97f4-5d63f24926d3" />
<br>

📌 특성의 양이 방대하므로, 라벨인 price와 의미있는 컬럼(특성)만을 추출  
<img width="1590" height="1189" alt="Image" src="https://github.com/user-attachments/assets/1e6da5ed-85d1-4770-9b0e-dc797364d143" />    
<br>
    
**3. 결측치 및 이상치 탐색**

⭐ price 컬럼  

📌 특성이 있는 그룹별로 price가 상이할 것으로 예상되므로, 그룹별 price 평균치 확인 후 price 결측치를 특성 그룹별 평균값으로 대체  
<img width="217" height="198" alt="Image" src="https://github.com/user-attachments/assets/7b36904f-5379-4454-891c-9f5dd36e98af" />    
<br>
📌 price 이상치 탐색  
<img width="1190" height="1181" alt="Image" src="https://github.com/user-attachments/assets/32e86853-3777-4ba7-9239-11d93f0f24db" />  
<br>
📌 이상치 기준을 정하기 위해 각 기준별로 시각화
<img width="1190" height="1181" alt="Image" src="https://github.com/user-attachments/assets/4d528d73-97e6-47ba-b12c-5d7a6af44fe8" />
<br>
📌 이상치 제거  
<img width="273" height="61" alt="Image" src="https://github.com/user-attachments/assets/9a660760-704b-4b78-b7b0-85e599450687" />  
<br>

⭐ 그 외 컬럼  

📌 선정된 중요 컬럼의 결측치 제거 (ex. bathrooms, bedrooms, beds)  
<img width="276" height="61" alt="Image" src="https://github.com/user-attachments/assets/0941ad01-6d45-4dcc-b6b6-6d4fb92ade78" />  
<br>
📌 선정된 중요 컬럼의 이상치 확인을 위한 각 컬럼이 갖고 있는 고유값과 그 개수 확인  
<img width="1781" height="201" alt="Image" src="https://github.com/user-attachments/assets/98420866-dfdc-44cf-a0d4-f846a4f02e16" />  
<img width="1778" height="491" alt="Image" src="https://github.com/user-attachments/assets/da6eee1c-4c9e-4afa-9e75-d834e884391b" />  
<img width="1776" height="582" alt="Image" src="https://github.com/user-attachments/assets/c4156490-3d34-4a37-82b0-74b0cb5339aa" />  
<img width="1777" height="390" alt="Image" src="https://github.com/user-attachments/assets/8db609e8-0b5f-4ca1-a726-d63a0cba9aba" />  
<img width="1773" height="723" alt="Image" src="https://github.com/user-attachments/assets/5761df43-69a6-41aa-97b2-276245bc9a11" />  
<br>
📌 개수가 적어 유의미하지 않은 값을 이상치로 처리 (ex. bathrooms이나 bedrooms 개수가 15개를 초과하는 경우 등)  
<img width="267" height="57" alt="Image" src="https://github.com/user-attachments/assets/47f7faad-7495-4bf4-83e9-f3960c98a5af" />  
<br>
    
**4. 데이터 시각화를 통한 탐색**

📌 총 수용인원, 화장실수, 침실수, 침대수 등과 가격 컬럼의 상관관계 도출을 위한 시각화  
<img width="1990" height="1990" alt="image" src="https://github.com/user-attachments/assets/f98a4fe1-aeb5-442e-9017-65d8b2f1ef10" />  

📌 지역별 가격 관계 시각화  
<img width="1790" height="790" alt="image" src="https://github.com/user-attachments/assets/908d9c70-ea96-4176-94aa-ff34eee18ebb" />  

📌 룸 타입별 가격 관계 시각화  
<img width="1790" height="790" alt="image" src="https://github.com/user-attachments/assets/41741568-f418-45c1-a7bc-52e83ed4674d" />  

📌 리뷰 평점 관련 칼럼 간 히트맵 도출  
<img width="939" height="709" alt="image" src="https://github.com/user-attachments/assets/dad157a6-bea1-4a60-a27d-5b71c0114cc2" />  

📌 숙소 위치별 가격 관찰  
<img width="974" height="697" alt="image" src="https://github.com/user-attachments/assets/3ad0af07-f3ef-4598-970d-dc1060a63662" />  

📌 리뷰 관련 컬럼과 가격의 상관관계 도출을 위한 시각화
<img width="788" height="668" alt="image" src="https://github.com/user-attachments/assets/015fb5d7-b731-4792-823b-51c36823809e" />    

📌 각종 리뷰 수와 가격의 상관관계 도출을 위한 산점도 시각화  
<img width="1352" height="1447" alt="image" src="https://github.com/user-attachments/assets/ce7eae7c-2717-42b2-ba13-d3988e7ed84a" />  

📌 로그화된 리뷰 수 컬럼과 가격의 상관관계 도출을 위한 히트맵 시각화
<img width="774" height="654" alt="image" src="https://github.com/user-attachments/assets/a1b822c3-c3e2-49c7-8cf3-2b99b5b35696" />

📌 amenities - 숙소 편의시설 칼럼
        
📍📍 편의시설 개수별 가격 평균
<img width="1619" height="523" alt="image" src="https://github.com/user-attachments/assets/870ee7e2-93f7-437c-97cd-c9148fbc30a2" />

📍📍 카테고리화 이후 가격 평균
<img width="1619" height="544" alt="image" src="https://github.com/user-attachments/assets/97e22fb9-b58b-46f4-acfb-31dcc8bdedaa" />


    
    
**5. 데이터 정제 및 전처리**
    
📌 review_scores_rating 제외 평점 관련 칼럼 모두 제거
    
📌 위도, 경도 칼럼 제거
    
📌 범주형 데이터 라벨 인코딩 후 상관관계 heatmap
<img width="784" height="658" alt="image" src="https://github.com/user-attachments/assets/07267193-8b0b-4d6e-b629-c1eb0780140d" />

![Image](https://github.com/user-attachments/assets/9ea4a854-3c87-499f-8537-69131683551d)
