import streamlit as st
import fitz  # PyMuPDF

def upload_pdf():
    uploaded_file = st.file_uploader("📤 Upload Research Paper (PDF)", type="pdf")

    if uploaded_file is not None:
        try:
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
            st.success("✅ PDF successfully uploaded and text extracted.")
            return text
        except Exception as e:
            st.error(f"❌ Failed to process PDF: {e}")
            return None
    return None
