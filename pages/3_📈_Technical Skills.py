import streamlit as st

st.title("📈 Technical Skills")

st.header("Data ")
columns = st.columns(7)
columns[0].button('Python')
columns[1].button('Mysql')
columns[2].button('Vs Code')
columns[3].button('Power Bi')
columns[4].button('Tableau')
columns[5].button('Nooj')
columns[6].button('Office')

st.header("Design")
columns = st.columns(7)
columns[0].button('Autocad')
columns[1].button('Vector')
columns[2].button('Cinema 4D')
columns[3].button('Keyshot')
columns[4].button('Rhino')
columns[5].button('Adobe')




pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')