
from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from pymongo.errors import PyMongoError

from app.database import todos_collection
from app.schemas import TodoCreate, TodoUpdate

router = APIRouter(prefix="/api/todos", tags=["To-Do Tasks"])


def serialize_todo(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description"),
        "status": todo["status"],
        "createdAt": todo["createdAt"].isoformat()
    }


def get_todo_or_404(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(
            status_code=404,
            detail="To-Do task not found"
        )

    todo = todos_collection.find_one({"_id": ObjectId(todo_id)})

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="To-Do task not found"
        )

    return todo


# CREATE: Add a new task
@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    try:
        data = todo.model_dump()
        data["createdAt"] = datetime.now(timezone.utc)

        result = todos_collection.insert_one(data)
        created_todo = todos_collection.find_one(
            {"_id": result.inserted_id}
        )

        return serialize_todo(created_todo)

    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database error while creating task"
        )


# READ: Get all tasks
@router.get("")
def get_all_todos():
    try:
        todos = todos_collection.find().sort("createdAt", -1)
        return [serialize_todo(todo) for todo in todos]

    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database error while fetching tasks"
        )


# READ: Get one task
@router.get("/{todo_id}")
def get_single_todo(todo_id: str):
    try:
        return serialize_todo(get_todo_or_404(todo_id))

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database error while fetching task"
        )


# UPDATE: Replace task details
@router.put("/{todo_id}")
def update_todo(todo_id: str, todo: TodoUpdate):
    try:
        existing_todo = get_todo_or_404(todo_id)

        todos_collection.update_one(
            {"_id": existing_todo["_id"]},
            {"$set": todo.model_dump()}
        )

        updated_todo = todos_collection.find_one(
            {"_id": existing_todo["_id"]}
        )

        return serialize_todo(updated_todo)

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database error while updating task"
        )


# DELETE: Remove a task
@router.delete("/{todo_id}")
def delete_todo(todo_id: str):
    try:
        existing_todo = get_todo_or_404(todo_id)

        todos_collection.delete_one(
            {"_id": existing_todo["_id"]}
        )

        return {"message": "To-Do task deleted successfully"}

    except HTTPException:
        raise
    except PyMongoError:
        raise HTTPException(
            status_code=500,
            detail="Database error while deleting task"
        )
