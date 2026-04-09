from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional
from Splex.model.userTransactions import UserTransaction, UserTransactionCreate, UserTransactionUpdate
from Splex.database.sessions import get_session
from Splex.service.userTransactions import readTransactions, addTransaction , getTransactionByUserId, updateTransactionById
from Splex.model.results import Result
from http import HTTPStatus 


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)
@router.get("/")
async def read_transactions(session: Session = Depends(get_session)):
    '''
        Endpoint to retrieve all user transactions.
    '''
    transactions = await readTransactions(session)
    return Result(http_status=HTTPStatus.OK, message="Transactions retrieved successfully.", is_success=True, data=transactions)

@router.post("/{user_id}/add")
async def add_transaction(userTransaction:UserTransactionCreate, session: Session = Depends(get_session)):
    '''
        Endpoint to add a transaction for a specific user.
    '''
    #TODO: Implement validation logic for userTransaction data
    if await addTransaction(userTransaction, session):
        return Result(http_status=HTTPStatus.CREATED, message="Transaction added successfully.", is_success=True)
    else:
        return Result(http_status=HTTPStatus.INTERNAL_SERVER_ERROR, message="Failed to add transaction.", is_success=False)

@router.get("/{user_id}/history")
async def transaction_history(user_id: int, session: Session = Depends(get_session)):
    '''
        Endpoint to retrieve transaction history for a specific user.
    '''
    # Placeholder logic for retrieving transaction history
    ret = await getTransactionByUserId(user_id, session)
    if ret:
        return Result(http_status=HTTPStatus.OK, message="Transaction history retrieved successfully.", is_success=True, data=ret)
    else:
        return Result(http_status=HTTPStatus.NOT_FOUND, message="No transactions found for the user.", is_success=False)

@router.delete("/{transaction_id}")
async def delete_transaction(user_id: int, transaction_id: int, session: Session = Depends(get_session)):
    '''
        Endpoint to delete a specific transaction for a user.
    '''
    # Placeholder logic for deleting a transaction
    return {"message": f"Transaction {transaction_id} deleted for user {user_id}."}

@router.patch("/{transaction_id}")
async def update_transaction(transaction_id: int, userTransaction: UserTransactionUpdate, session: Session = Depends(get_session)):
    '''
        Endpoint to update a specific transaction for a user.
    '''
    # Placeholder logic for updating a transaction
    if await updateTransactionById(transaction_id, userTransaction, session):
        return Result(http_status=HTTPStatus.NO_CONTENT, message="Transaction updated successfully.", is_success=True)
    else:
        return Result(http_status=HTTPStatus.NOT_FOUND, message="Transaction not found.", is_success=False)