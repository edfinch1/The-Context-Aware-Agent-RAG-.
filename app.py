import streamlit as st
import os
from rag_engine import RAGSystem
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Context-Aware RAG Agent",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for polished look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
    }
    .stChatInput {
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    if "rag_system" not in st.session_state:
        st.session_state.rag_system = None

initialize_session_state()

# Sidebar
with st.sidebar:
    st.title("brain.config")
    
    # API Key Handling
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = st.text_input("OpenAI API Key", type="password")
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("API Key loaded!")
    else:
        st.success("API Key loaded from environment")

    # Persona Selection
    persona = st.selectbox(
        "Agent Persona",
        ("Strict Legal Auditor", "Technical Writer", "Helpful Onboarding Buddy")
    )
    
    system_prompts = {
        "Strict Legal Auditor": "You are a strict legal auditor. Answer with precision, citing specific clauses. Do not speculate.",
        "Technical Writer": "You are a technical writer. Explain complex concepts clearly and concisely. Use formatting effectively.",
        "Helpful Onboarding Buddy": "You are a helpful onboarding buddy. Be welcoming, encouraging, and explain things in simple terms."
    }
    
    selected_prompt = system_prompts[persona]

    # File Upload
    st.divider()
    st.subheader("Data Ingestion")
    uploaded_file = st.file_uploader("Upload a PDF Document", type=("pdf"))

    if uploaded_file and st.button("Process Document") and api_key:
        with st.spinner("Processing document..."):
            try:
                # Initialize RAG System
                rag = RAGSystem(api_key)
                st.session_state.rag_system = rag
                
                # Process
                documents = rag.load_document(uploaded_file)
                chunks = rag.chunk_document(documents)
                vector_store = rag.create_vector_store(chunks)
                
                # Save to session state
                st.session_state.vector_store = vector_store
                st.success(f"Processed {len(chunks)} chunks!")
            except Exception as e:
                st.error(f"Error processing document: {str(e)}")

# Main Chat Interface
st.title("Context-Aware Knowledge Agent")

if not st.session_state.vector_store:
    st.info("👈 upload a PDF to get started.")
else:
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask a question about your document..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    rag = st.session_state.rag_system
                    vector_store = st.session_state.vector_store
                    
                    chain = rag.setup_retrieval_chain(vector_store, selected_prompt)
                    response = chain.invoke({"input": prompt})
                    
                    answer = response["answer"]
                    sources = response.get("context", [])
                    
                    # Display Answer
                    st.markdown(answer)
                    
                    # Display Sources
                    if sources:
                        with st.expander("View Sources"):
                            for i, doc in enumerate(sources):
                                st.markdown(f"**Source {i+1} (Page {doc.metadata.get('page_label', list(doc.metadata.values())[0] if doc.metadata else '?')}):**")
                                st.markdown(f"> {doc.page_content}")
                    
                    # Add assistant message to history
                    st.session_state.messages.append({"role": "assistant", "content": answer})

                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
