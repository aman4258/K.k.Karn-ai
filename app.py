import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="K.K. Karn AI", page_icon="🤖")

st.title("🤖 Welcome to K.K. Karn AI")
st.write("Main aapka personal AI assistant hoon.")

# API Key input
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Mujhse kuch bhi puchiye..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Side mein apni Gemini API Key dalein.")
