from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base
from . import crud, schemas
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Veritabanı tablosunu oluşturma
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React uygulamasının çalıştığı adres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veritabanı bağlantısını sağlayan fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# To-Do ekleme (Veritabanına kaydetme)
@app.post("/todos/", response_model=schemas.TodoResponse)
async def create_todo(todo: schemas.TodoItem, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

# Tüm To-Do'ları listeleme
@app.get("/todos/", response_model=list[schemas.TodoResponse])
async def get_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db=db)

# Sadece aktif (completed: False) görevleri listeleme
@app.get("/todos/active", response_model=list[schemas.TodoResponse])
async def get_active_todos(db: Session = Depends(get_db)):
    return crud.get_active_todos(db=db)

# Sadece tamamlanmış (completed: True) görevleri listeleme
@app.get("/todos/completed", response_model=list[schemas.TodoResponse])
async def get_completed_todos(db: Session = Depends(get_db)):
    return crud.get_completed_todos(db=db)

# To-Do güncelleme (örneğin: tamamlandı olarak işaretleme)
@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
async def update_todo(todo_id: int, updated_todo: schemas.TodoItem, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db_todo.title = updated_todo.title
    db_todo.completed = updated_todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo
