from pydantic import BaseModel as PydanticBaseModel
from typing import TypeVar, Optional
from datetime import datetime

T = TypeVar('T')

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Note(BaseModel):
    id: str | None =None
    title: str
    content: str
    createdAt: datetime| None = None
    updatedAt: datetime | None = None

    class config:
        schema_extra = {
            "example":{
                "title": "Example Title",
                "content": "Example Content"
            }
        }
        exclude = ["id", "createdAt", "updatedAt"]

class Response(BaseModel):
    code: int
    status: str
    message: str
    result: Optional[T] = None