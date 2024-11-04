from sqlalchemy.orm import Session
from models import TodoItem
from schemas import TodoCreate, TodoUpdate

# Retrieve all Todo items from the database
def get_todos(db: Session):
    return db.query(TodoItem).all()

# Create a new Todo item
def create_todo(db: Session, todo: TodoCreate):
    db_todo = TodoItem(**todo.dict())  # Map fields from schema to model
    db.add(db_todo)  # Add the new item to the session
    db.commit()  # Commit the transaction
    db.refresh(db_todo)  # Refresh the instance with the new ID
    return db_todo

# Retrieve a single Todo item by its ID
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(TodoItem).filter(TodoItem.id == todo_id).first()

# Update an existing Todo item by its ID
def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        for key, value in todo.dict().items():  # Update fields with new values
            setattr(db_todo, key, value)
        db.commit()  # Commit changes
        db.refresh(db_todo)  # Refresh the instance with updated data
    return db_todo

# Delete a Todo item by its ID
def delete_todo_by_id(db: Session, todo_id: int):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)  # Delete the item from the session
        db.commit()  # Commit the transaction
    return db_todo
