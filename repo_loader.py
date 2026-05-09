from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

g = Github(token)


def fetch_repo_files(repo_name):

    repo = g.get_repo(repo_name)

    all_files = []

    def read_contents(path=""):

        contents = repo.get_contents(path)

        for content in contents:

            # Folder
            if content.type == "dir":
                read_contents(content.path)

            # File
            else:

                # Optional filtering
                if content.name.endswith((
                    ".py",
                    ".js",
                    ".ts",
                    ".jsx",
                    ".tsx",
                    ".java",
                    ".cpp"
                )):

                    try:

                        file_data = {
                            "path": content.path,
                            "content": content.decoded_content.decode("utf-8")
                        }

                        all_files.append(file_data)

                        print("Loaded:", content.path)

                    except Exception as e:
                        print("Error reading", content.path)

    read_contents()

    return all_files