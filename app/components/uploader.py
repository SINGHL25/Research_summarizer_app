import streamlit as st
from backened.utils.pdf_reader import extract_text_from_pdf

def upload_pdf():
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            return text
    return None
