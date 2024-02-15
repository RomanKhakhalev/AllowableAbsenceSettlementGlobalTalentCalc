import streamlit as st

st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','tiff'])


if ID_file:
    tabs = st.tabs(['First sample','Second sample', 'First sample'])
    for i in range(3):
        with tabs[i]:
            cols= st.columns(2)
            with cols[0]:
                st.image(f'Data/Results/{i}.png', caption="Original", width=None, use_column_width=None)
            with cols[1]:
                with st.container:
                        st.markdown("Document validity:86%")
                        st.markdown("Photo validity: 33%")
        # with tabs[i]:
        #      st.image(f'Data/Photos/2.png', caption="Original", width=None, use_column_width=None)
        #      st.image(f'Data/Results/2.png', caption="Original", width=None, use_column_width=None)


    # with st.container:
#     st.header(f":green[*You have not exceed the allowance on number of days outside UK*]")