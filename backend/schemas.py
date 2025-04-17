from pydantic import BaseModel

class TodoItem(BaseModel):
    title: str
    completed: bool

class TodoResponse(TodoItem):
    id: int

    class Config:
        orm_mode = True
