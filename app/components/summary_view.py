### research_summarizer_app/app/components/summary_view.py

import streamlit as st
from backened.ai_model.summarizer import generate_summary

def display_summary(text):
    st.header("🔍 Summary")
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = generate_summary(text)
            st.success("Summary ready!")
            st.write(summary)
            return summary
