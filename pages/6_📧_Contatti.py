import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("📩 Contattami qui")

st.link_button("👥 Linkedin", "https://www.linkedin.com/in/emanuele-tonti/")

st.subheader(":mailbox: Scrivimi una mail!")


contact_form = """
<form action="https://formsubmit.co/bigzam.3@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


pdfFileObj = open('pdfs/Emanuele_Tonti_CV_.pdf', 'rb')
st.sidebar.download_button('📄Scarica CV',pdfFileObj,file_name='Emanuele_Tonti_CV_.pdf',mime='pdf')
