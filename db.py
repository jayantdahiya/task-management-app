from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database connection settings
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/taskmanagement")

# Create database engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database session dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 