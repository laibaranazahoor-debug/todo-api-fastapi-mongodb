
import os

from fastapi import FastAPI, HTTPException
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

from app.database import check_database_connection
from app.routes.todos import router as todos_router

load_dotenv()

app = FastAPI(
    title="To-Do List API",
    description="A CRUD API built with FastAPI and MongoDB Atlas",
    version="1.0.0"
)

app.include_router(todos_router)


@app.get("/")
def home():
    return {"message": "Welcome to the To-Do List API"}


@app.get("/health")
def health_check():
    try:
        check_database_connection()
        return {
            "status": "healthy",
            "database": "connected"
        }
    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database connection failed"
        )
