import numpy as np
import pandas as pd

import streamlit as st

st.write('# 인플루엔자 월별 환자수 추이')
st.write('## 출처: 건강보험심사평가원 보건의료빅데이터시스템')
st.write('월별 환자수(단위:명)')

df = pd.DataFrame({
    'data' : ['202210' , '202211' , '202212' , '202301'],
    'second coulmn' : [20771, 104327, 738954, 373886]
})


df

st.line_chart(df.rename(columns={'data':'index'}).set_index('index'))
