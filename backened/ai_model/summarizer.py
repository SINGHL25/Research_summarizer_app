### research_summarizer_app/backend/ai_model/summarizer.py

import streamlit as st
from transformers import pipeline

@st.cache_resource(show_spinner=False)
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

