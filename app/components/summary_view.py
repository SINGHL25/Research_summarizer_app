### research_summarizer_app/app/components/summary_view.py

import streamlit as st

def display_summary(text, summarizer):
    with st.spinner("Generating summary..."):
        summary_result = summarizer(text, max_length=150, min_length=40, do_sample=False)
        summary_text = summary_result[0]['summary_text']
        st.markdown("### Summary")
        st.write(summary_text)
        return summary_text
