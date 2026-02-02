import streamlit as st
from src.rag import generate_answer

st.set_page_config(page_title="Endee + Gemini RAG Agent")

st.title("🤖 RAG Agent using Endee & Gemini")

query = st.text_input("Ask a question from the documents")

if query:
    with st.spinner("Thinking..."):
        answer = generate_answer(query)
    st.success(answer)
