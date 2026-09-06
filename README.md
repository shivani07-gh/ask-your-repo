# 🚀 AskYourRepo

### AI-Powered GitHub Repository Understanding Tool

**AskYourRepo** helps developers understand unfamiliar GitHub repositories using AI-powered code search, architecture analysis, dependency visualization, and repository-specific learning roadmaps.

Instead of manually exploring a large codebase, developers can load a repository and interact with it through a single intelligent interface.

---

## ✨ Features

### 💬 AI-Powered Code Q&A
Ask natural-language questions about a repository and receive context-aware answers based on the actual codebase.

### 🔎 RAG-Based Code Search
Uses embeddings and vector search to retrieve relevant code before generating answers, improving the relevance of responses.

### 🏗️ Architecture Visualization
Automatically analyzes repository files and organizes them into architectural layers such as **Frontend, Backend, AI, and Database**.

### 🔗 Dependency Analysis
Extracts dependencies and identifies relationships between different parts of the repository.

### 🧩 File Role Classification
Classifies source files according to their architectural role and provides confidence information for the classification.

### 📚 Learning Roadmap
Generates a structured learning roadmap to help developers understand and learn an unfamiliar repository step by step.

---

## ⚙️ How It Works

```text
                         ┌─────────────────────┐
                         │   GitHub Repository │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Repository Loader  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Source Files    │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┴──────────────────┐
                 ▼                                     ▼
        ┌─────────────────┐                  ┌─────────────────────┐
        │   RAG Pipeline  │                  │ Architecture Engine │
        └────────┬────────┘                  └──────────┬──────────┘
                 │                                      │
                 ▼                                      ▼
        ┌─────────────────┐                  ┌─────────────────────┐
        │   Embeddings    │                  │ File Classification │
        └────────┬────────┘                  └──────────┬──────────┘
                 │                                      │
                 ▼                                      ▼
        ┌─────────────────┐                  ┌─────────────────────┐
        │   Vector Store  │                  │ Dependency Analysis │
        └────────┬────────┘                  └──────────┬──────────┘
                 │                                      │
                 ▼                                      ▼
        ┌─────────────────┐                  ┌─────────────────────┐
        │ Code Retrieval  │                  │ Architecture Graph │
        └────────┬────────┘                  └──────────┬──────────┘
                 │                                      │
                 └──────────────────┬───────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │   FastAPI Backend   │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
               💬 Q&A        🏗️ Architecture   📚 Roadmap
🛠️ Tech Stack
Backend
🐍 Python
⚡ FastAPI
📦 Pydantic
🐙 PyGithub
AI & Retrieval
🦜 LangChain
🧠 Embeddings
⚡ FAISS
🔎 Vector Search
🔄 Retrieval-Augmented Generation (RAG)
🤖 Large Language Models
Frontend
🌐 HTML
🎨 CSS
⚡ JavaScript
📊 SVG
Integration
🐙 GitHub API
📁 Project Structure
AskYourRepo/
│
├── backend/
│   ├── data/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── embeddings.py
│   ├── rag_pipeline.py
│   ├── repo_loader.py
│   ├── roadmap_generator.py
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── main.js
│   ├── style.css
│   ├── architecture.html
│   ├── architecture.js
│   └── architecture.css
│
├── requirements.txt
├── .env
└── README.md
🔌 API Endpoints
Endpoint	Method	Description
/load-repo	POST	Load and process a GitHub repository
/ask	POST	Ask questions about the repository
/users/{username}/repos	GET	Fetch repositories for a GitHub user
/visualize	GET	Generate repository architecture
/generate-roadmap	GET	Generate a learning roadmap
📄 Supported Files

AskYourRepo currently processes common source-code files:

.py
.js
.ts
.jsx
.tsx
.java
.cpp
🚀 Getting Started
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd AskYourRepo
2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the project root:

GITHUB_TOKEN=your_github_token
OPENAI_API_KEY=your_openai_api_key
5. Start the Backend
uvicorn backend.main:app --reload

The backend will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
6. Run the Frontend

Serve the frontend using a local web server and open the application in your browser.

🎯 Use Cases
🧑‍💻 Understanding unfamiliar codebases
🚀 Developer onboarding
🌐 Exploring open-source repositories
🔍 Finding implementation details quickly
🏗️ Visualizing project architecture
📚 Learning new projects and technologies
🤝 Helping developers navigate large repositories
💡 Why AskYourRepo?

Understanding a new repository often requires manually navigating files, tracing dependencies, identifying architecture, and figuring out where different components fit together.

AskYourRepo brings these tasks into one place.

Load a repository → Understand its architecture → Ask questions → Explore dependencies → Learn the codebase

🔮 Future Improvements
🔗 File-level dependency graphs
🧠 Improved architecture detection
🌍 Support for additional programming languages
⚡ Incremental repository indexing
🔎 Advanced code search
📊 Repository complexity analysis
🧹 Automated code quality insights
📜 License

This project is developed for educational and experimental purposes.

<div align="center">
🚀 AskYourRepo

Understand repositories. Don't just read them.

</div> ```
