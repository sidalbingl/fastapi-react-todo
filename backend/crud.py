from sqlalchemy.orm import Session
from . import models, schemas


def get_active_todos(db: Session):
    return db.query(models.Todo).filter(models.Todo.completed == False).all()


def get_completed_todos(db: Session):
    return db.query(models.Todo).filter(models.Todo.completed == True).all()


def create_todo(db: Session, todo: schemas.TodoItem):
    db_todo = models.Todo(title=todo.title, completed=False)  # Yeni görev 'completed: false' olarak ekleniyor
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, updated_data: schemas.TodoItem):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not db_todo:
        return None
    db_todo.title = updated_data.title or db_todo.title
    db_todo.completed = updated_data.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()




