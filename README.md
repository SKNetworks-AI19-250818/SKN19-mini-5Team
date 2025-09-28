### SKN19-mini-5Team
EDA / ML mini project 5Team

# 도쿄 숙소값 예측 프로젝트

### 🙋 "여권어디있지" 팀 소개
| 이름    | 김범섭 |  박도연  |  이상혁  |  이승원   |
| ------- | -------|----------|----------|---------- |
| git |   [WhatSupYap](https://github.com/WhatSupYap)   |[pdyeon999](https://github.com/pdyeon999)  | [sangpiri](https://github.com/sangpiri)    |    [seungwon-sw](https://github.com/seungwon-sw)      |


<br><br>
### 🧳 프로젝트 개요
![tokyo-tower-5664846_1920](https://github.com/user-attachments/assets/b3c2d61a-5b13-427a-992a-14fee90b30bc)

- 프로젝트 명: 엔저로 인해 일본 여행이 증가하는 현재 trend를 고려한, 도쿄 예비 여행객들을 위한 숙소값 예측
- 프로젝트 소개: 에어비앤비에서 제공하는 도쿄 숙소 리스트를 기반으로 숙소 조건과 가격의 관계를 분석함
- 프로젝트 목표: 숙소 조건과 가격의 유의미한 관계를 포착하고, 나아가 조건별 숙소값을 예측


<br><br>
### 💻 기술 스택
| 분야 |	기술 |
|------|---------|
|언어 | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt='python' width='20'/> python 3.12|
|개발 환경| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" alt='VSCode' width='20'/> VSCode| 
|데이터 처리|<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original.svg" alt='Pandas' width='20'/> Pandas, <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original.svg" alt='NumPy' width='20'/> NumPy|
|시각화|	<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/matplotlib/matplotlib-original.svg" alt='Matplotlib' width='20'/> Matplotlib, <img src="https://img.shields.io/badge/-Seaborn-green?logo=python&logoColor=white" height="20"/> Seaborn|
|버전 관리|<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" alt='github' width='20'/> github|

<br><br>
### 🪜 WBS
|분류|상세업무|시작일|종료일|
|---|---|---|---|
|기획|1-1. 데이터셋 탐색 |09.15|09.16|
|기획|1-2. 주제 선정 |09.16|09.16|
|EDA|2-1. 데이터 구조 및 기초 통계 확인 |09.16|09.18|
|EDA|2-2. 결측치 및 이상치 탐색 |09.16|09.18|
|EDA|2-3. 시각화를 통한 컬럼별 탐색 |09.16|09.18|
|EDA|2-4. 컬럼 선정 |09.18|09.18|
|EDA|2-5. 데이터 정제 및 전처리 |09.18|09.20|
|EDA|2-6. EDA 취합 및 정리 |09.21|09.22|
|ML|3-1. 모델 선택 및 학습 |09.24|09.25|
|ML|3-2. 성능 평가 및 하이퍼파라미터 튜닝 |09.25|09.26|
|ML|3-3. 최종 모델 확정 |09.26|09.26|


<br><br>
### 💭 데이터셋
- 파일명: `listings.csv.gz`
- 주요 칼럼: 숙소가 위치한 지역, 숙소별 방 유형, 화장실/침실/침대 개수, 제공하는 편의시설, 리뷰 평점, 1박당 가격 등
- 데이터 출처: [Airbnb](https://insideairbnb.com/)

<br><br>
### 🪴 EDA  
<br>

**0. 프로젝트 방향 선정**
- 숙소값에 큰 영향을 미치는 날짜별 가격 데이터를 조회했으나, 성수기에 따른 추가 가격은 에어비앤비 측에서 미제공하므로 성수기/비수기의 가격 차이는 고려하지 않기로 결정
- 그 외 숙소값에 영향을 미치는 특징들을 추출하여 EDA 과정을 진행한 후 머신러닝 모델을 통해 특정한 특징들을 충족하는 숙소값을 예측해보기로 함
<br><br> 

**1. 데이터 로드**
```
df = pd.read_csv('./data/listings.csv.gz', compression='gzip')
```
<br>

**2. 데이터 구조 및 기초 통계 확인**

📌 데이터의 기본 컬럼, 결측치, 데이터 타입 등 확인  
<img width="737" height="593" alt="Image" src="https://github.com/user-attachments/assets/ef8db27e-44f9-48a9-a0f8-fc52b4360cd9" />
<br><br>

📌 데이터의 상위 5행 확인  
<img width="1823" height="467" alt="Image" src="https://github.com/user-attachments/assets/4256555f-59e6-4cf9-9286-72c31334f8f3" />
<br>  
📌 특성의 양이 방대하므로, 라벨인 price와 의미있는 컬럼(특성)만을 추출  
<img width="621" height="765" alt="Image" src="https://github.com/user-attachments/assets/d1739e11-2ecd-4629-97f4-5d63f24926d3" />    
<br>
<br>
    
**3. 결측치 및 이상치 탐색**

⭐ price 컬럼  

📌 특성이 있는 그룹별로 price가 상이할 것으로 예상되므로, 그룹별 price 평균치 확인 후 price 결측치를 특성 그룹별 평균값으로 대체  
<img width="1590" height="1189" alt="Image" src="https://github.com/user-attachments/assets/1e6da5ed-85d1-4770-9b0e-dc797364d143" /> 
<br>  
📌 price 이상치 탐색  
<img width="217" height="198" alt="Image" src="https://github.com/user-attachments/assets/7b36904f-5379-4454-891c-9f5dd36e98af" />  
<br>
📌 이상치 기준을 정하기 위해 각 기준별로 시각화
<img width="1190" height="1181" alt="Image" src="https://github.com/user-attachments/assets/4d528d73-97e6-47ba-b12c-5d7a6af44fe8" />  
<br>
📌 이상치 제거  
<img width="273" height="61" alt="Image" src="https://github.com/user-attachments/assets/9a660760-704b-4b78-b7b0-85e599450687" />  
<br><br>

⭐ 그 외 컬럼  

📌 선정된 중요 컬럼의 결측치 제거 (ex. bathrooms, bedrooms, beds)  
<img width="272" height="61" alt="Image" src="https://github.com/user-attachments/assets/ce57733b-7bdb-4a98-9d62-c598d9a89548" />
<br>  
📌 선정된 중요 컬럼의 이상치 확인을 위한 각 컬럼이 갖고 있는 고유값과 그 개수 확인  
<img width="1781" height="201" alt="Image" src="https://github.com/user-attachments/assets/98420866-dfdc-44cf-a0d4-f846a4f02e16" />  
<img width="1778" height="491" alt="Image" src="https://github.com/user-attachments/assets/da6eee1c-4c9e-4afa-9e75-d834e884391b" />  
<img width="1776" height="582" alt="Image" src="https://github.com/user-attachments/assets/c4156490-3d34-4a37-82b0-74b0cb5339aa" />  
<img width="1777" height="390" alt="Image" src="https://github.com/user-attachments/assets/8db609e8-0b5f-4ca1-a726-d63a0cba9aba" />  
<img width="1773" height="723" alt="Image" src="https://github.com/user-attachments/assets/5761df43-69a6-41aa-97b2-276245bc9a11" />  
<br>
📌 개수가 적어 유의미하지 않은 값을 이상치로 처리하여 제거
<br>
<img width="267" height="57" alt="Image" src="https://github.com/user-attachments/assets/47f7faad-7495-4bf4-83e9-f3960c98a5af" />  
<br>
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
<br><br>

    
**5. 데이터 정제 및 전처리**
    
📌 review_scores_rating 제외 평점 관련 칼럼 모두 제거
    
📌 위도, 경도 칼럼 제거
    
📌 범주형 데이터 라벨 인코딩 후 상관관계 도출을 위한 히트맵 시각화
<img width="784" height="658" alt="image" src="https://github.com/user-attachments/assets/07267193-8b0b-4d6e-b629-c1eb0780140d" />  
<br>

📌 데이터 전처리 완료 직후 info  
<img width="489" height="531" alt="Image" src="https://github.com/user-attachments/assets/5ed4dc40-7ed7-43e0-be3e-8847617d66f2" />  

### 1️⃣ 2차 데이터 전처리 진행  
1) 문자열 타입인 컬럼의 데이터 변환 : 라벨 인코딩 진행  
<img width="980" height="215" alt="Image" src="https://github.com/user-attachments/assets/1d6d33dc-8bb7-46ec-9e95-a8e93bc201b9" />   
  
2) 피처 엔지니어링을 통한 파생 특성 생성  
   (단, 모델링 사전 테스트시 r2값에 큰 영향없고 특성 중요도 떨어지므로, 모델링시는 사용하지 않음) 
<img width="802" height="129" alt="Image" src="https://github.com/user-attachments/assets/f4bf3a1f-9849-443c-9eeb-c25f3f9517d9" />  

  
### 2️⃣ 모델링  
1) 학습과 평가 데이터 분리  

2) 라벨 데이터의 값이 크므로, 로그화 진행    
  
3) 모델 선택 : 앙상블 모델 中 LightGBM
<img width="692" height="458" alt="Image" src="https://github.com/user-attachments/assets/c80e3a75-9ca0-4aa0-b981-e962029e0804" />  
  
4) 1차 모델링 결과 (cv=3으로 진행한 경우)
<img width="581" height="48" alt="Image" src="https://github.com/user-attachments/assets/881a8dce-080a-40d9-9bcf-45c1a2ea9dcc" />  

5) 교차 검증 진행 (cv=5로 진행)  
<img width="634" height="377" alt="Image" src="https://github.com/user-attachments/assets/137168bb-0897-4618-94a0-e1d18c5545ee" />  

6) 2차 모델링 결과  
<img width="842" height="52" alt="Image" src="https://github.com/user-attachments/assets/14ec443e-5028-473c-a87b-98d1516098b0" />  

7) 모델링 후 특성 중요도 확인  
<img width="1036" height="697" alt="Image" src="https://github.com/user-attachments/assets/b4543a8a-94fe-471f-98a5-e6b47a3b8af9" />  

  
### 3️⃣ 예측 페이지 구현
1) 시작 화면
<img width="2880" height="1332" alt="스크린샷1" src="https://github.com/user-attachments/assets/09ac0334-befe-4557-9136-f0e1b19a0731" />

2) '선택 시작하기' 버튼을 눌렀을 때
<img width="2880" height="1334" alt="스크린샷2" src="https://github.com/user-attachments/assets/935d3e1b-bf16-4a5c-9d5a-3001405231a2" />

3-1) 옵션을 선택 후 '기본 옵션으로 예측 결과 보기' 버튼을 눌렀을 때
<img width="2824" height="1487" alt="스크린샷3-1" src="https://github.com/user-attachments/assets/340a5330-1589-4ca9-be39-8746a0430cfa" />

3-2-1) 옵션을 선택 후 '추가 옵션 선택' 버튼을 눌렀을 때
<img width="2824" height="2278" alt="스크린샷3-2" src="https://github.com/user-attachments/assets/ee46daa2-74d4-420e-b552-70d5828dbe1d" />

3-2-2) 추가 옵션 선택 후 '추가 옵션으로 예측 결과 보기' 버튼을 눌렀을 때
<img width="2824" height="1421" alt="스크린샷3-3" src="https://github.com/user-attachments/assets/6f79a8c1-07c9-43f1-955d-3fcb0de9a255" />

### 4️⃣ Trouble shooting
1) 김범섭
    - 문제 상황 : EDA 과정에서 amenities 컬럼이 중요하다 여겼으나 호스트가 직접 입력한 배열형태의 문자열으로 구성되어 학습용 데이터로 사용하기 어려웠다.
    - 해결 : 모든 데이터를 다운로드 받아보니 패턴이 보여 ast 라이브러리르 티용 텍스트를 분류하여 약 30종류로 카테고리로 분류를 진행하였고 분류된 데이터를 ML학습에 사용할 수 있었다.
   
2) 박도연
    - 문제 상황 : 같은 가상환경에서 lightgbm과 joblib을 `pip install`하고 `streamlit run`을 했음에도 streamlit 페이지에서 모델을 불러오지 못하는 문제가 있었다.
    - 해결 : 설치 경로를 출력해본 결과, streamlit이 가상환경 내에 설치되어 있지 않아 환경 외부에 설치된 경로로 실행되고 있었고, 따라서 lightgbm, joblib 모듈을 찾지 못하는 문제였다. 가상환경에도 streamlit을 install함으로써 해결했고, 환경 분리의 중요성을 깨달았다.
     
3) 이상혁
    - 문제 상황 : 피처 엔지니어링 과정 중 파생 특성을 생성하면서, 해당 파생 특성을 생성할 때 사용한 특성 변수를 삭제하지 않고 모델링을 진행했더니 R2 점수는 상승했으나 과대적합이 더 심해지는 문제가 발생하였다. 또한 Grid Search를 통해 최적의 하이퍼 파라미터를 찾는 과정에서 너무 다양한 하이퍼 파라미터를 입력했더니, 출력 과정에서 시간이 상당히 오래 소요되었다.
    - 해결 : 과대적합 방지를 위해 파생 특성을 생성할 때 사용한 특성 변수를 삭제하고 모델링을 진행하였다. 특성 변수들 간의 다중공선성 방지를 위해서라도, 피처 엔지니어링시 특성 변수들 간의 관계를 더 주의해야 함을 깨달았다. 또한 Grid Search를 통해 세밀한 하이퍼 파라미터를 찾는 것도 중요하지만, 출력 시간 단축을 위해 Random Search를 이용하였다.

4) 이승원
   - 문제 상황 : 피어슨 상관 계수 분석에서 X데이터의 특정 컬럼과 y(price)의 상관 계수가 낮게 나왔다. 하지만 이는 선형적 관계에 대한 반영이므로 비선형적 관계에 대한 가능성을 배제하기 어려웠다.
   - 해결 : 비선형적 관계에 대해 학습을 할 수 있는 XGBoost, 랜덤 포레스트 등의 트리 기반 모델을 사용해 학습했다.



### 5️⃣ 회고록
| 이름  | 회고 |
| ------ | --------------- |
| 김&nbsp;범&nbsp;섭 | EDA, ML 과정중 EDA과정을 주도적으로 진행하였다. EDA 추가 분석 덕분에 ML은 팀 동료들의 도움을 많이 받았다. ML 부분에서는 스스로 생각한 부분이 적은 것 같아 아쉽다. 프로젝트 마무리 후 전체적으로 리뷰가 필요할 듯 하다. |
| 박&nbsp;도&nbsp;연 | 배뤘던 여러 모델을 이용해 실데이터를 학습시키고 성능을 평가해보았다. 그리고 간단하게라도 이용자에게 값을 직접 받아 피쳐 데이터로 변환해 예측을 수행하는 페이지를 구현했는데, 생각보다 많은 처리를 필요로 했다. 성능 높이기와 동시에 이용자에게 어느 정도의 값을 받고 나머지 피쳐는 어떤 식으로 처리해야 유용한 서비스가 될 수 있는지 고려하는 게 다음 프로젝트의 숙제일 것 같다. | 
| 이&nbsp;상&nbsp;혁 | 모델링에 집중을 했었는데 모델링 결과를 이용해 라벨값을 예측해보니, 데이터 전처리의 중요성을 더 실감하게 되었다. 데이터에 대한 도메인 지식을 높이고 그를 통해 올바른 데이터 정제를 해야 좋은 모델을 도출할 수 있는 것 같다. | 
| 이&nbsp;승&nbsp;원 | 머신 러닝의 다양한 모델들을 사용해보며 성능과 특징을 비교해 볼 수 있었다. |
