from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional
from Splex.model.users import User, UserCreate , UserAuthenticate
from Splex.database.sessions import get_session
from Splex.service.users import create_user, authenticate_user, get_user, get_user_by_email
from http import HTTPStatus 

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@router.post("/")
async def create(user: UserCreate, session: Session = Depends(get_session)):
    return HTTPStatus.CREATED if await create_user(user,session) else HTTPStatus.BAD_REQUEST

@router.post("/authenticate")
async def authenticate(userAuth: UserAuthenticate, session: Session = Depends(get_session)):
    if await authenticate_user(userAuth.email, userAuth.password, session):
        return await get_user_by_email(userAuth.email, session)    
    else:
        return HTTPStatus.UNAUTHORIZED

@router.get("/")
async def read_user(email: EmailStr|None = None, session: Session = Depends(get_session)):
    if email is None:
        return await get_user(session)
    elif email:
        return await get_user_by_email(email,session)

@router.get("/")
async def read_users(session: Session = Depends(get_session)):
    return await get_user(session)