import streamlit as st

st.title("건설 안전사고 위험도 예측 서비스")
st.text("텍스트를 입력하세요")
st.text("텍스트를 입력하세요") 
st.write('아무거나 쓰세요')
# user input 받기 
st.text_input('사용자 입력을 받아보세요: ')

lang = ['py', 'java', 'c', 'go']
selected_lang = st.selectbox('언어선택하쇼',lang)
st.write('니가고른언어는 {}임니다'.format(selected_lang))


selected_item = st.radio("Radio Part", ("A", "B", "C"))
if selected_item == "A":
    st.write("A!!")
elif selected_item == "B":
    st.write("B!")
elif selected_item == "C":
    st.write("C!")


#공사기간 (yy.mm.dd ~ yy.mm.dd)
#시설물종류 (건축~)
lang2 = ['건축', '건축1', '건축2', '건축3']
selected_lang2 = st.selectbox('시설물종류를 선택해주세요 : ',lang2)
#공종 (철근콘크리트~)
lang3 = ['철근콘크리트', '철근콘크리트1', '철근콘크리트2', '철근콘크리트3']
selected_lang3 = st.selectbox('공종을 선택해주세요 : ',lang3)
#설계안전성검토 (대상,비대상)
selected_item2 = st.radio("설계안전성검토를 선택해주세요 : ", ("대상", "비대상"))
#시설관리공사 (공공,민간)
#공정률 (~%)
st.text_input('공정률을 입력해주세요 : ')
#공사비 (~원)
st.text_input('공사비를 입력해주세요 : ')
#작업자수 (~명)
st.text_input('작업자수를 입력해주세요 : ')