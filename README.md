# 🤖 RAG-Based AI Chatbot

An AI chatbot that reads PDF documents and answers questions about them using LangChain, FAISS, and Groq LLM.

##  Live Demo
(You'll add the Streamlit link here after deployment)

## What it does
- Upload any PDF document
- Ask questions about the content
- AI answers based ONLY on the document
- Maintains chat history

## How it works
1. **PDF Loading** — Reads PDF using PyPDFLoader
2. **Chunking** — Splits document into searchable chunks
3. **Embeddings** — Converts text to vector embeddings
4. **FAISS Database** — Stores embeddings for fast search
5. **RAG Retrieval** — Finds relevant chunks for questions
6. **LLM Generation** — Groq AI generates answers

## Tech Stack
- **Python** — Backend
- **Streamlit** — Web interface
- **LangChain** — AI orchestration
- **FAISS** — Vector database
- **HuggingFace** — Embeddings
- **Groq API** — Free LLM (llama, gpt-oss models)

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Environment Variables
Create `.env` file:
