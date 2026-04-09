from Splex.model.users import UserCreate, UserRead, User
from sqlmodel import Session, select
from fastapi import Depends
from typing import Annotated
from Splex.database.sessions import get_session
from Splex.utils.hash_bcrypt import hash_pass, verify_pass

async def create_user(user: UserCreate, session: Session = Depends(get_session)) -> bool:
    """
    Creates a new user in the database.

    Args:
        user (User): The user object to be created.

    Returns:
        User: The created user object with an assigned ID.
    """
    try:
        print("user_db before hashing:", user)
        user_db = User(**user.dict())
        user_db.secret_hashed_password = hash_pass(user.password)
        print("user_db after hashing:", user_db)
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        return True
    except Exception as e:
        print("Error creating user:", e)
        raise e
    
async def authenticate_user(email: str, password: str, session: Session = Depends(get_session)) -> UserRead | None:
    """
    Authenticates a user by verifying their username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        User | None: The authenticated user object if credentials are valid, otherwise None.
    """
    user = session.exec(select(User).where(User.email == email)).first()
    if user and verify_pass(password, user.secret_hashed_password):
        return True
    return False

async def get_user(session: Session=  Depends(get_session)) -> UserRead | None:
    """
    Retrieves a user by their ID.

    Args:
        session (Session): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        User | None: The user object if found, otherwise None.
    """
    print("Getting all users")
    user = session.exec(select(User))
    if not user:
        return None
    return [UserRead(**u.dict()) for u in user]
    

async def get_user_by_email(email: str = "",session:Session = Depends(get_session)) -> UserRead | None:
    """
    Retrieves a user by their email.

    Args:
        session (Session): The database session.
        email (str): The email of the user to retrieve.

    Returns:
        User | None: The user object if found, otherwise None.
    """
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        return None
    user_ret = UserRead(**user.dict())
    return user_ret
