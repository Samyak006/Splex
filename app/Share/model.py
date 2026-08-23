
from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class Share(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transaction_id: int = Field(default=None,foreign_key="transaction.id")
    createdBy: int = Field(default=None,foreign_key="users.id")
    description: str
    amount: float | None

    # Relationship to User model
    createdByUser: "User" = Relationship(
    back_populates="shares",
    sa_relationship_kwargs={"foreign_keys": "[Share.createdBy]"}
)
    users: list["User"] = Relationship(back_populates="userShares") #type: ignore
    transaction: "Transaction" = Relationship(back_populates="shares") #type: ignore


class ShareCreate(SQLModel):
    createdBy: int
    description: str
    amount: float|None = 0
    transaction_id: int

class ShareUpdate(SQLModel):
    description: Optional[str] = None
    amount: Optional[float] = None

class ShareRead(BaseModel):
    id: int
    createdBy: int
    description: str
    amount: float
    transaction_id: int
    