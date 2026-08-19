from fastapi import FastAPI, Depends
from app.Transaction.router import transactions
from app.Plaid.transactions import  get_transactions
from app.config import settings
from app.database.db import get_db_engine
from contextlib import asynccontextmanager
from app.User.router import router as user_router
from app.Share.router import router as share_router
from app.UserShare.router import router as user_share_router
from app.Transaction.router import router as transaction_router

#initializes the database before receiving any requests
@asynccontextmanager
async def lifespan(app: FastAPI):
	get_db_engine()
	yield

app = FastAPI()
app.include_router(user_router)
app.include_router(share_router)
app.include_router(user_share_router)
app.include_router(transaction_router)



@app.get("/")
async def root():
	return {"message":"Hello World"}

@app.get("/test")
def test():
	return get_transactions()

