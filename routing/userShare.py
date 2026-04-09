from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional
from Splex.model.userShare import UserShare, UserShareCreate, UserShareUpdate, UserShareRead, UserShareKey
from Splex.database.sessions import get_session
from Splex.service.userShare import get_all_user_shares, add_user_share, get_user_share_by_id, delete_user_share_by_id, update_user_share_by_id
from Splex.model.results import Result
from http import HTTPStatus 

router = APIRouter(
    prefix="/user-shares",
    tags=["user-shares"],
)

@router.get("/")
async def read_user_shares(session: Session = Depends(get_session)):
    '''
        Endpoint to retrieve all user shared resources.
    '''
    user_shares = await get_all_user_shares(session)
    if user_shares is None:
        return Result(http_status=HTTPStatus.NOT_FOUND, message="No user shares found.", is_success=False)
    return Result(http_status=HTTPStatus.OK, message="User shares retrieved successfully.", is_success=True, data=user_shares)

@router.post("/add")
async def add_user_share_endpoint(user_share_data: UserShareCreate, session: Session = Depends(get_session)):
    '''
        Endpoint to add a new user shared resource.
    '''
    ret_user_share = await add_user_share(user_share_data, session)
    if not ret_user_share:
        return Result(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, message="Failed to add user share.", is_success=False)
    return Result(http_status=HTTPStatus.CREATED, message="User share added successfully.", is_success=True, data=ret_user_share)

# @router.get("/{user_share_id}")
# async def get_user_share(user_share_id: UserShareKey, session: Session = Depends(get_session)):
#     '''
#         Endpoint to retrieve a specific user shared resource by ID.
#     '''
#     user_share = await get_user_share_by_id(UserShareKey, session)
#     if user_share is None:
#         return Result(http_status=HTTPStatus.NOT_FOUND, message="User share not found.", is_success=False)
#     return Result(http_status=HTTPStatus.OK, message="User share retrieved successfully.", is_success=True, data=user_share)