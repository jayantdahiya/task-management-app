from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from typing import List
from datetime import datetime

from db import get_db
from models import User, Task
from schemas import TaskCreate, TaskUpdate, TaskResponse
from auth import get_current_user

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task

@router.get("/tasks/", response_model=List[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    date_filter: datetime = Query(None),
    search: str = Query(None)
):
    statement = select(Task).where(
        Task.user_id == current_user.id,
        Task.is_deleted == False
    )
    
    # Apply date filter if provided
    if date_filter:
        statement = statement.where(Task.timestamp >= date_filter)
    
    # Apply fuzzy search if provided
    if search:
        statement = statement.where(Task.title.contains(search))
    
    results = db.execute(statement).all()
    tasks = [result[0] for result in results]
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    statement = select(Task).where(
        Task.id == task_id,
        Task.user_id == current_user.id,
        Task.is_deleted == False
    )
    result = db.execute(statement).first()
    task = result[0] if result else None
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
        
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    statement = select(Task).where(
        Task.id == task_id,
        Task.user_id == current_user.id,
        Task.is_deleted == False
    )
    result = db.execute(statement).first()
    task = result[0] if result else None
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Update task fields if provided
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    
    # Update timestamp automatically
    task.timestamp = datetime.now()
    
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    statement = select(Task).where(
        Task.id == task_id,
        Task.user_id == current_user.id,
        Task.is_deleted == False
    )
    result = db.execute(statement).first()
    task = result[0] if result else None
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Soft delete
    task.is_deleted = True
    
    db.add(task)
    db.commit()
    
    return None 