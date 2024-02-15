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
                with st.container():
                    st.markdown("Likelihood of image being AI generated: :green[30%]")
                    st.markdown("Likelihood of photo being photoshopped: :green[30%]")    
                    st.markdown("MRZ number incongruence: :green[30%]")     
                    
        # with tabs[i]:
        #      st.image(f'Data/Photos/2.png', caption="Original", width=None, use_column_width=None)
        #      st.image(f'Data/Results/2.png', caption="Original", width=None, use_column_width=None)


with st.container():    
     s = f"<p style='font-size:20px;'>:green[Likelihood of the photo being AI generated 50%]</p>"
     st.markdown(s, unsafe_allow_html=True)  
     