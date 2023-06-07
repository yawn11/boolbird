import streamlit as st
import pandas as pd

st.title("건설 안전사고 위험도 예측 서비스")
st.write('아래 정보를 입력해주세요\n')

#def preprocess_data():
    # CSV 파일 경로
    #csv_file_path = 'output/output-v2.csv'

    # CSV 파일 로드
    #df = pd.read_csv(csv_file_path)

    # 시설물 종류 추출
    #facility_types = df['시설물 종류'].unique().tolist()

    # 공종 추출
    #job_types = df['공종'].unique().tolist()

    #return facility_types, job_types


# 데이터 전처리 함수 호출하여 시설물 종류와 공종 추출
#facility_types, job_types = preprocess_data()


#공사기간 (yy.mm.dd ~ yy.mm.dd)
col1,col2 = st.columns([1,1])
with col1 :
    day1 = st.date_input('공사 시작일을 선택해주세요 : ')
with col2 :
    day2 = st.date_input('공사 종료일을 선택해주세요 : ')

col1,col2 = st.columns([9,1])
with col1 :
    st.write("전체 공사 기간은 ", day1, "부터 ", day2, "까지입니다.")
with col2 :
    ' '

#시설물종류 (건축~)
col1,col2 = st.columns([1,1])
with col1 :
    lang2 = ['건축', '건축1', '건축2', '건축3']
    selected_lang2 = st.selectbox('시설물종류를 선택해주세요 : ',lang2)
    #selected_lang2 = st.selectbox('시설물종류를 선택해주세요:', facility_types = preprocess_data())

#공종 (철근콘크리트~)
with col2 :
    lang3 = ['철근콘크리트', '철근콘크리트1', '철근콘크리트2', '철근콘크리트3']
    selected_lang3 = st.selectbox('공종을 선택해주세요 : ',lang3)
    #selected_lang3 = st.selectbox('공종을 선택해주세요:', job_types = preprocess_data())

#설계안전성검토 (대상,비대상)
with col1 :
    selected_item2 = st.radio("설계안전성검토를 선택해주세요 : ", ("대상", "비대상"))

#시설관리공사 (공공,민간)
with col2 :
    selected_item3 = st.radio("시설관리공사를 선택해주세요 : ", ("공공", "민간"))

#공사비 (~원)
with col1 :
    st.text_input('공사비를 입력해주세요 : ')
    
#공정률 (~%)
with col2 :
    st.text_input('공정률을 입력해주세요 : ')

#작업자수 (~명)
with col1 :
    st.text_input('작업자수를 입력해주세요 : ')

#통계페이지 이동하는 버튼
with col2 :
    st.write(' ')
    st.button('위험도 예측 결과 확인')