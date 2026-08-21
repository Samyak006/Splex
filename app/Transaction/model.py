from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from app.TransactionShareLink.model import TransactionShareLink

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int= Field(foreign_key="user.id")
    amount: float
    description: str

    # Relationship to User model
    user: User = Relationship(back_populates="transactions")  #type: ignore
    shares: list["Share"] = Relationship(back_populates="transactions", link_model=TransactionShareLink) #type: ignore

class TransactionCreate(SQLModel):
    user_id: int
    amount: float
    description: str

class TransactionUpdate(SQLModel):
    amount: Optional[float] = None
    description: Optional[str] = None

class TransactionRead(SQLModel):
    user_id: int
    amount: float
    description: str