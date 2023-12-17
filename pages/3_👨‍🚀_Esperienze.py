import streamlit as st

st.title("👨‍🚀 Esperienze")
st.container()

st.subheader("TULIPS S.P.A. (2023)")
st.write("Data Analyst.")

st.subheader("TECNAM S.N.C. (2021-2022)")
st.write("Freelance come Designer, Modellatore 3D, Renderista,Tecnico Informatico.")

st.subheader("Hotel Medusa (2017)")
st.write("Cameriere - Stagionale.")

st.subheader("Minimarket Alex e Mirco Riccione(2011-2016)")
st.write("Commesso e magazziniere - collaboratore familiare stagionale.")

st.subheader("Jam Studio (2010)")
st.write("Tecnico Informatico - tirocinio.")

pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')