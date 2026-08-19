from sqlmodel import create_engine, SQLModel
from app.config import settings

def get_db_engine(db_url:str = settings.sqldb_url):
    """
    Creates and returns a database engine object.

    Returns:
        Engine: A database engine object.
    """
    engine = create_engine(db_url, echo=True)
    return engine

# Create all tables in the database
SQLModel.metadata.create_all(get_db_engine())