import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/jmp2.jpg", width=400)

with col2:
    st.title("Elijah Dayon")
    content = """Hi, I'm Elijah with the ID 119 student from DLSU. Right now I'm developing skill as web developer 
    to prepare for OJT. Once I settled with OJT, I will plan studying course related to either Artificial Intelligence
     or GIS for my undergrad thesis"""
    st.info(content)