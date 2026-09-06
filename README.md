# AskYourRepo

### AI-Powered GitHub Repository Understanding & Architecture Analysis

AskYourRepo is an AI-powered developer tool that helps engineers understand unfamiliar GitHub repositories faster.

It combines **Retrieval-Augmented Generation (RAG)**, **vector search**, **dependency analysis**, and **architecture visualization** to turn a repository into an interactive, searchable knowledge base.

Instead of manually navigating hundreds of files, developers can load a repository, ask questions about its implementation, visualize its architecture, and generate a learning roadmap from the codebase itself.

---

## Overview

Understanding an unfamiliar repository usually requires:

- Exploring large numbers of files
- Finding where specific functionality is implemented
- Tracing dependencies between modules
- Understanding the overall architecture
- Identifying technologies and components
- Figuring out what to learn before modifying the project

AskYourRepo automates these steps through a unified interface.

**Repository → Code Understanding → Retrieval → Architecture → Insights**

---

## Core Capabilities

### 1. Repository-Aware AI Q&A

Load a GitHub repository and ask questions in natural language.

Examples:

```text
"How does authentication work?"

"Where is the API request handled?"

"How is the database connected?"

"Which files implement the RAG pipeline?"

The system retrieves relevant code from the repository before generating the answer, making responses specific to the selected codebase.

2. Retrieval-Augmented Generation

The repository source code is processed into embeddings and stored in a vector database.

When a question is asked:

User Question
      ↓
Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Code Chunks
      ↓
LLM
      ↓
Context-Aware Answer

This allows the model to answer questions using the actual repository context rather than relying only on its pretrained knowledge.

3. Architecture Visualization

AskYourRepo analyzes repository files and classifies them into architectural layers such as:

Frontend
Backend
AI
Database

It then builds an interactive architecture graph showing relationships between the major components of the repository.

Selecting a layer provides additional information about the files belonging to that component.

4. Dependency Analysis

The system extracts imports and dependencies from source files and uses them to identify relationships between different parts of the repository.

This helps developers understand:

Which component depends on what?
Where does a particular module connect?
How are different architectural layers related?
5. File Role Classification

Repository files are analyzed and classified according to their likely architectural role.

The classification system considers:

File path
File extension
Source-code patterns
Framework-specific indicators
Architectural keywords

The resulting classification includes confidence information, allowing the architecture engine to build a more meaningful representation of the repository.

6. Repository Learning Roadmap

AskYourRepo can generate a structured learning roadmap based on the technologies, components, and source files present in the repository.

This provides developers with a practical sequence for understanding an unfamiliar project.

System Architecture
                         GitHub Repository
                                │
                                ▼
                       ┌──────────────────┐
                       │ Repository Loader │
                       └────────┬─────────┘
                                │
                         Source Code Files
                                │
                ┌───────────────┴────────────────┐
                │                                │
                ▼                                ▼
        ┌─────────────────┐              ┌────────────────────┐
        │   RAG Pipeline  │              │ Architecture Engine│
        └────────┬────────┘              └─────────┬──────────┘
                 │                                 │
                 ▼                                 ▼
          Code Chunking                    File Classification
                 │                                 │
                 ▼                                 ▼
           Embeddings                     Dependency Extraction
                 │                                 │
                 ▼                                 ▼
          Vector Store                    Architecture Graph
                 │                                 │
                 └───────────────┬─────────────────┘
                                 ▼
                         FastAPI Backend
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
          AI Q&A          Architecture        Learning
                          Visualization        Roadmap
Tech Stack
Layer	Technologies
Backend	Python, FastAPI, Pydantic
AI / LLM	LangChain, Large Language Models
Retrieval	Embeddings, FAISS, Vector Search, RAG
Repository Integration	GitHub API, PyGithub
Frontend	HTML, CSS, JavaScript
Visualization	SVG
Configuration	Python-dotenv
Project Structure
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
API
Endpoint	Method	Purpose
/load-repo	POST	Loads and processes the selected GitHub repository
/ask	POST	Answers questions using repository context
/users/{username}/repos	GET	Retrieves repositories for a GitHub user
/visualize	GET	Generates repository architecture data
/generate-roadmap	GET	Generates a repository-specific learning roadmap
Supported Source Files

The current repository loader supports:

Python       .py
JavaScript   .js
TypeScript   .ts
React        .jsx / .tsx
Java         .java
C++          .cpp
Getting Started
Prerequisites
Python 3.10+
Git
GitHub Personal Access Token
LLM API key
Installation
git clone YOUR_GITHUB_REPOSITORY_URL
cd AskYourRepo

Create and activate a virtual environment:

Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file:

GITHUB_TOKEN=your_github_token
OPENAI_API_KEY=your_openai_api_key

Start the backend:

uvicorn backend.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
Example Workflow
1. Select a GitHub repository
            ↓
2. Repository files are fetched
            ↓
3. Source code is processed
            ↓
4. Embeddings are generated
            ↓
5. Vector store is created
            ↓
6. Repository becomes searchable
            ↓
7. Ask questions about the codebase
            ↓
8. Explore generated architecture
            ↓
9. Follow the generated learning roadmap
Why This Project?

AskYourRepo combines multiple developer-focused AI capabilities into one workflow:

Code Retrieval + RAG + Dependency Analysis + Architecture Understanding + Learning Assistance

The goal is to reduce the time required to understand an unfamiliar codebase and make repository exploration more accessible for developers.

Future Scope
File-level dependency graphs
AST-based code analysis
Support for additional programming languages
Incremental repository indexing
Repository complexity and code-quality analysis
More detailed architecture inference
Improved cross-file reasoning
License

This project is developed for educational and experimental purposes.

AskYourRepo — Understand a codebase before you change it.
