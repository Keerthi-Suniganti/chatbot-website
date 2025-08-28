import streamlit as st
from googletrans import Translator

# ------------------------
# Website title & Shinchan Watermark
# ------------------------
st.set_page_config(page_title="Shinchan", page_icon="🤖", layout="centered")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.ibb.co/D4R8tWf/shinchan-bg.png");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    opacity: 0.1;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ------------------------
# Title & Intro
# ------------------------
st.title("💬 Shinchan Chatbot Website")
st.write("Welcome! Ask me anything below:")

# ------------------------
# Language Selection
# ------------------------
translator = Translator()

st.sidebar.title("🌐 Language Settings")
language = st.sidebar.selectbox("Choose Language", ["English", "Hindi", "Telugu", "Japanese"])

def translate_text(text, target_lang):
    lang_codes = {"English": "en", "Hindi": "hi", "Telugu": "te", "Japanese": "ja"}
    return translator.translate(text, dest=lang_codes[target_lang]).text

# ------------------------
# User Input & Response
# ------------------------
user_input = st.text_input("You:")

if user_input:
    # Step 1: Translate input to English (for processing)
    translated_in = translate_text(user_input, "English")

    # Step 2: Dummy chatbot reply (replace with real model later)
    bot_reply = f"I heard you say: {translated_in}"

    # Step 3: Translate back to selected language
    translated_out = translate_text(bot_reply, language)

    # Step 4: Show reply
    st.markdown(f"**🤖 Shinchan:** {translated_out}")

