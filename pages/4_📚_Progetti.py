import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("🖥️ Progetti")

st.link_button("🌺 Iris", "https://progetti-portfolio-ruhwsrys82wz43tk7csv4f.streamlit.app/")
st.link_button("🚀 Startup", "https://progetti-portfolio-5hlpsswcnuu4injkjtxcy4.streamlit.app/")
st.link_button("🐧 Penguins", "https://progetti-portfolio-esmqc3ivnvffvywxcg3b2z.streamlit.app/")
st.link_button("🏢 Immobili", "https://progetti-portfolio-3qnshxc8p25qkaohegwadq.streamlit.app/")
st.link_button("🎭 Fake News Detection", "https://progetti-portfolio-774v2foj9eyxawgfkrt4wz.streamlit.app/")

pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')

