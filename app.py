# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import re
from dateutil import parser


#------------아래는 제목-----------------


#제목
col1,empty2,col2 = st.columns([1, 0.3, 8.7])
with col1 :
    st.image("phoenix.png", width=80)
with col2 :
    st.title("건설 안전사고 위험도 예측 서비스\n")


#------------아래는 입력 (총 10개)---------

df = pd.DataFrame()

#(1) 공사기간 (yy.mm.dd ~ yy.mm.dd)
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    start_day = st.date_input('공사 시작일을 선택해주세요')
with col2 :
    end_day = st.date_input('공사 종료일을 선택해주세요')

#(2) 공사기간 계산
#start_day = parser.parse(start_day)
#end_day = parser.parse(end_day)
#dur = (end_day - start_day).days
#if (dur <= 0): st.write("공사기간 입력 오류")
#else:
#   df['공사기간'] = float(dur)
#   print(df)

#(3) 시설물종류 (건축~)
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    lang2 = ['건축', '산업환경설비', '조경', '토목', '기타']
    selected_lang2 = st.selectbox('시설물종류를 선택해주세요',lang2)
#if (selected_lang2 == '건축'): 
    
#(4) 공정률 (~%)
with col2 :
    percent = st.text_input('공정률을 입력해주세요  (단위 : %)', value="", placeholder="65%라면 '65'라고 입력해주세요")
#percent = float(percent)    

#(6),(5) 공종 (철근콘크리트~)
with col2:
    lang3 = ['가설공사', '강구조물공사', '건축 토공사', '건축물 부대공사', '관공사', '관공사 부대공사', '교량공사', '금속공사', '기계설비공사', '댐 및 제방공사', '도로 및 포장공사', '도장공사', '말뚝공사', '목공사', '미장공사', '방수공사', '산업설비공사', '수장공사', '전기설비공사', '조경공사', '조적공사', '지반개량공사', '지반조사', '지붕 및 홈통공사', '지정공사', '창호 및 유리공사', '철골공사', '철근콘크리트공사', '철도 및 궤도공사', '타일 및 돌공사', '터널공사', '토공사', '통신설비공사', '특수 건축물공사', '프리캐스트 콘크리트공사', '하천공사', '항만공사', '해체 및 철거공사', '기타']
    search_term = st.text_input('공종 검색어 입력을 통해 빠르게 검색할 수 있습니다', value="", placeholder="금속공사라면 '금속'을 검색해보세요")
    
    filtered_lang3 = [item for item in lang3 if search_term.lower() in item.lower()]
with col1:
    selected_lang3 = st.selectbox('공종을 선택해주세요', filtered_lang3)

#(7) 설계안전성검토 (대상,비대상)
with col1 :
    selected_item2 = st.radio("설계안전성검토를 선택해주세요", ("대상", "비대상"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#(8) 시설관리공사 (공공,민간)
with col2 :
    selected_item3 = st.radio("시설관리공사를 선택해주세요", ("공공", "민간"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#(9) 공사비 (~원)
with col1 :
    st.text_input('공사비를 입력해주세요 (단위: 억 원)', value="", placeholder="10억 원이라면 '10'이라고 입력해주세요")

#(10) 작업자수 (~명)
with col2 :
    st.text_input('작업자수를 입력해주세요  (단위 : 명)', value="", placeholder="1,000명이라면 '1000'이라고 입력해주세요")


#------------아래는 출력-----------------


#통계페이지 이동하는 버튼
st.write(' ')
button_clicked = st.button('위험도 예측 결과 확인')
danger = ["하", "중", "상"]
if button_clicked:
    if True:
        st.write(f"{danger[0]}")
    #elif 조건식2:
        #st.write(f"{danger[1]}")
    #elif 조건식3:
        #st.write(f"{danger[2]}")
    # Add a placeholder 진행 상황 바

m=0.5
bar = st.progress(m)

i=0.3
bar = st.empty()
bar.progress(i)







#def preprocess_data():
    # CSV 파일 경로
    #csv_file_path = 'output/output-v2.csv'

    # CSV 파일 로드
    #df = pd.read_csv(csv_file_path)