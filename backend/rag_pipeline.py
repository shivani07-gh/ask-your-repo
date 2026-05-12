from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")


def ask_question(vectorstore, query):

    llm = ChatNVIDIA(
        model="mistralai/mixtral-8x7b-instruct-v0.1",
        api_key=api_key,
        temperature=0
    )

    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(query, k=6)

    context = "\n\n".join([
        f"FILE: {doc.metadata['source']}\n{doc.page_content}"
        for doc in docs
    ])

    prompt = f"""
You are an expert software engineer and codebase analyst.

Your task is to analyze the provided GitHub repository code context
and answer the user's question accurately.

Instructions:
- Explain clearly and technically.
- Mention important files involved.
- If the answer is not available in context, say so honestly.
- Keep answers concise but useful.
- Focus only on repository-related information.

REPOSITORY CODE:

{context}

USER QUESTION:
{query}

DETAILED ANSWER:
"""

    response = llm.invoke(prompt)

    # Remove duplicate source files
    unique_sources = list(set([
        doc.metadata["source"]
        for doc in docs
    ]))

    return {
        "answer": response.content,
        "sources": unique_sources
    }