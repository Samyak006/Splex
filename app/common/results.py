from sqlmodel import SQLModel, Field
from typing import Optional, Any as Object

class Result(SQLModel):
    http_status: str = Field(index=True)
    data: Optional[Object]| None = None
    message: Optional[str] = None
    is_success: bool = True
