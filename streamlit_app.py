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
    counter += 1
    if counter > MAX_COUNTER:
        counter = 0
#    col1, col2= st.columns(2)
#    with col1:
    with tabs[0]:
    	 st.header('Please, enter the initial parameters')
         #st.image(f'Data/Photos/1.png', caption="Original", width=None, use_column_width=None)
    with tabs[1]:
        st.header('Please, enter the initial parameters')
    	#t.image(f'Data/Results/{counter}.png', caption="Results", width=None, use_column_width=None)
    # with col2:
    #     st.markdown("Document validity:86%")
    #     st.markdown("Photo validity: 33%")

    # with st.container:
#     st.header(f":green[*You have not exceed the allowance on number of days outside UK*]")