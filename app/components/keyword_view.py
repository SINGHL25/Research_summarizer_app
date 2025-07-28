### research_summarizer_app/app/components/keyword_view.py

import streamlit as st
from backened.ai_model.keyword_extractor import extract_keywords

def display_keywords(text):
    st.header("🔑 Keywords")
    keywords = extract_keywords(text)
    st.write(keywords)
