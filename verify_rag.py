"""
Terminal test for the RAG system using the Acme Corp PDF and .env API key.
"""
import os
from dotenv import load_dotenv
from rag_engine import RAGSystem

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found in .env")
    exit(1)

PDF_PATH = "acme_corp_policy_manual.pdf"
if not os.path.exists(PDF_PATH):
    print(f"ERROR: {PDF_PATH} not found. Run generate_test_pdf.py first.")
    exit(1)

print("Initialising RAG system...")
rag = RAGSystem(api_key)

print("Loading PDF...")
with open(PDF_PATH, "rb") as f:
    docs = rag.load_document(f)
print(f"  Loaded {len(docs)} pages")

print("Chunking...")
chunks = rag.chunk_document(docs)
print(f"  Created {len(chunks)} chunks")

print("Building vector store (ChromaDB EphemeralClient)...")
vs = rag.create_vector_store(chunks)
print("  Vector store ready")

print("\nSetting up retrieval chain (Strict Legal Auditor persona)...")
persona = "You are a strict legal auditor. Answer with precision, citing specific clauses. Do not speculate."
chain = rag.setup_retrieval_chain(vs, persona)

QUESTIONS = [
    "What is the maximum redundancy payout for an employee with 8 years of service?",
    "Can an L3 employee claim business class on a 5-hour domestic flight?",
    "How many EAP counselling sessions am I entitled to per year?",
]

print("\n" + "="*60)
for q in QUESTIONS:
    print(f"\nQ: {q}")
    result = chain.invoke({"input": q})
    print(f"A: {result['answer']}")
    if result.get("context"):
        pages = [str(d.metadata.get("page", "?")) for d in result["context"]]
        print(f"   [Sources: pages {', '.join(pages)}]")
    print("-"*60)

print("\nAll tests passed!")
