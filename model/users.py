from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    email: EmailStr 
    secret_hashed_password: str

    transactions: list["UserTransaction"] | None = Relationship(back_populates="user")  # Relationship to Transaction model
    shares: list["Share"] | None = Relationship(back_populates="userList")  # Relationship to Share model
    
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    secret_hashed_password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    secret_hashed_password: Optional[str] = None

class UserAuthenticate(BaseModel):
    email: str
    password: str