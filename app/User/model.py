from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    email: EmailStr 
    secret_hashed_password: str
    
    #Relationship
    userShares: list["Share"] = Relationship(back_populates="users") #type: ignore
    transactions: list["Transaction"] = Relationship(back_populates="user") #type: ignore
    shares: list["Share"] = Relationship(back_populates="createdByUser", sa_relationship_kwargs={"foreign_keys": "[Share.createdBy]"}) #type: ignore

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