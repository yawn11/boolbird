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

list = ["시설물 종류_건축","시설물 종류_산업환경설비","시설물 종류_조경","시설물 종류_토목",
        "공공/민간 구분_공공","공공/민간 구분_민간",
        "날씨_강설","날씨_강우","날씨_강풍","날씨_맑음","날씨_안개","날씨_흐림",
        "공종_가설공사","공종_강구조물공사","공종_건축 토공사","공종_건축물 부대공사","공종_관공사","공종_관공사 부대공사","공종_교량공사","공종_금속공사","공종_기계설비공사","공종_기타","공종_댐 및 제방공사","공종_도로 및 포장공사","공종_도장공사","공종_말뚝공사","공종_목공사","공종_미장공사","공종_방수공사","공종_산업설비공사","공종_수장공사","공종_전기설비공사","공종_조경공사","공종_조적공사","공종_지반개량공사","공종_지반조사","공종_지붕 및 홈통공사","공종_지정공사","공종_창호 및 유리공사","공종_철골공사","공종_철근콘크리트공사","공종_철도 및 궤도공사","공종_타일 및 돌공사","공종_터널공사","공종_토공사","공종_통신설비공사","공종_특수 건축물공사","공종_프리캐스트 콘크리트공사","공종_하천공사","공종_항만공사","공종_해체 및 철거공사",
        "발생일시","공사비","공사기간","공정률","작업자수","설계안전성검토","기온","습도"]

df = pd.DataFrame({"class": list, "boolean": 0.0})
df = df.set_index("class")

#(1) 공사기간 (yy.mm.dd ~ yy.mm.dd)
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    start_day = st.date_input('공사 시작일을 선택해주세요')
with col2 :
    end_day = st.date_input('공사 종료일을 선택해주세요')

#(2) 공사기간 계산
start_day = parser.parse(str(start_day))
end_day = parser.parse(str(end_day))
dur = (end_day - start_day).days
if (dur <= 0): st.error("공사기간 입력 오류입니다. 입력한 공사 시작일과 종료일을 다시 한 번 확인해주세요.")
df.loc['공사기간'] = dur

#(3) 시설물종류 (건축~)
col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1 :
    facility = ['건축', '산업환경설비', '조경', '토목', '기타']
    selected_facility = st.selectbox('시설물종류를 선택해주세요',facility)
string = '시설물 종류_'
df.loc[string + selected_facility] = 1.0
    
#(4) 공정률 (~%)
with col2 :
    percent = st.text_input('공정률을 입력해주세요  (단위 : %)', value="", placeholder="65%라면 '65'라고 입력해주세요")
if percent:
    df.loc['공정률'] = float(percent)
else:
    df.loc['공정률'] = None #이건 왜 있는거야? <- 이거 if문으로 안하니까 ㅇ
    # #근데 그 구글폼에서 다음섹션으로 넘어가는 것처럼도 괜찮으면 if문 없어도 되고 음모르겟다람쥐ㅣ나돜ㅋㅋㅋㅋ 다람ㅣ 일단 보류옥퀴
    # st.error("공사기간 입력 오류입니다. 입력한 공사 시작일과 종료일을 다시 한 번 확인해주세요.")
    

    #(6),(5) 공종 (철근콘크리트~)
with col2:
    category = ['가설공사', '강구조물공사', '건축 토공사', '건축물 부대공사', '관공사', '관공사 부대공사', '교량공사', '금속공사', '기계설비공사', '댐 및 제방공사', '도로 및 포장공사', '도장공사', '말뚝공사', '목공사', '미장공사', '방수공사', '산업설비공사', '수장공사', '전기설비공사', '조경공사', '조적공사', '지반개량공사', '지반조사', '지붕 및 홈통공사', '지정공사', '창호 및 유리공사', '철골공사', '철근콘크리트공사', '철도 및 궤도공사', '타일 및 돌공사', '터널공사', '토공사', '통신설비공사', '특수 건축물공사', '프리캐스트 콘크리트공사', '하천공사', '항만공사', '해체 및 철거공사', '기타']
    search_term = st.text_input('공종 검색어 입력을 통해 빠르게 검색할 수 있습니다', value="", placeholder="금속공사라면 '금속'을 검색해보세요")
    
    filtered_category = [item for item in category if search_term.lower() in item.lower()]
with col1:
    selected_category = st.selectbox('공종을 선택해주세요', filtered_category)
string = '공종_'
df.loc[string + selected_category] = 1.0

#(7) 설계안전성검토 (대상,비대상)
with col1 :
    selected_item2 = st.radio("설계안전성검토를 선택해주세요", ("대상", "비대상"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
if (selected_item2 == "대상"):
    df['설계안전성검토'] = 1.0

#(8) 시설관리공사 (공공,민간)
with col2 :
    selected_item3 = st.radio("시설관리공사를 선택해주세요", ("공공", "민간"))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
if (selected_item3 == "공공"):
    df['시설관리공사'] = 1.0

#(9) 공사비 (~원)
with col1 :
    cost = st.text_input('공사비를 입력해주세요 (단위: 억 원)', value="", placeholder="10억 원이라면 '10'이라고 입력해주세요")
df['공사비'] = cost

#(10) 작업자수 (~명)
with col2 :
    person = st.text_input('작업자수를 입력해주세요  (단위 : 명)', value="", placeholder="1,000명이라면 '1000'이라고 입력해주세요")
df['작업자수'] = person

#------------아래는 출력-----------------


#통계페이지 이동하는 버튼
st.write(' ')
button_clicked = st.button('위험도 예측 결과 확인')
danger = ["하", "중", "상"]
if button_clicked:
    if True:
        st.write(f"위험도는\" {danger[0]} "\"입니다.")
    #elif 조건식2:
        #st.write(f"위험도는", {danger[1]}, "\"입니다.")
    #elif 조건식3:
        #st.write(f"위험도는", {danger[2]}, "\"입니다.")
    
    
    # Add a placeholder 진행 상황 바
    # 전체 바의 스타일과 크기를 설정하는 CSS 스타일
    bar_style = 'background-color: #F0F2F6; height: 8px; width: 100%;'

    # 빨간색 부분의 스타일과 크기를 설정하는 CSS 스타일
    redred = 0.7  # 빨간색 부분의 비율 (0.0 ~ 1.0 사이의 값)
    red_width = int(redred * 100)  # 빨간색 부분의 너비 계산
    red_bar_style = f'background-color: #FF0000; height: 100%; width: {red_width}%;'

    # 바의 HTML 코드
    bar = f'<div style="{bar_style}"><div style="{red_bar_style}"></div></div>'

    # Streamlit에 표시
    st.markdown(bar, unsafe_allow_html=True)







#def preprocess_data():
    # CSV 파일 경로
    #csv_file_path = 'output/output-v2.csv'

    # CSV 파일 로드
    #df = pd.read_csv(csv_file_path)