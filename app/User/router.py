from fastapi import APIRouter, Depends, Response, Request, HTTPException
from sqlmodel import Session
from pydantic import EmailStr
from app.User.model import UserCreate , UserAuthenticate
from app.database.sessions import get_session
from app.User.service import UserService
from http import HTTPStatus 
from app.Utils.jwt import create_access_token, decode_access_token

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)

@router.post("/")
async def create(user: UserCreate, 
                 user_service: UserService = Depends(get_user_service)):
    return HTTPStatus.CREATED if await user_service.create_user(user) else HTTPStatus.BAD_REQUEST

@router.post("/authenticate")
async def authenticate(
        userAuth: UserAuthenticate,
        response: Response,
        user_service: UserService = Depends(get_user_service)
    ):
    user_data = await user_service.authenticate_user(userAuth) 
    if user_data is None:
        raise HTTPException(
            status_code = HTTPStatus.UNAUTHORIZED,
            detail = "Invalid Credentials"
        )
    token, exp = create_access_token(data = {"sub":userAuth.email})
    response.set_cookie(
        key='token',
        value=token,
        expires=exp,
        httponly=True
    )
    return HTTPStatus.OK

@router.get("/")
async def read_user(
        request: Request,
        email: EmailStr|None = None, 
        user_service: UserService = Depends(get_user_service)
        ):
    token = request.cookies.get("token",None)
    if token:
        email = decode_access_token(token=token).get('sub')
        if email:
            return await user_service.get_user_by_email(email)
        return HTTPStatus.FORBIDDEN
    return HTTPStatus.BAD_REQUEST
