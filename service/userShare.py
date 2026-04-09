from sqlmodel import Session, select
from fastapi import Depends
from Splex.database.sessions import get_session
from Splex.model.userShare import UserShare, UserShareCreate, UserShareUpdate, UserShareRead

async def get_all_user_shares(session: Session = Depends(get_session)) -> list[UserShareRead]:
    '''
        Retrieves all user shared resources.
    '''
    user_shares = session.exec(select(UserShare)).all()
    return user_shares

async def add_user_share(user_share_data: UserShareCreate, session: Session = Depends(get_session)) -> UserShareRead:
    '''
        Adds a new user shared resource.
    '''
    try:
        user_share = UserShare(**user_share_data.dict())
        session.add(user_share)
        session.commit()
        session.refresh(user_share)
        return UserShareRead(**user_share.dict())
    except Exception as e:
        print("Error adding user share:", e)
        raise e

async def get_user_share_by_id(user_share_id: int, session: Session = Depends(get_session)) -> UserShareRead | None:
    '''
        Retrieves a specific user shared resource by ID.
    '''
    user_share = session.get(UserShare, user_share_id)
    return user_share

async def delete_user_share_by_id(user_share_id: int, session: Session = Depends(get_session)) -> bool:
    '''
        Deletes a specific user shared resource by ID.
    '''
    try:
        user_share = session.get(UserShare, user_share_id)
        if not user_share:
            return False
        session.delete(user_share)
        session.commit()
        return True
    except Exception as e:
        print("Error deleting user share:", e)
        raise e

async def update_user_share_by_id(user_share_id: int, user_share_data: UserShareUpdate, session: Session = Depends(get_session)) -> bool:
    '''
        Updates a specific user shared resource by ID.
    '''
    try:
        user_share = session.get(UserShare, user_share_id)
        if not user_share:
            return False
        for key, value in user_share_data.dict().items():
            if value is not None:
                setattr(user_share, key, value)
        session.add(user_share)
        session.commit()
        return True
    except Exception as e:
        print("Error updating user share:", e)
        raise e