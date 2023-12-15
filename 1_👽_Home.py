import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.header("# Welcome to Rocket Science! 👋")


st.subheader(
    """
    Benvenuto sulla mia pagina creata interamente con streamlit.
"""
)

st.subheader(
    """   
    👈 Seleziona le sezioni sulla sidebar per progetti e contatti.
"""
)

pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')