from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, crud, schemas
from models import SessionLocal, engine
from fastapi.responses import JSONResponse

# Create the database tables if they do not exist
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Provide the session to the route handlers
    finally:
        db.close()  # Close the session after the request is completed

# Endpoint to retrieve all Todo items
@app.get("/todos", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)  # Call the CRUD function to get all todos

# Endpoint to create a new Todo item
@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)  # Call the CRUD function to create a new todo

# Endpoint to retrieve a single Todo item by ID
@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id)  # Call the CRUD function to get a specific todo
    if db_todo is None:
        # Raise an HTTP 404 error if the todo is not found
        raise HTTPException(status_code=404, detail="To-Do not found")
    return db_todo

# Endpoint to update an existing Todo item by ID
@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)  # Call the CRUD function to update a specific todo
    if db_todo is None:
        # Raise an HTTP 404 error if the todo is not found
        raise HTTPException(status_code=404, detail="To-Do not found")
    return db_todo

# Endpoint to delete a Todo item by ID
@app.delete("/todos/{todo_id}", response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo_by_id(db, todo_id)  # Call the CRUD function to delete a specific todo
    if db_todo is None:
        # Raise an HTTP 404 error if the todo is not found
        raise HTTPException(status_code=404, detail="To-Do not found")
    # Return a 204 No Content response after successful deletion
    return JSONResponse(status_code=204, content="To-Do item deleted")
