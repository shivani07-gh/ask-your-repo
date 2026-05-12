from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Ask Your Repo Backend Running "
    }