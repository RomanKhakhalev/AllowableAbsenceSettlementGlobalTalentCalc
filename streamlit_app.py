import streamlit as st


def formatIt(t):
    if t<20:
        result = f":green[{t}%]"
    else:
        if t < 80:
            result = f":yellow[{t}%]"
        else:
            result = f":red[{t}%]"
    return result


st.set_page_config(
    page_title="Super-accurate ID checker for major and most prominent banks",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

SCORES = [
         [92,98,8,13],
         [78,7,78,42],
         [7,19,7,5,60]
         ]


with st.sidebar:
    st.header('Please, enter the initial parameters')
    ID_file = st.file_uploader('Please upload ID document', type = ['jpg','png','jpeg', 'bmp','tiff'], accept_multiple_files = True)


if ID_file:
        st.header('ID checking app')
        tabs = st.tabs(['Lois Griffin','Steven Bell', 'Elon Musk'])
        for i in range(3):
            with tabs[i]:
                st.header(f"Total authenticy score: {SCORES[i][0]} %")  
                cols= st.columns(2)
                with cols[0]:
                    st.image(f'Data/Results/{i}.png', caption="Uploaded image", width = None, use_column_width = None)
                with cols[1]:
                    with st.container():
                        st.subheader(f"Likelihood of image being AI generated: {formatIt(SCORES[i][1])}")
                        st.subheader(f"Likelihood of photo being photoshopped: {formatIt(SCORES[i][2])}")    
                        st.subheader(f"MRZ number incongruence: {formatIt(SCORES[i][3])}")     
                        
        # with tabs[i]:
        #      st.image(f'Data/Photos/2.png', caption="Original", width=None, use_column_width=None)
        #      st.image(f'Data/Results/2.png', caption="Original", width=None, use_column_width=None)



     