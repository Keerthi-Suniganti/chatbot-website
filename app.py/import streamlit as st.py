import streamlit as st

# Website title
st.set_page_config(page_title="Chatbot Website", page_icon="🤖", layout="centered")

st.title("💬 Chatbot Website")
st.write("Welcome! Ask me anything below:")

# User input
user_input = st.text_input("You:")

# Dummy chatbot logic (replace with Watson or any model later)
if user_input:
    st.markdown(f"**🤖 Bot:** I heard you say: {user_input}")
