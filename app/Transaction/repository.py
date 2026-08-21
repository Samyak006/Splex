from sqlmodel import Session, select
from fastapi import Depends
from app.Transaction.model import Transaction, TransactionRead, TransactionCreate, TransactionUpdate

class TransactionRepository:
    def __init__(self, session: Session):
        self.session = session

    async def read_transactions(self)-> list[TransactionRead]:
        '''
            Endpoint to retrieve all user transactions.
        '''
        transactions = self.session.exec(select(Transaction)).all() 
        return [TransactionRead.model_validate(transaction) for transaction in transactions]

    async def add_transaction(self, user_transaction:TransactionCreate) -> TransactionRead:
        '''
            Endpoint to add a transaction for a specific user.
        '''
        try:
            transaction = Transaction.model_validate(user_transaction)
            self.session.add(transaction)
            self.session.commit()
            self.session.refresh(transaction)
            return TransactionRead.model_validate(transaction)
        except Exception as e:
            print("Error adding transaction:", e)
            raise e

    async def get_transaction_by_user_id(self, user_id: int) -> list[TransactionRead]:
        '''
            Retrieves transactions for a specific user by user ID.
        '''
        try:
            transactions = self.session.exec(select(Transaction).where(Transaction.user_id == user_id)).all()
            return Transaction.model_validate(transactions)
        except Exception as e:
            print("Error retrieving transactions:", e)
            raise e

    async def update_transaction_by_id(self, transaction_id: int, user_transaction: TransactionUpdate) -> bool:
        '''
            Updates a specific transaction by its ID.
        '''
        try:
            transaction = self.session.get(Transaction, transaction_id)
            if not transaction:
                return False
            for key, value in user_transaction.model_dump().items():
                if value is not None:
                    setattr(transaction, key, value)
            self.session.add(transaction)
            self.session.commit()
            self.session.refresh(transaction)
            return True
        except Exception as e:
            print("Error updating transaction:", e)
            raise e