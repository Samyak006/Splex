
from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from TransactionShareLink.model import TransactionShareLink

class Share(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transaction_id: int = Field(foreign_key="transaction.id")
    createdBy: int = Field(foreign_key="user.id")
    description: str
    amount: float|None

    # Relationship to User model
    users: list["User"] | None = Relationship(back_populates="shares") #type: ignore
    transactions: list["Transactions"] = Relationship(back_populates="shares",link_model=TransactionShareLink) #type: ignore

class ShareCreate(SQLModel):
    createdBy: int
    description: str
    amount: float|None = 0

class ShareUpdate(SQLModel):
    description: Optional[str] = None
    amount: Optional[float] = None

class ShareRead(BaseModel):
    id: int
    createdBy: int
    description: str
    amount: float
    