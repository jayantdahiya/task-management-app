from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str
    hashed_password: str
    
    tasks: list["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    timestamp: datetime = Field(default_factory=datetime.now)
    is_deleted: bool = Field(default=False)  # For soft delete
    
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="tasks") 