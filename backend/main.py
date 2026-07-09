from pathlib import Path
from dotenv import load_dotenv

# ======================================
# LOAD ENV VARIABLES
# ======================================

env_path = Path(__file__).resolve().parent / ".env"

if not env_path.exists():
    env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(
    dotenv_path=env_path,
    override=True
)


# ======================================
# IMPORTS
# ======================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Database
from backend.database.mongodb import connect_db


# Routes
import backend.routes.repos as repos
import backend.routes.ask as ask
import backend.routes.roadmap as roadmap

from backend.routes.architecture_routes import (
    router as architecture_router
)

# import backend.routes.dependencies as dependencies


# ======================================
# APP INITIALIZATION
# ======================================

app = FastAPI(
    title="AskYourRepo API"
)


# ======================================
# DATABASE CONNECTION
# ======================================

@app.on_event("startup")
async def startup_db():

    await connect_db()


# ======================================
# CORS
# ======================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ======================================
# ROUTERS
# ======================================

app.include_router(
    repos.router
)

app.include_router(
    ask.router
)

app.include_router(
    roadmap.router
)

app.include_router(
    architecture_router
)

# app.include_router(dependencies.router)


# ======================================
# HOME ROUTE
# ======================================

@app.get("/")
def home():

    return {
        "message":
        "AskYourRepo API Running 🚀"
    }