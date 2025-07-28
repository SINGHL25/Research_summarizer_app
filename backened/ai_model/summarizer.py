### research_summarizer_app/backend/ai_model/summarizer.py

from transformers import pipeline
summarizer = pipeline("summarization")

def generate_summary(text):
    return summarizer(text[:1000])[0]['summary_text']
