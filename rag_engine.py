import os
import tempfile
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import chromadb
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

class RAGSystem:
    def __init__(self, api_key: str):
        """Initialize the RAG system with OpenAI API key."""
        self.api_key = api_key
        os.environ["OPENAI_API_KEY"] = api_key
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        # PersistentClient writes to disk so any thread can access it
        self.chroma_dir = tempfile.mkdtemp()
        self.chroma_client = chromadb.PersistentClient(path=self.chroma_dir)

    def load_document(self, uploaded_file) -> List[Document]:
        """Load a PDF document from an uploaded file."""
        if not uploaded_file:
            return []
        
        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        try:
            loader = PyPDFLoader(tmp_file_path)
            documents = loader.load()
        finally:
            # Clean up temporary file
            os.remove(tmp_file_path)
            
        return documents

    def chunk_document(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        return text_splitter.split_documents(documents)

    def create_vector_store(self, chunks: List[Document]) -> Chroma:
        """Create a Chroma vector store on disk via PersistentClient."""
        return Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            collection_name="rag_collection",
            client=self.chroma_client
        )

    def setup_retrieval_chain(self, vector_store: Chroma, system_prompt: str):
        """Create a retrieval chain for Q&A."""
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt + "\n\nAnswer the user's question based ONLY on the following context:\n\n{context}"),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        return create_retrieval_chain(retriever, question_answer_chain)
