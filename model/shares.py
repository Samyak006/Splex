
from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from Splex.model.userTransactions import UserTransaction


class Share(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transaction_id: int = Field(foreign_key="usertransaction.id", sa_column_kwargs={"name":"transaction_id"})
    createdBy: int = Field(foreign_key="user.id", sa_column_kwargs={"name":"user_id"})
    description: str
    userList: list["User"] | None = Relationship(back_populates="shares")  # Relationship to User model

class ShareCreate(SQLModel):
    createdBy: int
    description: str

class ShareUpdate(SQLModel):
    description: Optional[str] = None

class ShareRead(BaseModel):
    id: int
    createdBy: int
    description: str
    