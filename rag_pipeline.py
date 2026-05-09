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
    docs = vectorstore.similarity_search(query, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a code assistant.

Use the following repository code context to answer the question.

CODE CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [doc.metadata["source"] for doc in docs]
    }