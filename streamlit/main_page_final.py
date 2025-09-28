import streamlit as st
import pandas as pd
import numpy as np
import lightgbm
from joblib import load
from datetime import date


# 예측에 필요한 LightGBM 모델 파일 로드
loaded_model = load('./assets/model_LGBMReg_r2_test_0.71.jobilb')


# 1. neighbourhood_cleansed
neighbourhood_json = pd.read_json('./assets/le_neighbourhood_cleansed.json')

# 2. property_type
property_type_json = pd.read_json('./assets/le_property_type.json')

# 3. room_type
room_type_json = pd.read_json('./assets/le_room_type.json')

# 3-2. room -> property 매핑
room_to_property = {'Entire home/apt': 'Entire rental unit',
 'Hotel room': 'Room in hostel',
 'Private room': 'Private room in home',
 'Shared room': 'Shared room in hostel'}

# 4. 어매니티 기본값 딕셔너리
amnt_default_value_dict = {'amnt_self_checkin': 1,
 'amnt_instant_book': 0,
 'amnt_kitchen': 1,
 'amnt_hair_dryer': 1,
 'amnt_free_parking': 0,
 'amnt_wifi': 1,
 'amnt_private_bathroom': 0,
 'amnt_bbq_grill': 0,
 'amnt_washer': 1,
 'amnt_pets_allowed': 0,
 'amnt_clothes_dryer': 1,
 'amnt_heating': 1,
 'amnt_air_conditioning': 1,
 'amnt_workspace': 0,
 'amnt_iron': 0,
 'amnt_pool': 0,
 'amnt_bathtub': 1,
 'amnt_ev_charger': 0,
 'amnt_crib': 0,
 'amnt_king_bed': 0,
 'amnt_gym': 0,
 'amnt_breakfast': 0,
 'amnt_fireplace': 0,
 'amnt_smoking_allowed': 0,
 'amnt_waterfront': 0,
 'amnt_smoke_alarm': 1,
 'amnt_carbon_monoxide_alarm': 0}

# 5. 기준 날짜 (데이터 업로드 날짜) 정의
base_date = date(2025, 6, 27)


# 예측에 필요한 함수 정의
def make_X(neighbourhood, room_type, accommodates,
            bedrooms, beds, bathrooms, review_scores_rating,
            amnt_values):
    
    # 피쳐 초기화
    X = []

    # neighbourhood_cleansed 라벨 변환
    X.append(int(neighbourhood_json[neighbourhood_json.iloc[:, 0] == neighbourhood].index[0]))
    
    # property_type 임의 부여
    X.append(int(property_type_json[property_type_json.iloc[:, 0] == room_to_property[room_type]].index[0]))

    # room_type 라벨 변환
    X.append(int(room_type_json[room_type_json.iloc[:, 0] == room_type].index[0]))

    # 어매니티 제외 나머지 피쳐 합치기
    X.extend([accommodates, bathrooms, bedrooms, beds, review_scores_rating])
    
    # amnt_values 합치기
    X.extend(amnt_values)

    return np.array(X).reshape(1, -1)

st.set_page_config(layout="wide")


# 제목
st.markdown("<h1 style='text-align: center;'>도쿄 1박 숙박비 예상</h1>", unsafe_allow_html=True)

# CSS 스타일 (배경 + 카드 박스)
st.markdown(
    """
    <style>
    .stApp {
        background: 
            linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
            url('https://media.triple.guide/triple-cms/c_limit,f_auto,h_1024,w_1024/c790403c-fdf1-47f7-b9cc-d5b320a7dbfb');
        background-repeat: no-repeat;
        background-size: cover;
        background-attachment: scroll;
        background-position: top center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 세션 상태 초기화
# 시작하기 버튼 세션
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False

# 추가 옵션 버튼 세션
if 'extra_input' not in st.session_state:
    st.session_state.extra_input = False

# 결과 보기 버튼 세션
if 'show_result' not in st.session_state:
    st.session_state.show_result = False


# 버튼 클릭 시 실행할 콜백 함수
def start_app():
    st.session_state.start_clicked = True


# 피쳐 초기화
get_X = False

if not st.session_state.start_clicked:
    st.button('희망하는 옵션 선택 시작하기!', on_click=start_app)

else:
    # 컬럼 나누기
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("(1) 지역, 타입, 인원 선택")

        # 1. 지역, 타입, 수용인원 선택
        neighbourhood = st.selectbox("숙소 지역 선택", neighbourhood_json)
        room_type = st.selectbox("숙소 타입 선택", room_type_json)
        
        st.markdown("---")
        accommodates = st.number_input("인원 선택(1~16)", 1, 16)
        

    with col2:
        st.subheader("(2) 방 옵션, 평점 선택")

        # 2. 침실 수, 침대 수, 화장실 수, 점수 평균 선텍
        bedrooms = st.number_input("침실 수 선택(0~10)", 0, 10)
        beds = st.number_input("침대 개수 선택(0~25)", 0, 25)
        bathrooms = st.number_input("화장실 수 선택(0~10)", 0, 10)

        st.markdown("---")
        review_scores_rating = st.number_input("평점 선택(0.0~5.0)", 0.0, 5.0)


    with col3:
        # 3. 기본 편의시설 선택
        st.subheader("(3) 편의시설 유무 선택")

        self_checkin = st.checkbox("셀프 체크인")
        wifi = st.checkbox("WIFI")
        parking = st.checkbox("주차 가능")
        iron = st.checkbox("다리미")

        selected_options = []

        if self_checkin:
            selected_options.append("amnt_self_checkin")
        if wifi:
            selected_options.append("amnt_wifi")
        if parking:
            selected_options.append("amnt_free_parking")
        if iron:
            selected_options.append("amnt_iron")


        st.markdown("---")

    # 버튼을 항상 표시하도록 수정
    with col3:
        if st.button("추가 옵션 선택", key='add_option'):
            st.session_state.extra_input = True
            st.session_state.show_result = False  # 추가 옵션을 선택하면 결과 화면 리셋
        if st.button("기본 옵션으로 예측 결과 보기", key='first_view'):
            st.session_state.show_result = True
            st.session_state.extra_input = False  # 기본 예측을 선택하면 추가 옵션 리셋
     

    # 추가 옵션 선택 버튼을 눌렀을 때
    if st.session_state.extra_input:
        # 어매니티 칼럼 저장
        amnt_values = {k: 0 for k in amnt_default_value_dict}
        for k in selected_options:
            amnt_values[k] = 1

        st.subheader("추가 편의시설 옵션")

        amenity_cols = st.columns(3)
        
        # 값 받을 열두 개 어매니티 칼럼
        question_amenities = {
            "amnt_hair_dryer": "헤어드라이어",
            "amnt_bbq_grill": "바베큐 그릴",
            "amnt_washer": "세탁기",
            "amnt_heating": "난방",
            "amnt_air_conditioning": "냉방",
            "amnt_workspace": "업무 전용 공간",
            "amnt_pool": "수영장",
            "amnt_bathtub": "대형 욕조",
            "amnt_crib":"아기 침대",
            "amnt_smoking_allowed": "흡연 가능",
            "amnt_smoke_alarm": "화재경보기",
            "amnt_carbon_monoxide_alarm": "일산화탄소 경보기"
        }

        for i, amnt in enumerate(question_amenities.items()):
            with amenity_cols[i % 3]:
                choice = st.radio(f"{amnt[1]}", ["필요", "불필요"], index=1, key=f"amenity_{amnt[1]}")
                if choice == "필요":
                    amnt_values[amnt[0]] = 1

        st.markdown("---")
        if st.button("추가 옵션으로 예측 결과 보기", key='second_view'):
            get_X = make_X(neighbourhood, room_type, accommodates,
                           bedrooms, beds, bathrooms, review_scores_rating,
                           list(amnt_values.values()))#, first_date)  # first_date 제외
            
            pred = loaded_model.predict(get_X)
            st.markdown("<h1 style='text-align: center;'>숙박비: 약 "+str(format(int(np.expm1(pred)*10), ','))+"원</h1>", unsafe_allow_html=True)

            # 에어비앤비 사이트 링크
            st.write('에어비앤비 바로가기 >> https://www.airbnb.co.kr/')
    
    # 기본 옵션으로 예측 결과 보기 버튼을 눌렀을 때
    elif not st.session_state.extra_input and st.session_state.show_result:
        # 어매니티 칼럼 저장
        amnt_values = amnt_default_value_dict.copy()  # 딕셔너리 복사
        for k in selected_options:
            amnt_values[k] = 1

        get_X = make_X(neighbourhood, room_type, accommodates,
                           bedrooms, beds, bathrooms, review_scores_rating,
                           list(amnt_values.values()))#, first_date)  # first_date 제외

        pred = loaded_model.predict(get_X)
        st.markdown("<h1 style='text-align: center;'>숙박비: 약 "+str(format(int(np.expm1(pred)*10), ','))+"원</h1>", unsafe_allow_html=True)

        # 에어비앤비 사이트 링크
        st.write('에어비앤비 바로가기 >> https://www.airbnb.co.kr/')
        
        # 다른 옵션 선택 버튼 추가
        if st.button("추가 옵션으로 다시 예측하기"):
            st.session_state.extra_input = True
            st.session_state.show_result = False
            st.rerun()