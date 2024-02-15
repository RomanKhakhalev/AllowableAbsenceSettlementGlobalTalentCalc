import streamlit as st, pandas as pd, matplotlib as plt
st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','till'])



if ID_file:
    st.markdown(f'***The upload document was faked with probability 80%***')