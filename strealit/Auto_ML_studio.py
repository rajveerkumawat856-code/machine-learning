import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header('Auto ML Project')
file=st.file_uploader('Uplode Your File',type=['csv'])

if file is not None:
    df=pd.read_csv(file)
    if 'show_data' not in st.session_state:
        st.session_state.show_data=False

    if st.button('Show / Hide Data'):
        st.session_state.show_data=not st.session_state.show_data
    if st.session_state.show_data:
        st.dataframe(df)
    
columns=st.selectbox('select the column',df.columns)
st.write(df[columns])
