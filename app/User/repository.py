from app.User.model import UserCreate, UserRead, User
from sqlmodel import Session, select
from fastapi import Depends
from app.database.sessions import get_session
from app.Utils.hash_bcrypt import hash_pass, verify_pass

class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    
    async def get_user_by_email(self, email:str)->User:
        """
        Finds a user by email

        Args:
            email (str): The email string to be found
        
        Returns:
            returns user Object
        """
        result = self.session.exec(select(User).where(User.email == email)).first() 
        return UserRead(**result.model_dump())

    async def create_user(self, user: UserCreate) -> bool:
        """
        Creates a new user in the database.

        Args:
            user (User): The user object to be created.

        Returns:
            User: The created user object with an assigned ID.
        """
        try:
            print("user_db before hashing:", user)
            user_db = User(**user.model_dump())
            user_db.secret_hashed_password = hash_pass(user.password)
            print("user_db after hashing:", user_db)
            self.session.add(user_db)
            self.session.commit()
            self.session.refresh(user_db)
            return True
        except Exception as e:
            print("Error creating user:", e)
            raise e