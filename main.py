from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session
from Splex.routing import transactions
from Splex.service.plaid.transactions import  get_transactions
from Splex.config import settings
app = FastAPI()

if not settings.is_only_integration:
	from Splex.database.sessions import get_session
	from Splex.routing import users, userTransactions, share, userShare
	print("Running in integration mode, skipping router inclusion.")
	app.include_router(users.router)
	app.include_router(userTransactions.router)
	app.include_router(share.router)
	app.include_router(userShare.router)
app.include_router(transactions.router)

@app.get("/")
async def root():
	return {"message":"Hello World"}

@app.get("/test")
def test():
	return get_transactions()

