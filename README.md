# AskYourRepo

### AI-Powered GitHub Repository Understanding & Architecture Analysis

AskYourRepo is an AI-powered developer tool that helps engineers
understand unfamiliar GitHub repositories faster.

It combines **Retrieval-Augmented Generation (RAG), vector search,
dependency analysis, architecture visualization, and repository-specific
learning roadmaps** into a single workflow.

Instead of manually navigating a large codebase, developers can load a
repository, ask questions about its implementation, explore its
architecture, trace dependencies, and generate a learning roadmap from
the repository itself.

------------------------------------------------------------------------

## Overview

Understanding an unfamiliar codebase often requires manually exploring
files, tracing dependencies, identifying architectural components, and
locating the implementation of specific features.

AskYourRepo streamlines this process by turning a GitHub repository into
an interactive, searchable knowledge base.

The system allows developers to:

-   Ask natural-language questions about a repository
-   Retrieve relevant source-code context
-   Explore the repository architecture
-   Analyze dependencies between components
-   Classify files according to their architectural role
-   Generate a repository-specific learning roadmap

------------------------------------------------------------------------

## Key Features

### AI-Powered Repository Q&A

Ask natural-language questions about the selected repository and receive
answers grounded in the actual source code.

Example questions:

-   How does authentication work?
-   Where is the API request handled?
-   How is the database connected?
-   Where is the RAG pipeline implemented?

### Retrieval-Augmented Generation

The repository source code is processed into embeddings and stored in a
vector database. When a user asks a question, relevant code is retrieved
and provided as context to the language model.

``` text
User Question
      ↓
Query Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Code Chunks
      ↓
LLM + Retrieved Context
      ↓
Context-Aware Answer
```

This enables repository-specific responses instead of relying only on
general model knowledge.

### Architecture Visualization

AskYourRepo analyzes repository files and organizes them into
architectural layers such as:

-   Frontend
-   Backend
-   AI
-   Database

The system then generates an interactive architecture graph that helps
developers understand how major components of the repository relate to
each other.

### Dependency Analysis

Source files are analyzed to extract imports and dependencies.

This helps developers understand relationships between modules and
identify how different architectural layers interact.

### File Role Classification

Repository files are classified according to their likely architectural
role using signals such as:

-   File path
-   File extension
-   Source-code patterns
-   Framework-specific indicators
-   Architectural keywords

Classification confidence is also maintained to support more reliable
architecture analysis.

### Repository Learning Roadmap

AskYourRepo can generate a structured learning roadmap based on the
technologies, components, and structure detected in the repository.

This provides developers with a practical sequence for understanding an
unfamiliar project.

------------------------------------------------------------------------

## System Architecture

``` text
                         GitHub Repository
                                │
                                ▼
                       ┌──────────────────┐
                       │ Repository Loader │
                       └────────┬─────────┘
                                │
                                ▼
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
          Code Processing                  File Classification
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
```

------------------------------------------------------------------------

## RAG Pipeline

``` text
Repository Files
      ↓
File Processing
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Similarity Retrieval
      ↓
Relevant Context
      ↓
LLM
      ↓
Generated Answer
```

------------------------------------------------------------------------

## Architecture Analysis Pipeline

``` text
Repository Files
      ↓
File Role Classification
      ↓
Architectural Layers
      ↓
Dependency Extraction
      ↓
Dependency Graph
      ↓
Interactive Architecture Visualization
```

------------------------------------------------------------------------

## Tech Stack

  Category                 Technologies
  ------------------------ ---------------------------------------
  Backend                  Python, FastAPI, Pydantic
  AI / LLM                 LangChain, Large Language Models
  Retrieval                Embeddings, FAISS, Vector Search, RAG
  Repository Integration   GitHub API, PyGithub
  Frontend                 HTML, CSS, JavaScript
  Visualization            SVG
  Configuration            Python-dotenv

------------------------------------------------------------------------

## Project Structure

``` text
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
```

------------------------------------------------------------------------

## API Endpoints

  ---------------------------------------------------------------------------
  Endpoint                    Method                  Description
  --------------------------- ----------------------- -----------------------
  `/load-repo`                POST                    Load and process a
                                                      GitHub repository

  `/ask`                      POST                    Ask questions using
                                                      repository context

  `/users/{username}/repos`   GET                     Retrieve repositories
                                                      for a GitHub user

  `/visualize`                GET                     Generate repository
                                                      architecture

  `/generate-roadmap`         GET                     Generate a
                                                      repository-specific
                                                      learning roadmap
  ---------------------------------------------------------------------------

------------------------------------------------------------------------

## Supported Source Files

The current repository loader supports:

``` text
Python       .py
JavaScript   .js
TypeScript   .ts
React        .jsx / .tsx
Java         .java
C++          .cpp
```

------------------------------------------------------------------------

## Getting Started

### Prerequisites

-   Python 3.10+
-   Git
-   GitHub Personal Access Token
-   LLM API Key

### Installation

Clone the repository:

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AskYourRepo
```

Create a virtual environment.

**Windows**

``` bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

``` bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

``` env
GITHUB_TOKEN=your_github_token
OPENAI_API_KEY=your_openai_api_key
```

### Run the Backend

``` bash
uvicorn backend.main:app --reload
```

The API will be available at:

``` text
http://127.0.0.1:8000
```

Interactive API documentation:

``` text
http://127.0.0.1:8000/docs
```

### Run the Frontend

Serve the frontend using a local web server and open the application in
your browser.

------------------------------------------------------------------------

## Workflow

``` text
Select GitHub Repository
          ↓
Fetch Repository Files
          ↓
Process Source Code
          ↓
   ┌──────┴───────┐
   ↓              ↓
RAG Pipeline   Architecture Analysis
   ↓              ↓
Embeddings     File Classification
   ↓              ↓
Vector Store   Dependency Analysis
   ↓              ↓
Code Retrieval Architecture Graph
   └──────┬───────┘
          ↓
   Developer Interface
          ↓
   ┌──────┼───────┐
   ↓      ↓       ↓
  Q&A  Architecture Roadmap
```

------------------------------------------------------------------------

## Use Cases

-   Understanding unfamiliar codebases
-   Developer onboarding
-   Exploring open-source projects
-   Finding implementation details quickly
-   Tracing dependencies
-   Visualizing project architecture
-   Learning a new repository faster

------------------------------------------------------------------------

## Why AskYourRepo?

AskYourRepo brings multiple developer workflows into one system:

**Code Search + RAG + Dependency Analysis + Architecture Understanding +
Learning Assistance**

The goal is to reduce the time and effort required to understand an
unfamiliar codebase before making changes to it.

------------------------------------------------------------------------

## Future Scope

-   AST-based code analysis
-   File-level dependency graphs
-   Support for additional programming languages
-   Incremental repository indexing
-   Repository complexity analysis
-   Automated code-quality insights
-   Improved cross-file reasoning

------------------------------------------------------------------------

## License

This project is developed for educational and experimental purposes.

------------------------------------------------------------------------


### AskYourRepo

**Understand a codebase before you change it.**


