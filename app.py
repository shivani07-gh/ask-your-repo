from backend.repo_loader import fetch_repo_files
from backend.embeddings import create_vector_store
from backend.rag_pipeline import ask_question

repo_name = input("Enter repo (username/repo): ")

files = fetch_repo_files(repo_name)

print("\nCreating embeddings...\n")

vectorstore = create_vector_store(files)

print("\nVECTOR DATABASE READY ")

print("\nASK QUESTIONS ABOUT THE REPO \n")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    result = ask_question(vectorstore, query)

    print("\nAI ANSWER:\n")
    print(result["answer"])

    print("\nSOURCE FILES:\n")

    for source in result["sources"]:
        print(source)

    print("\n" + "="*50 + "\n")