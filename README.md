# Enterprise Knowledge Engine (RAG)

## Project Title: Enterprise Knowledge Engine (RAG)

**Problem:** Professionals spend too much time manually searching through long PDFs (contracts, manuals, reports) for specific answers.

**Solution:** A Retrieval-Augmented Generation (RAG) system that grounded AI responses in company-specific data.

**ROI:**
*   **Speed:** Reduces information retrieval time by 80%.
*   **Accuracy:** Eliminates AI hallucinations by using strict source grounding.
*   **Scalability:** Allows non-technical staff to query complex data using natural language.

## Getting Started

### Prerequisites

*   Python 3.10+
*   OpenAI API Key

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/edfinch1/The-Context-Aware-Agent-RAG-.git
    cd The-Context-Aware-Agent-RAG-
    ```

2.  Create and Activate Virtual Environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up Environment Variables:
    Create a `.env` file in the root directory and add your OpenAI API Key:
    ```bash
    OPENAI_API_KEY=sk-your-openai-api-key
    ```

### Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

1.  **Upload:** Upload a PDF document via the sidebar.
2.  **Configure:** Choose a system persona (e.g., "Strict Legal Auditor").
3.  **Chat:** Ask questions about the document. The AI will answer based ONLY on the document content and provide citations.
