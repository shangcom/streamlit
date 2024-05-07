import streamlit as st
import pandas as pd
import numpy as np

st.title("인공지능 시인 만들기")

st.header("목차")

st.subheader("1.LLM 이란?")
st.write("대형 언어 모델 또는 거대 언어 모델은 수많은 파라미터를 보유한 인공 신경망으로 구성되는 언어 모델이다. 자기 지도 학습이나 반자기지도학습을 사용하여 레이블링되지 않은 상당한 양의 텍스트로 훈련된다. LLM은 2018년 즈음에 모습을 드러냈으며 다양한 작업을 위해 수행된다.")
st.subheader("2.LMM 실습")

# st.button("test")

if st.button("여기를 누르세요"):
   st.write("Data Loading......")
    # 데이터 로딩 함수는 여기에!

st.write("당신의 성별은?")
checkbox_btn1 = st.checkbox('남')
checkbox_btn2 = st.checkbox('여')

if checkbox_btn1:
   st.write('남성')

if checkbox_btn2:
   st.write('여성')

selected_item = st.radio("메뉴판", ("짜장", "짬뽕", "볶음밥"))

if selected_item == "짜장":
   st.write("짜장면 선택")
elif selected_item =="짬뽕":
   st.write("짬뽕 선택")
elif selected_item =="볶음밥":
   st.write("볶음밥 선택")
else:
   st.write("메뉴는 3가지")

   
option = st.selectbox('학년을 고르세요', ('1학년', '2학년', '3학년'))
st.write('선택 학년 : ', option)
multi_select = st.multiselect('과목들을 선택하세요', ['경영', '경제', '회계', '물리', '화학'])
st.write('선택한 과목 : ', multi_select)

values = st.slider('범위를 선택하세요', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


# height = np.array([166,168,170,172,174])
df = pd.DataFrame({"이름":['홍일동','홍이동','홍삼동','홍사동','홍오동']},
{"키":['166','168','170','172','174']})
st.table(df)