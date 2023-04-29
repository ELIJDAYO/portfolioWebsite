import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/jmp2.jpg", width=400)

with col2:
    st.title("Elijah Dayon")
    content = """Hi, I'm Elijah. An ID 119 student from De La Salle University. I'm developing skill 
    as web developer to prepare for OJT. I will plan studying course related to either Artificial Intelligence
     or GIS for my undergrad thesis"""
    st.info(content)

content2 = """
The links below can lead to some course works or personal projects I have done in the past.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    # extract each row from df
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

# last 10 rows df[10:]
# first 10 roes df[:10]
with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")