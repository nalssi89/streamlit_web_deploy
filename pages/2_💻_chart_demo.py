import streamlit as st
import pandas as pd
import numpy as np

# 페이지 기본 설정
st.set_page_config(
    page_icon="🏚️",
    page_title="날씨의 스트림릿 배포하기",
    layout="wide",
)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df)