import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a Project above.")

st.markdown(
    """
    📧 [Email](bigzam.3@outlook.com)

    👥 [Linkedin](https://www.linkedin.com/in/emanuele-tonti/)

    🗺️ [Instagram](https://www.instagram.com/_goldenmanu_/)
"""
)