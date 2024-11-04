from pydantic import BaseModel
from typing import Optional

# Base schema for Todo, containing common fields for title, description, and completed status
class TodoBase(BaseModel):
    title: str  # Title of the todo item (required)
    description: Optional[str] = None  # Optional description for the todo item
    completed: bool = False  # Status indicating if the todo is completed, default is False

# Schema for creating a new Todo item, inherits from TodoBase
class TodoCreate(TodoBase):
    pass  # No additional fields needed; same as TodoBase

# Schema for updating an existing Todo item, inherits from TodoBase
class TodoUpdate(TodoBase):
    pass  # No additional fields needed; same as TodoBase

# Schema for response when retrieving a Todo item, includes an ID field
class TodoResponse(TodoBase):
    id: int  # Unique identifier for the todo item

    # Config class to enable compatibility with SQLAlchemy ORM objects
    class Config:
        orm_mode = True  # Allows Pydantic to read SQLAlchemy models directly
