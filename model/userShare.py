from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class UserShare(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    share_id: int = Field(foreign_key="share.id", primary_key=True)
    amount: float

class UserShareCreate(SQLModel):
    user_id: int
    share_id: int
    amount: float

class UserShareUpdate(SQLModel):
    amount: Optional[float] = None

class UserShareRead(SQLModel):
    user_id: int
    share_id: int
    amount: float

class UserShareDelete(SQLModel):
    user_id: int
    share_id: int

class UserShareKey(SQLModel):
    user_id: int
    share_id: int