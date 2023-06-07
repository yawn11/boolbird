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