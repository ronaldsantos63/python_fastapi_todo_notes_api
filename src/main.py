from typing import List, Union
import uuid
from fastapi import Depends, FastAPI

from model.todo import Todo, TodoStatus


app = FastAPI()

async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/todos", response_model=List[Todo], response_model_exclude_unset=True)
async def all_todos(commons: dict = Depends(common_parameters)):
    return [
        Todo(id=uuid.uuid1().hex, title="Estudar Python", status=TodoStatus.in_progress),
        Todo(id=uuid.uuid1().hex, title="Estudar Java", description="Estudar desde os princípios"),
        Todo(id=uuid.uuid1().hex, title="Estudar Flutter", description="Começar pelo dart e depois atacar o flutter", status=TodoStatus.done)
    ]

@app.post("/todos", response_model=Todo)
async def add_todo(todo: Todo):
    return todo