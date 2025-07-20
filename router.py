 
from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import SchemaTaskAdd


router = APIRouter(
    prefix="/tasks"
)

@router.post("")
async def add_task(
    task:  Annotated[SchemaTaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "tasak_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}


