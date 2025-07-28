import streamlit as st
from app.components.upload_pdf import upload_pdf_ui
from app.components.summary_view import display_summary
from app.components.visualize_sections import display_visualization

st.set_page_config(page_title="Research Paper Summarizer", layout="wide")
st.title("📚 Research Paper Summarizer")

# Upload
pdf_text = upload_pdf_ui()

# Summarize & Display
if pdf_text:
    display_summary(pdf_text)
    display_visualization(pdf_text)

