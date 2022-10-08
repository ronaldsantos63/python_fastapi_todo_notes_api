from enum import Enum
from typing import Annotated, Union
from uuid import uuid4
from pydantic import BaseModel, Field, validator

class TodoStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done",


class Todo(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    title: Annotated[str, Field(max_length=80)]
    description: Union[str, None] = None,
    status: TodoStatus = Field(TodoStatus.todo, alias="status")

    @validator('title')
    def check_title_not_empty(cls, v):
        assert v != '', 'Empty title are not allowed'
        return v
