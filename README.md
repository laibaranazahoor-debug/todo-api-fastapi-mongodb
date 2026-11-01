# To-Do List API

A RESTful CRUD To-Do List API built using **Python, FastAPI, and MongoDB Atlas**.

This project was developed as a Backend Development Internship Assignment for Skill Spectrum.

## Features

- Create a new To-Do task
- Retrieve all To-Do tasks
- Retrieve a single task by ID
- Update an existing task
- Delete a task
- MongoDB Atlas cloud database integration
- Input validation using Pydantic
- Proper HTTP status codes and error handling
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Pydantic
- Uvicorn
- Python-dotenv

## Project Structure

```text
todo_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       └── todos.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd todo-api-fastapi-mongodb
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory.

Add your MongoDB Atlas connection details:

```env
MONGODB_URL=your_mongodb_atlas_connection_string
DATABASE_NAME=todo_database
PORT=8000
```

Replace the placeholder with your actual MongoDB Atlas connection string. Never upload your `.env` file or database credentials to GitHub.

### 5. Run the application

```bash
python -m uvicorn app.main:app --reload --port 8000
```

The API will run at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/todos` | Create a To-Do task |
| GET | `/api/todos` | Retrieve all tasks |
| GET | `/api/todos/{todo_id}` | Retrieve a task by ID |
| PUT | `/api/todos/{todo_id}` | Update a task |
| DELETE | `/api/todos/{todo_id}` | Delete a task |

## To-Do Schema

Each task contains:

- `title`: Required string
- `description`: Optional string
- `status`: `pending` or `completed`
- `createdAt`: Automatically generated creation timestamp

## HTTP Status Codes

- `200 OK`: Successful read, update, or delete
- `201 Created`: Task created successfully
- `404 Not Found`: Task does not exist
- `422 Unprocessable Entity`: Invalid request data
- `500 Internal Server Error`: Database or server error

## API Documentation

FastAPI provides interactive Swagger documentation.

Open:

`http://127.0.0.1:8000/docs`

## Database

This project uses **MongoDB Atlas Free Cluster** as its cloud database.

Database name: `todo_database`

Collection name: `todos`

## Testing

All five CRUD endpoints were tested using FastAPI Swagger UI. Successful responses were received, and saved documents were verified in MongoDB Atlas Data Explorer.

## Author

**Laiba Zahoor**

Backend Development Internship Project

Skill Spectrum