<<<<<<< HEAD

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error(" GROQ_API_KEY not found in .env file!")
    st.stop()

os.environ["GROQ_API_KEY"] = api_key


st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("RAG-Based AI Chatbot")
st.write("Upload a PDF document and ask questions about it!")
st.divider()


with st.sidebar:
    st.header(" Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload any PDF document"
    )
    
    if uploaded_file:
        st.success(f" File uploaded: {uploaded_file.name}")


if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "llm" not in st.session_state:
    st.session_state.llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7,
        groq_api_key=api_key
    )

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if uploaded_file:
    with st.spinner(" Processing PDF..."):
        
        pdf_path = f"uploaded_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = text_splitter.split_documents(documents)
        
        
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        vector_store = FAISS.from_documents(chunks, embeddings)
        st.session_state.vector_store = vector_store
        
        st.success(f" PDF processed! {len(chunks)} chunks extracted")
        st.info(f" Ready to answer questions about: {uploaded_file.name}")



if st.session_state.vector_store:
    st.subheader(" Ask Questions")
    
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    
    user_question = st.chat_input("Ask something about the document...")
    
    if user_question:
        
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_question
        })
        
        with st.chat_message("user"):
            st.markdown(user_question)
        
     
        with st.chat_message("assistant"):
            with st.spinner(" Thinking..."):
               
                relevant_docs = st.session_state.vector_store.similarity_search(
                    user_question, k=3
                )
                context = "\n".join([doc.page_content for doc in relevant_docs])
                
                
                prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided context.
If the answer is not in the context, say "I don't have that information in the document."

Context:
{context}

Question: {user_question}

Answer:"""
                
               
                response = st.session_state.llm.invoke(prompt)
                answer = response.content
                
                st.markdown(answer)
                
                
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer
                })

else:
    st.info(" Upload a PDF file from the sidebar to get started!")

st.divider()
st.caption(" Your documents are processed locally. No data is stored.")
=======
# ═══════════════════════════════════════════════════════════
# RAG-Based AI Chatbot Web App using Streamlit
# ═══════════════════════════════════════════════════════════

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in .env file!")
    st.stop()

os.environ["GROQ_API_KEY"] = api_key

# ─────────────────────────────────────────────────────────
# Streamlit UI Setup
# ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG-Based AI Chatbot")
st.write("Upload a PDF document and ask questions about it!")
st.divider()

# ─────────────────────────────────────────────────────────
# Sidebar for PDF Upload
# ─────────────────────────────────────────────────────────

with st.sidebar:
    st.header("📁 Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload any PDF document"
    )
    
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")

# ─────────────────────────────────────────────────────────
# Initialize Session State
# ─────────────────────────────────────────────────────────

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "llm" not in st.session_state:
    st.session_state.llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7,
        groq_api_key=api_key
    )

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ─────────────────────────────────────────────────────────
# Process Uploaded PDF
# ─────────────────────────────────────────────────────────

if uploaded_file:
    with st.spinner("🔄 Processing PDF..."):
        # Save uploaded file
        pdf_path = f"uploaded_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Load PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        # Split into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = text_splitter.split_documents(documents)
        
        # Create embeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Build vector store
        vector_store = FAISS.from_documents(chunks, embeddings)
        st.session_state.vector_store = vector_store
        
        st.success(f"✅ PDF processed! {len(chunks)} chunks extracted")
        st.info(f"📊 Ready to answer questions about: {uploaded_file.name}")

# ─────────────────────────────────────────────────────────
# Chat Interface
# ─────────────────────────────────────────────────────────

if st.session_state.vector_store:
    st.subheader("💬 Ask Questions")
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input box
    user_question = st.chat_input("Ask something about the document...")
    
    if user_question:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_question
        })
        
        with st.chat_message("user"):
            st.markdown(user_question)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                # Retrieve relevant chunks
                relevant_docs = st.session_state.vector_store.similarity_search(
                    user_question, k=3
                )
                context = "\n".join([doc.page_content for doc in relevant_docs])
                
                # Create prompt
                prompt = f"""You are a helpful assistant. Answer the question based ONLY on the provided context.
If the answer is not in the context, say "I don't have that information in the document."

Context:
{context}

Question: {user_question}

Answer:"""
                
                # Get response from LLM
                response = st.session_state.llm.invoke(prompt)
                answer = response.content
                
                st.markdown(answer)
                
                # Add assistant message to history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": answer
                })

else:
    st.info("👆 Upload a PDF file from the sidebar to get started!")

st.divider()
st.caption("🔐 Your documents are processed locally. No data is stored.")
>>>>>>> 71a728e1e4ae005c49b7de29d049adc7c81cd51b
