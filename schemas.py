from typing import Optional
from pydantic import BaseModel

class SchemaTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class SchemaTaskGet(SchemaTaskAdd):
    id: int 

