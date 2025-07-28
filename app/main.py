### research_summarizer_app/app/main.py

### research_summarizer_app/app/main.py
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st



from backened.ai_model.summarizer import load_summarizer
from backened.utils import pdf_reader
from app.components import uploader, summary_view, qa_view, keyword_view

st.set_page_config(page_title="AI Research Summarizer", layout="wide")
st.title("📚 AI-Powered Research Paper Summarizer")

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def load_local_summarizer():
    model_path = "backened/ai_model/distilbart_model"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    return pipeline("summarization", model=model, tokenizer=tokenizer)

pdf_text = uploader.upload_pdf()

if pdf_text:
    summary = summary_view.display_summary(pdf_text, summarizer)
    keyword_view.display_keywords(pdf_text)
    qa_view.ask_questions(pdf_text)
