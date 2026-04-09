from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class UserTransaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int= Field(foreign_key="user.id")
    amount: float
    description: str
    user: User = Relationship(back_populates="transactions")  # Relationship to User model

class UserTransactionCreate(SQLModel):
    user_id: int
    amount: float
    description: str

class UserTransactionUpdate(SQLModel):
    amount: Optional[float] = None
    description: Optional[str] = None