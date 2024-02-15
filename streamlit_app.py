import streamlit as st

st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','till'])
#asdfasd


if ID_file:
    st.markdown(f'***The upload document was faked with probability 80%***')
    tabs = st.tabs(['Original Photo','Checking result'])
    st.markdown(f'***The upload document was faked with probabilidty 80%***')
    st.markdown(f'***The upload document was faked with probability 80%***')
    with tabs[0]:
    	 st.image('Photos/1.png', caption="Results", width=None, use_column_width=None)
    with tabs[1]:
    	st.image('Results/1.png', caption="Results", width=None, use_column_width=None)

 