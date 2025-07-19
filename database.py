from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel
from typing import Optional


class UrlDataBase(BaseModel):
    pass


engine = create_async_engine(
    url="sqlite+aiosqlite:///tasks.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class DataBaseModel(DeclarativeBase):
    pass

class TaskOrm(DataBaseModel):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DataBaseModel.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DataBaseModel.metadata.drop_all)
