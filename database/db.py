from sqlmodel import create_engine, SQLModel
from Splex.config import settings
from Splex.model import User, UserTransaction

def get_db_engine():
    """
    Creates and returns a database engine object.

    Returns:
        Engine: A database engine object.
    """
    engine = create_engine(settings.sqldb_url, echo=True)
    return engine

# Create all tables in the database
SQLModel.metadata.create_all(get_db_engine())