### research_summarizer_app/app/main.py

### research_summarizer_app/app/main.py

import sys
import os
import torch

# Add the parent directory (project root) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.components import uploader, summary_view, qa_view, keyword_view
from backened.ai_model import summarizer
from backened.utils import pdf_reader
from app.components import uploader, summary_view, qa_view, keyword_view


st.set_page_config(page_title="AI Research Summarizer", layout="wide")
st.title("📚 AI-Powered Research Paper Summarizer")

pdf_text = uploader.upload_pdf()

if pdf_text:
    summary = summary_view.display_summary(pdf_text)
    keyword_view.display_keywords(pdf_text)
    qa_view.ask_questions(pdf_text)

### research_summarizer_app/app/components/uploader.py

import streamlit as st
from backened.utils.pdf_reader import extract_text_from_pdf

def upload_pdf():
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            return text
    return None
