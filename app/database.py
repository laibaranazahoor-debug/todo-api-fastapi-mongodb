
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME", "todo_database")

if not MONGODB_URL:
    raise RuntimeError("MONGODB_URL is missing from .env")

client = MongoClient(
    MONGODB_URL,
    serverSelectionTimeoutMS=5000
)

database = client[DATABASE_NAME]
todos_collection = database["todos"]


def check_database_connection():
    client.admin.command("ping")
    return True
