from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.db import get_db_engine
from app.Transaction.router import router
from sqlmodel import SQLModel

#initializes the database before receiving any requests
@asynccontextmanager
async def lifespan(app: FastAPI):
	SQLModel.metadata.create_all(get_db_engine())
	yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

