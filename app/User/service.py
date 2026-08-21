from app.User.model import UserCreate, UserRead, User
from sqlmodel import Session, select
from fastapi import Depends
from app.database.sessions import get_session
from app.Utils.hash_bcrypt import hash_pass, verify_pass
from app.User.repository import UserRepository
from app.User.model import UserAuthenticate

class UserService:
    def __init__(self, session: Session):
        self.UserRepository = UserRepository(session)
        self.session = session

    async def create_user(self, user: UserCreate) -> bool:
        """
        Creates a new user in the database.

        Args:
            user (User): The user object to be created.

        Returns:
            User: The created user object with an assigned ID.
        """
        if await self.UserRepository.get_user_by_email(user.email) is None:
            await self.UserRepository.create_user(user)
            return True   
        return False
    
    async def authenticate_user(self, userAuth: UserAuthenticate) -> UserRead | None:
        """
        Authenticates a user by verifying their username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User | None: The authenticated user object if credentials are valid, otherwise None.
        """
        user = await self.UserRepository.get_user_by_email(userAuth.email)
        if user and verify_pass(userAuth.password, user.secret_hashed_password):
            return user
        return None

    async def get_user_by_email(self, email: str = "") -> UserRead | None:
        """
        Retrieves a user by their email.

        Args:
            session (Session): The database session.
            email (str): The email of the user to retrieve.

        Returns:
            User | None: The user object if found, otherwise None.
        """
        return await self.UserRepository.get_user_by_email(email)
