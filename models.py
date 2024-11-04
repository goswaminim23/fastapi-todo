from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for an SQLite database stored in a file
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Create a new engine instance with SQLite, disabling the thread check for SQLite compatibility in multi-threaded environments
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class to manage database connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# Define the TodoItem model, representing the "todos" table in the database
class TodoItem(Base):
    __tablename__ = "todos"  # Name of the table in the database
    
    # Columns in the "todos" table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for each todo item
    title = Column(String, index=True)  # Title of the todo item, indexed for faster search
    description = Column(String, index=True, nullable=True)  # Optional description of the todo item
    completed = Column(Boolean, default=False)  # Status of the todo item, defaulting to not completed
