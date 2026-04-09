from sqlmodel import Session
from Splex.database.db import get_db_engine
from Splex.config import settings
from typing import Generator

def get_session() -> Generator:  # pragma: no cover
    """
    Returns a generator that yields a database session

    Yields:
        Session: A database session object.

    Raises:
        Exception: If an error occurs while getting the database session.
    """

    engine = get_db_engine()
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close() 