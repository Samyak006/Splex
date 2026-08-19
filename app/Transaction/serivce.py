from sqlmodel import Session, select
from fastapi import Depends
from Splex.database.sessions import get_session
from Splex.model.userTransactions import UserTransaction, UserTransactionCreate, UserTransactionUpdate

async def readTransactions(session: Session = Depends(get_session))-> list[UserTransaction]:
    '''
        Endpoint to retrieve all user transactions.
    '''
    transactions = session.exec(select(UserTransaction)).all() 
    return transactions

async def addTransaction(user_transaction:UserTransactionCreate, session: Session = Depends(get_session)) -> UserTransaction:
    '''
        Endpoint to add a transaction for a specific user.
    '''
    try:
        transaction = UserTransaction(**user_transaction.dict())
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return True
    except Exception as e:
        print("Error adding transaction:", e)
        raise e

async def getTransactionByUserId(user_id: int, session: Session = Depends(get_session)) -> list[UserTransaction]:
    '''
        Retrieves transactions for a specific user by user ID.
    '''
    try:
        transactions = session.exec(select(UserTransaction).where(UserTransaction.user_id == user_id)).all()
        return transactions
    except Exception as e:
        print("Error retrieving transactions:", e)
        raise e

async def updateTransactionById(transaction_id: int, user_transaction: UserTransactionUpdate, session: Session = Depends(get_session)) -> bool:
    '''
        Updates a specific transaction by its ID.
    '''
    try:
        transaction = session.get(UserTransaction, transaction_id)
        if not transaction:
            return False
        for key, value in user_transaction.dict().items():
            if value is not None:
                setattr(transaction, key, value)
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        return True
    except Exception as e:
        print("Error updating transaction:", e)
        raise e