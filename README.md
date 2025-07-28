# Research_summarizer_app
A web app that lets users upload research papers (PDFs), summarizes the key sections (abstract, methods, results, conclusions), and visualizes the paper structure using NLP.
### research_summarizer_app/README.md

# AI Research Paper Summarizer (Streamlit App)

## Features
- 📄 Upload research PDFs
- 🤖 Generate AI summaries
- 🔍 Ask questions (QA)
- 🧠 Extract keywords

## Setup
```bash
git clone https://github.com/yourusername/research_summarizer_app.git
cd research_summarizer_app
pip install -r requirements.txt
streamlit run app/main.py
```
app/
  main.py
  components/
    uploader.py
    summary_view.py
    qa_view.py
    keyword_view.py
backend/
  ai_model/
    summarizer.py
    qa_model.py
    keyword_extractor.py
  utils/
    pdf_reader.py
