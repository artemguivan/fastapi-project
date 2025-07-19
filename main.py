from fastapi import FastAPI, Depends
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from database import delete_tables, create_tables
from schemas import SchemaTaskAdd
from router import router as task_router


# context
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await delete_tables()  
    print("Tables deleted.")
    yield  
 
    print("Shutting down...")
    await create_tables()  
    print("Tables created.")
    print("Database operations completed during shutdown.")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
 

tasks = []


# @app.get("/home")
# def get_home():
#     task = Task(name="home data")
#     return {"data": task}


