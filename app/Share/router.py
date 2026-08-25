from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from http import HTTPStatus
from app.database.sessions import get_session
from app.Share.service import ShareService
from app.Share.model import ShareCreate, ShareUpdate, ShareRead

router = APIRouter(
    prefix="/shares",
    tags=["shares"],
)

def get_service(session: Session = Depends(get_session)):
    return ShareService(session)

@router.get("/", status_code=HTTPStatus.OK)
async def read_shares(service: ShareService = Depends(get_service)):
    '''
        Retrieves all shares.
    '''
    shares = await service.get_all_shares()
    if not shares:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="No shares found.")
    return shares

@router.post("/add", status_code=HTTPStatus.CREATED)
async def add_share(share_data: ShareCreate, service: ShareService = Depends(get_service)):
    '''
        Adds a new share.
    '''
    result = await service.add_share(share_data)
    if not result:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Failed to add share.")
    return result

@router.get("/{share_id}", status_code=HTTPStatus.OK)
async def get_share(share_id: int, service: ShareService = Depends(get_service)):
    '''
        Retrieves a specific share by ID.
    '''
    share = await service.get_share_by_id(share_id)
    if share is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Share not found.")
    return share

@router.delete("/{share_id}", status_code=HTTPStatus.OK)
async def delete_share(share_id: int, service: ShareService = Depends(get_service)):
    '''
        Deletes a specific share by ID.
    '''
    result = await service.delete_share_by_id(share_id)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Share not found.")
    return HTTPStatus.OK

@router.patch("/{share_id}", status_code=HTTPStatus.OK)
async def update_share(share_id: int, share_data: ShareUpdate, service: ShareService = Depends(get_service)):
    '''
        Updates a specific share by ID.
    '''
    result = await service.update_share_by_id(share_id, share_data)
    if not result:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Share not found.")
    return HTTPStatus.OK