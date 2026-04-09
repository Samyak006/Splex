from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional
from Splex.database.sessions import get_session
from Splex.model.results import Result
from Splex.service.share import get_all_shares, add_share_service, get_share_by_id, delete_share_by_id, update_share_by_id
from Splex.model.shares import Share, ShareCreate, ShareUpdate, ShareRead
from http import HTTPStatus 


router = APIRouter(
    prefix="/shares",
    tags=["shares"],
)

@router.get("/")
async def read_shares(session: Session = Depends(get_session)):
    '''
        Endpoint to retrieve all shared resources.
    '''
    # Placeholder logic for retrieving shares
    shares = await get_all_shares(session)
    if shares is None:
        return Result(http_status=HTTPStatus.NOT_FOUND, message="No shares found.", is_success=False)
    return Result(http_status=HTTPStatus.OK, message="Shares retrieved successfully.", is_success=True, data=shares)

@router.post("/add")
async def add_share(share_data: ShareCreate, session: Session = Depends(get_session)):
    '''
        Endpoint to add a new shared resource.
    '''
    # Placeholder logic for adding a share
    ret_share = await add_share_service(share_data, session)
    if not ret_share:
        return Result(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, message="Failed to add share.", is_success=False)
    return Result(http_status=HTTPStatus.CREATED, message="Share added successfully.", is_success=True, data=ret_share)

@router.get("/{share_id}")
async def get_share(share_id: int, session: Session = Depends(get_session)):
    '''
        Endpoint to retrieve a specific shared resource by ID.
    '''
    # Placeholder logic for retrieving a share
    share = await get_share_by_id(share_id, session)
    if share is None:
        return Result(http_status=HTTPStatus.NOT_FOUND, message="Share not found.", is_success=False)
    return Result(http_status=HTTPStatus.OK, message="Share retrieved successfully.", is_success=True, data=share)

@router.delete("/{share_id}")
async def delete_share(share_id: int, session: Session = Depends(get_session)):
    '''
        Endpoint to delete a specific shared resource by ID.
    '''
    # Placeholder logic for deleting a share
    if not await delete_share_by_id(share_id, session):
        return Result(http_status=HTTPStatus.NOT_FOUND, message="Share not found.", is_success=False)
    return Result(http_status=HTTPStatus.OK, message="Share deleted successfully.", is_success=True)

@router.patch("/{share_id}")
async def update_share(share_id: int, share_data: dict, session: Session = Depends(get_session)):
    '''
        Endpoint to update a specific shared resource by ID.
    '''
    # Placeholder logic for updating a share
    if not await update_share_by_id(share_id, ShareUpdate(**share_data), session):
        return Result(http_status=HTTPStatus.NOT_FOUND, message="Share not found.", is_success=False)
    return Result(http_status=HTTPStatus.NO_CONTENT, message="Share updated successfully.", is_success=True)