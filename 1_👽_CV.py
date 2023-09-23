import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Rocket Science! 👋")

st.sidebar.success("aaa")

st.markdown(
    """
    Benvenuto sulla mia pagina creata interamente con streamlit.
    
    👈 Seleziona le sezioni sulla sidebar per scoprire chi sono, cosa faccio e per contattarmi.
    ### Vuoi scoprire streamlit?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)