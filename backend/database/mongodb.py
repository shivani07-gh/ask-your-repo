import os
import certifi

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv


load_dotenv()


MONGO_URL = os.getenv("MONGO_URL")


client = AsyncIOMotorClient(
    MONGO_URL,
    tlsCAFile=certifi.where()
)


database = client["ask_your_repo_db"]

users_collection = database["users"]


async def connect_db():

    try:

        await client.admin.command("ping")

        print("MongoDB Connected Successfully 🚀")


    except Exception as e:

        print("MongoDB Connection Failed ❌")
        print(e)