import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.header("THE BEST COMPANY")
content = """Hi, I am Sarvesh Uttarwar, CEO of BEST company. This is one of the best company to work, it has got a 
great working environment, we've got great clients, recently we raised 200 million dollars at a valuation 1.6 
billlion dollars. Below are the photos of some of our employees """
st.write(content)
st.title("OUR EMPLOYEES")
col1 ,col2 , col3 = st.columns([2,2,2])
df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index,row in df[0:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.image(row["image"])
        st.write(row["role"])
with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.image(row["image"])
        st.write(row["role"])
with col3:
    for index,row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.image(row["image"])
        st.write(row["role"])



