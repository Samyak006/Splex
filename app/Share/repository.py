from sqlmodel import Session, select
from app.Share.model import Share, ShareCreate, ShareUpdate, ShareRead

class ShareRepository:
    def __init__(self, session: Session):
        self.session = session

    async def get_all_shares(self) -> list[ShareRead]:
        '''
            Retrieves all shared resources.
        '''
        shares = self.session.exec(select(Share)).all()
        return [ShareRead.model_validate(share) for share in shares]

    async def add_share(self, share_data: ShareCreate) -> ShareRead:
        '''
            Adds a new shared resource.
        '''
        try:
            share = Share.model_validate(share_data)
            self.session.add(share)
            self.session.commit()
            self.session.refresh(share)
            return ShareRead.model_validate(share)
        except Exception as e:
            print("Error adding share:", e)
            raise e

    async def get_share_by_id(self, share_id: int) -> ShareRead | None:
        '''
            Retrieves a specific shared resource by ID.
        '''
        share = self.session.get(Share, share_id)
        return share

    async def delete_share_by_id(self, share_id: int) -> bool:
        '''
            Deletes a specific shared resource by ID.
        '''
        try:
            share = self.session.get(Share, share_id)
            if not share:
                return False
            self.session.delete(share)
            self.session.commit()
            return True
        except Exception as e:
            print("Error deleting share:", e)
            raise e

    async def update_share_by_id(self, share_id: int, share_data: ShareUpdate) -> bool:
        '''
            Updates a specific shared resource by ID.
        '''
        try:
            share = self.session.get(Share, share_id)
            if not share:
                return False
            for key, value in share_data.model_dump(exclude_unset=None).items():
                setattr(share, key, value)
            self.session.add(share)
            self.session.commit()
            self.session.refresh(share)
            return True
        except Exception as e:
            print("Error updating share:", e)
            raise e