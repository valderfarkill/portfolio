import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Emanuele Tonti")

st.header("#Su di me! 👋")

st.subheader("Data Analyst/Designer Product Manager")
st.write("👋🏻 Ciao, Sono Manu. Designer e Data Analyst. Sto cercando attivamente lavoro.")
st.write("🏋🏻 Hobby: ;i piace l'informatica, leggere, i videogiochi, e soprattuto mangiare!")
st.write("👨🏼‍💻 Interessi accademici: Design, Data Science, Cybersecurity")
st.write("💭 Prospetti ideali: Data Analyst, DBA, Product Manager, Designer, CYbersecurity Analyst")

st.subheader(
    """   
    👈 Seleziona le sezioni sulla sidebar per altre informazioni.
"""
)

pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')