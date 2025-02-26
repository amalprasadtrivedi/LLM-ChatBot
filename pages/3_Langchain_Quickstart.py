import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 Langchain Quickstart App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    st.markdown(
        """
        <style>
            .full-width-button img {
                width: 100% !important;
            }
        </style>
        <a href="https://amalprasadtrivediportfolio.vercel.app/" target="_blank" class="full-width-button">
            <img src="https://img.shields.io/badge/Created%20by-Amal%20Prasad%20Trivedi-blue">
        </a>
        """,
        unsafe_allow_html=True
    )


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "What are 3 key advice for learning how to code?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)