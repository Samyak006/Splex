from sqlmodel import Session
from app.Share.repository import ShareRepository
from app.Share.model import ShareRead, ShareCreate, ShareUpdate

class ShareService:
    def __init__(self, session: Session):
        self._repository = ShareRepository(session)

    async def get_all_shares(self) -> list[ShareRead]:
        '''
            Retrieves all transactions.
        '''
        return await self._repository.get_all_shares()

    async def add_share(self, share: ShareCreate) -> ShareRead:
        '''
            Adds a new transaction.
        '''
        return await self._repository.add_share(share)

    async def get_share_by_user_id(self, user_id: int) -> list[ShareRead]:
        '''
            Retrieves transactions for a specific user.
        '''
        return await self._repository.get_share_by_id(user_id)

    async def update_share_by_id(self, share_id: int, share: ShareUpdate) -> bool:
        '''
            Updates a transaction by ID.
        '''
        return await self._repository.update_share_by_id(share_id, share)
