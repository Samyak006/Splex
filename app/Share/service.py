from sqlmodel import Session, select
from fastapi import Depends
from Splex.database.sessions import get_session
from Splex.model.shares import Share, ShareCreate, ShareUpdate, ShareRead

async def get_all_shares(session: Session = Depends(get_session)) -> list[ShareRead]:
    '''
        Retrieves all shared resources.
    '''
    shares = session.exec(select(Share)).all()
    return shares

async def add_share_service(share_data: ShareCreate, session: Session = Depends(get_session)) -> ShareRead:
    '''
        Adds a new shared resource.
    '''
    try:
        share = Share(**share_data.dict())
        session.add(share)
        session.commit()
        session.refresh(share)
        return ShareRead(**share.dict())
    except Exception as e:
        print("Error adding share:", e)
        raise e

async def get_share_by_id(share_id: int, session: Session = Depends(get_session)) -> ShareRead | None:
    '''
        Retrieves a specific shared resource by ID.
    '''
    share = session.get(Share, share_id)
    return share

async def delete_share_by_id(share_id: int, session: Session = Depends(get_session)) -> bool:
    '''
        Deletes a specific shared resource by ID.
    '''
    try:
        share = session.get(Share, share_id)
        if not share:
            return False
        session.delete(share)
        session.commit()
        return True
    except Exception as e:
        print("Error deleting share:", e)
        raise e

async def update_share_by_id(share_id: int, share_data: ShareUpdate, session: Session = Depends(get_session)) -> bool:
    '''
        Updates a specific shared resource by ID.
    '''
    try:
        share = session.get(Share, share_id)
        if not share:
            return False
        for key, value in share_data.dict().items():
            if value is not None:
                setattr(share, key, value)
        session.add(share)
        session.commit()
        session.refresh(share)
        return True
    except Exception as e:
        print("Error updating share:", e)
        raise e