# RAG-The-Enterprise-brain
🧠 Enterprise Brain: Private RAG Infrastructure
Enterprise Brain is a secure, Retrieval-Augmented Generation (RAG) system designed for businesses to interact with their proprietary documentation without compromising data privacy.

Built with a focus on auditability, the system provides precise answers backed by document citations, effectively eliminating AI hallucinations in a corporate context.

🚀 Core Features
Semantic Data Retrieval: Uses Vector Embeddings (ChromaDB) to understand the meaning of queries rather than just matching keywords.

Automatic Source Attribution: Every response includes the specific document name and page number used to generate the answer.

Privacy-First Architecture: Designed to bridge private local data with LLMs, ensuring enterprise secrets aren't used for training public models.

Smart Document Processing: Automated pipeline for PDF ingestion, recursive character chunking, and metadata tagging.

🛠️ The Tech Stack
Language: Python 3.10+

AI Orchestration: LangChain

Vector Database: ChromaDB

LLM Integration: OpenAI GPT-4o / GPT-4 Turbo

Backend Framework: Flask

Frontend: HTML5, CSS3, Bootstrap

📂 Project Structure
Plaintext
.
├── app.py              # Flask Web Server & Routing
├── rag_engine.py       # RAG Logic (Chunking, Embedding, Retrieval)
├── templates/          # Frontend HTML Chat Interface
├── db/                 # Persistent Vector Storage (Local)
├── uploads/            # Temporary storage for processed PDFs
└── requirements.txt    # Project Dependencies
⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/enterprise-brain.git
cd enterprise-brain
Set up a Virtual Environment:

Bash
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file in the root directory and add your key:

Plaintext
OPENAI_API_KEY=your_api_key_here
Run the Application:

Bash
python app.py
The app will be available at http://127.0.0.1:5000