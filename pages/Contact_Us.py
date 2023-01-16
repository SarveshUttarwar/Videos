import streamlit as st
st.header("contact Me")
with st.form(key = "email_forms"):
    user_email = st.text_input("Enter your email address")
    message = st.text_area("enter your message")
    button = st.form_submit_button("submit")
    if button:
        print(button)
        print("I was pressed!")
