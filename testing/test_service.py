from Splex.model.results import Result
from http import HTTPStatus 
from sqlmodel import Session, select
from fastapi import Depends
from Splex.database.sessions import get_session
from Splex.model.shares import Share

async def test_get_user_share(session: Session = Depends(get_session)):
    '''
        Test function to retrieve all shares from the database.
    '''
    share = session.exec(select(Share)).first()
    print(share.userList)
    return 

async def test_share():
    ret = await test_get_user_share()
        