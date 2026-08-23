from sqlmodel import Session
from app.Transaction.repository import TransactionRepository
from app.Transaction.model import TransactionRead, TransactionCreate, TransactionUpdate

class TransactionService:
    def __init__(self, session: Session):
        self.transaction_repo = TransactionRepository(session)

    async def read_transactions(self) -> list[TransactionRead]:
        '''
            Retrieves all transactions.
        '''
        return await self.transaction_repo.read_transactions()

    async def add_transaction(self, transaction: TransactionCreate) -> TransactionRead:
        '''
            Adds a new transaction.
        '''
        return await self.transaction_repo.add_transaction(transaction)

    async def get_transactions_by_user_id(self, user_id: int) -> list[TransactionRead]:
        '''
            Retrieves transactions for a specific user.
        '''
        return await self.transaction_repo.get_transaction_by_user_id(user_id)

    async def update_transaction(self, transaction_id: int, transaction: TransactionUpdate) -> bool:
        '''
            Updates a transaction by ID.
        '''
        return await self.transaction_repo.update_transaction_by_id(transaction_id, transaction)