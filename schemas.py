from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

# Schema for creating new users
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Schema for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Schema for user responses (excludes sensitive data)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

# Schema for creating new tasks
class TaskCreate(BaseModel):
    title: str
    description: str

# Schema for updating existing tasks
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Schema for task responses
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    timestamp: datetime
    user_id: int 