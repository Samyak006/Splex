from sqlmodel import SQLModel, Field

class TransactionShareLink(SQLModel, table=True):
    transaction_id: int = Field(default=None, primary_key=True, foreign_key="transaction.id")
    share_id: int = Field(default=None, primary_key=True, foreign_key="share.id")