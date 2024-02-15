import streamlit as st

st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','tiff'])

counter = 0
MAX_COUNTER = 2
if ID_file:
    tabs = st.tabs(['Original Photo','Checking results'])
    counter += 1
    if counter > MAX_COUNTER:
        counter = 0
    
    with col1:
        with tabs[0]:
            col1, col2= st.columns(2)
            with col1:
                st.image(f'Data/Photos/1.png', caption="Original", width=None, use_column_width=None)
            with col2:
                st.image(f'Data/Results/1.png', caption="Original", width=None, use_column_width=None)
        with tabs[1]:
             st.image(f'Data/Photos/2.png', caption="Original", width=None, use_column_width=None)
             st.image(f'Data/Results/2.png', caption="Original", width=None, use_column_width=None)
    with col2:
        st.markdown("Document validity:86%")
        st.markdown("Photo validity: 33%")

    # with st.container:
#     st.header(f":green[*You have not exceed the allowance on number of days outside UK*]")