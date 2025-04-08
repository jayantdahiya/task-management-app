from fastapi import FastAPI
from sqlmodel import SQLModel
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from db import engine
from routes import auth, tasks
from errors import validation_exception_handler, http_exception_handler

app = FastAPI(title="Task Management API")

# Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Include routers
app.include_router(auth.router, prefix="", tags=["Authentication"])
app.include_router(tasks.router, prefix="", tags=["Tasks"])

# Add error handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler) 