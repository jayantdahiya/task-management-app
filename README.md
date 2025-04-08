# Task Management Application

A RESTful API for task management built with FastAPI and PostgreSQL.

## Tech Stack

- Python 3.8+
- FastAPI
- SQLAlchemy with SQLModel
- PostgreSQL
- JWT Authentication
- Pydantic

## Setup Instructions

### Using Docker (Recommended)

1. Clone the repository
   ```bash
   git clone https://github.com/jayantdahiya/task-management-app.git
   cd task-management-app
   ```

2. Build and run with Docker Compose
   ```bash
   docker-compose up --build
   ```

3. Access the API at http://localhost:8000
   - API documentation is available at http://localhost:8000/docs

### Manual Setup

1. Clone the repository or ensure you are in the project root.

2. Create and activate a virtual environment (if not already done in Step 1)
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database and ensure the `DATABASE_URL` in `db.py` is correctly configured. You might need to manually create the `taskmanagement` database.

5. Run the application
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API at http://localhost:8000
   - API documentation is available at http://localhost:8000/docs

## API Endpoints

### User Authentication
- POST /register/ – Register a new user
- POST /login/ – Authenticate and get a JWT token

### Task Management
- POST /tasks/ – Create a new task
- GET /tasks/ – List all tasks with optional filters
- GET /tasks/{task_id} – Get details of a specific task
- PUT /tasks/{task_id} – Update a task
- DELETE /tasks/{task_id} – Soft delete a task 
