import streamlit as st

st.title("건설 안전사고 위험도 예측 서비스")
st.text("텍스트를 입력하세요")
st.text("텍스트를 입력하세요") 
st.write('아무거나 쓰세요')
# user input 받기 
st.text_input('사용자 입력을 받아보세요: ')
occupation = st.selectbox(“직군을 선택하세요.”,
 [“Backend Developer”,
 “Frontend Developer”,
 “ML Engineer”,
 “Data Engineer”,
 “Database Administrator”,
 “Data Scientist”,
 “Data Analyst”,
 “Security Engineer”])
st.write(“당신의 직군은 “, occupation, “ 입니다.”)