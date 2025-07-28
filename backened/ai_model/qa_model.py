### research_summarizer_app/backend/ai_model/qa_model.py

from transformers import pipeline
qa_pipeline = pipeline("question-answering")

def answer_question(context, question):
    result = qa_pipeline(question=question, context=context[:1000])
    return result['answer']
