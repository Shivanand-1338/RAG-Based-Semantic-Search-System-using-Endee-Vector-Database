📚 RAG-Based Semantic Search System using Endee Vector Database
🚀 Project Overview

This project implements a Retrieval Augmented Generation (RAG) system that enables semantic search and question answering over unstructured documents.
The core of the system is the Endee Vector Database, which stores document embeddings and performs fast similarity-based retrieval.

Instead of relying on keyword matching, the system understands the semantic meaning of user queries and retrieves the most relevant content.

🎯 Problem Statement

Traditional keyword-based search systems fail to capture semantic relationships between words and often return irrelevant results.
This project addresses that limitation by using vector embeddings and similarity search, allowing users to retrieve accurate and context-aware information from documents.

🧠 Use Cases Demonstrated
1️⃣ Semantic Search

Retrieves documents based on semantic similarity, not exact keyword matches.

Enables more accurate and flexible information retrieval.

2️⃣ Retrieval Augmented Generation (RAG)

Relevant document chunks are retrieved from the Endee Vector Database.

The retrieved context is used to generate informed responses.

Reduces hallucination and improves answer accuracy.

🔮 Future Extensions

Recommendation systems using vector similarity

Agentic AI workflows with memory and tool execution

Integration with cloud-based LLMs when API access is available

🏗 System Architecture
Documents
   ↓
Text Chunking
   ↓
Local Embedding Generation
   ↓
Endee Vector Database
   ↓
Semantic Similarity Search
   ↓
Context Retrieval
   ↓
Answer Generation

📦 Role of Endee Vector Database

Endee is used as the core vector database in this project.

It is responsible for:

Storing high-dimensional document embeddings

Performing fast cosine similarity search

Enabling semantic retrieval for RAG workflows

Persisting data using Docker volumes

Endee ensures scalable and efficient vector search, which is critical for AI-driven applications.

🛠 Tech Stack

Programming Language: Python

Vector Database: Endee (Docker-based)

Embedding Model: Local transformer embeddings

Frontend: Streamlit

Containerization: Docker & Docker Compose

⚙️ Setup & Installation
1️⃣ Prerequisites

Docker Desktop (running)

Python 3.10+

At least 2 GB RAM

Port 8080 available

2️⃣ Start Endee Server
docker compose up -d


Verify:

docker ps


Access dashboard:

http://localhost:8080

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Create Vector Index (Run Once)
python src/create_index.py


⚠️ Index creation is a one-time operation.
Running it again will raise a conflict error, which is expected behavior.

5️⃣ Ingest Documents
python src/ingest.py


This step:

Splits documents into chunks

Generates embeddings

Stores vectors in Endee

6️⃣ Run the Application
streamlit run app.py

🧪 Example Queries
What is machine learning?
Explain semantic search.
What is Retrieval Augmented Generation?
What is the role of vector databases?

📁 Project Structure
Endee-RAG-System/
│
├── data/
│   └── documents/
│       └── sample.txt
│
├── src/
│   ├── create_index.py
│   ├── ingest.py
│   ├── search.py
│   └── rag.py
│
├── app.py
├── requirements.txt
├── docker-compose.yml
└── README.md

🧠 Key Learnings

Vector databases are essential for semantic search and RAG pipelines

Index lifecycle management is critical in production systems

Decoupling retrieval and generation improves system reliability

Local embeddings enable offline, stable AI workflows

✅ Conclusion

This project demonstrates a practical and scalable AI application where vector search is the core component.
By combining local embeddings with the Endee Vector Database, the system delivers accurate semantic search and RAG functionality suitable for real-world use cases.