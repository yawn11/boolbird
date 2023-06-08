# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

st.title("건설 안전사고 위험도 예측 서비스")
st.write('아래 정보를 입력해주세요')
st.title(" ")

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
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    day1 = st.date_input('공사 시작일을 선택해주세요 : ')
with col2 :
    day2 = st.date_input('공사 종료일을 선택해주세요 : ')

col1,col2 = st.columns([2, 0.03])
with col1 :
    st.write("전체 공사 기간은 ", day1, "부터 ", day2, "까지입니다.")
with col2 :
    ' '

#시설물종류 (건축~)
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    lang2 = ['건축', '산업환경설비', '조경', '토목', '기타']
    selected_lang2 = st.selectbox('시설물종류를 선택해주세요 : ',lang2)
    #selected_lang2 = st.selectbox('시설물종류를 선택해주세요:', facility_types)
    
#공정률 (~%)
with col2 :
    st.text_input('공정률을 입력해주세요 : ')
    
# 공종 (철근콘크리트~)
with col1:
    lang3 = ['가설공사', '강구조물공사', '건축 토공사', '건축물 부대공사', '관공사', '관공사 부대공사', '교량공사', '금속공사', '기계설비공사', '댐 및 제방공사', '도로 및 포장공사', '도장공사', '말뚝공사', '목공사', '미장공사', '방수공사', '산업설비공사', '수장공사', '전기설비공사', '조경공사', '조적공사', '지반개량공사', '지반조사', '지붕 및 홈통공사', '지정공사', '창호 및 유리공사', '철골공사', '철근콘크리트공사', '철도 및 궤도공사', '타일 및 돌공사', '터널공사', '토공사', '통신설비공사', '특수 건축물공사', '프리캐스트 콘크리트공사', '하천공사', '항만공사', '해체 및 철거공사', '기타']
    search_term = st.text_input('공종 검색어를 입력하세요:', '')
    
    filtered_lang3 = [item for item in lang3 if search_term.lower() in item.lower()]
with col2:
    selected_lang3 = st.selectbox('공종 검색어가 포함된 항목을 선택해주세요:', filtered_lang3)

#설계안전성검토 (대상,비대상)
with col1 :
    selected_item2 = st.radio("설계안전성검토를 선택해주세요 : ", ("대상", "비대상"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#시설관리공사 (공공,민간)
with col2 :
    selected_item3 = st.radio("시설관리공사를 선택해주세요 : ", ("공공", "민간"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#공사비 (~원)
with col1 :
    st.text_input('공사비를 입력해주세요 : ')

#작업자수 (~명)
with col2 :
    st.text_input('작업자수를 입력해주세요 : ')

#통계페이지 이동하는 버튼
st.write(' ')
st.button('위험도 예측 결과 확인')



#오늘