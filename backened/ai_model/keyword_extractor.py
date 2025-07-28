### research_summarizer_app/backend/ai_model/keyword_extractor.py

from collections import Counter
import re

def extract_keywords(text, top_k=10):
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = set(["the", "and", "of", "in", "to", "is", "for", "that", "on", "with"])
    keywords = [w for w in words if w not in stop_words and len(w) > 3]
    return [w for w, _ in Counter(keywords).most_common(top_k)]
