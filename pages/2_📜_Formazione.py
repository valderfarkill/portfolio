import streamlit as st

st.title("📜 Formazione")
st.container()

st.subheader("IFOA - Tecnico esperto nell'analisi e nella visualizzazione dei dati (IFTS) (2022-2023)")
st.write("Durante il corso ho appreso l'utilizzo di vari tool per elaborazione dati come Tableau e PowerBI (DAX) per la visualizzazione. Excel e SQL per database. Machine Learning e Data Mining con IDE VsCode, Python e le sue librerie.")

st.subheader("LABA Rimini - Diploma di Accademia di Belle Arti di 1° Livello - Design, Voto 110/110 (2017-2021)")
st.write("Utilizzo di programmi come Photoshop, Illustrator, Indesign per l'elaborazione grafica e Rhinoceros, Cinema 4D per la modellazione e rendering.")

st.subheader("Google Digital Academy (Skillshop) - Certificazione Google Analytics(2023)")
st.write("Utilizzo di Google Analytics 4")

st.subheader("IFOA - Attestato Project Work Laboratoriale (2023)")
st.write("Project Work in elaborazione di dati tramite Excel(Microsoft Office) e Tableau. Analisi della parte semantica con Nooj. Utilizzo piattaforma di KPI6.")

st.subheader("IFOA - Attestato in Strumenti di data analysis e visualization (2023)")
st.write("Elaborazione di dati tramite Excel(Microsoft Office) e Tableau. Analisi della parte semantica con Nooj.")

st.subheader("Circolo Ratataplan Riccione - Attestato Dreamweaver e Fireworks Developer (2011)")
st.write("Creazione pagine web dinamiche con Dreamweaver, MySQL e PHP.")

st.subheader("Circolo Ratataplan Riccione - Attestato Dreamweaver e Fireworks Designer (2011)")
st.write("Creazione di siti strutturati con Dreamweaver, HTML, CSS, Javascript.")

pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')