### research_summarizer_app/app/components/qa_view.py

import streamlit as st
from backend.ai_model.qa_model import answer_question

def ask_questions(context):
    st.header("❓ Ask Questions")
    question = st.text_input("Enter a question about the paper")
    if question:
        with st.spinner("Answering..."):
            answer = answer_question(context, question)
            st.write(f"**Answer:** {answer}")
