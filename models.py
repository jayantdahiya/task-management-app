from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

# User model for authentication and task
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str
    hashed_password: str
    
    # One-to-many
    tasks: list["Task"] = Relationship(back_populates="user")

# Task model
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.now)
    is_deleted: bool = Field(default=False)  # Soft delete
    
    # Foreign key to associate task with user
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="tasks") 