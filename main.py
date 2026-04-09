from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session
from Splex.routing import users, userTransactions, share, userShare
from Splex.database.sessions import get_session
from Splex.testing.test_service import test_get_user_share

app = FastAPI()
app.include_router(users.router)
app.include_router(userTransactions.router)
app.include_router(share.router)
app.include_router(userShare.router)

@app.get("/")
async def root():
	return {"message":"Hello World"}

@app.get("/test")
async def test_db(session: Session = Depends(get_session)):
	return await test_get_user_share(session)

