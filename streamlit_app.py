import streamlit as st

st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

SCORES = [
         
         ['10%','30%','50%','60%'],
         ['10%','30%','50%','60%'],
         ['10%','30%','50%','60%']

         ]

with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','tiff'])


if ID_file:
    for i in range(3):
        with st.container():    
           st.header(f"Total authenticy score: :green[{SCORES[i][0]}]")  
        tabs = st.tabs(['Lois Griffin','Steven Bell', 'Elon Musk'])
        with tabs[i]:
            cols= st.columns(2)
            with cols[0]:
                st.image(f'Data/Results/{i}.png', caption="Original", width=None, use_column_width=None)
            with cols[1]:
                with st.container():
                    st.subheader("Likelihood of image being AI generated: :green[30%]")
                    st.subheader("Likelihood of photo being photoshopped: :green[30%]")    
                    st.subheader("MRZ number incongruence: :green[30%]")     
                        
        # with tabs[i]:
        #      st.image(f'Data/Photos/2.png', caption="Original", width=None, use_column_width=None)
        #      st.image(f'Data/Results/2.png', caption="Original", width=None, use_column_width=None)



     