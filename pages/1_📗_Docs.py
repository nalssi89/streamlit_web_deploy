import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_icon="🏚️",
    page_title="날씨의 스트림릿 배포하기",
    layout="wide",
)

st.subheader("도큐먼트")


code = """
import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon="🏚️",
    page_title="날씨의 스트림릿 배포하기",
    layout="wide",
)

# 페이지 헤드, 서브헤드 제목 설정
st.header("날씨 홈페이지 오신 것을 환영합니다.")
st.subheader("스트림릿 기능 맛보기")

# 페이지 컬럼 분할(예, 부트스트랩 컬럼, 그리드)
cols = st.columns((1,1,2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "18 °C", "5")
cols[0].metric("10/13", "21 °C", "-2")
cols[1].metric("10/14", "16 °C", "1")
cols[1].metric("10/15", "17 °C", "-4")
cols[1].metric("10/16", "20 °C", "-2")

# 라인 그래프 데이터 생성(with pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c'])

cols[2].line_chart(chart_data)
"""

if st.button("app.py 코드 보기"):
    st.code(code, language="python")