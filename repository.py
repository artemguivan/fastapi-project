# work with db like a collection
from main import SchemaTaskAdd
from database import new_session, TaskOrm
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: SchemaTaskAdd) -> int:
        async with new_session() as session:
            task_dict: dict = data.model_dump()

            # orm creates new task
            # we dont put id, db yourself do it
            task = TaskOrm(**task_dict)
            # session work with transaction
            session.add(task)
            await session.flush() # send changet to db and get key of task but dont finish the process
            await session.commit() # all changes send to db
            return task.id
        

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models

