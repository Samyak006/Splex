from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from http import HTTPStatus
from app.Transaction.model import TransactionCreate, TransactionUpdate, TransactionRead
from app.Transaction.serivce import TransactionService
from app.database.sessions import get_session

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

def get_transaction_service(session: Session = Depends(get_session)):
    return TransactionService(session)

@router.post("/", status_code=HTTPStatus.CREATED)
async def create(transaction: TransactionCreate,
                  transaction_service: TransactionService = Depends(get_transaction_service)):
    result = await transaction_service.add_transaction(transaction)
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Failed to create transaction")
    return result

@router.get("/", status_code=HTTPStatus.OK)
async def read_transactions(transaction_service: TransactionService = Depends(get_transaction_service)):
    return await transaction_service.read_transactions()

@router.get("/user/{user_id}", status_code=HTTPStatus.OK)
async def read_transactions_by_user(user_id: int,
                                     transaction_service: TransactionService = Depends(get_transaction_service)):
    return await transaction_service.get_transactions_by_user_id(user_id)

@router.put("/{transaction_id}", status_code=HTTPStatus.OK)
async def update(transaction_id: int, transaction: TransactionUpdate,
                  transaction_service: TransactionService = Depends(get_transaction_service)):
    result = await transaction_service.update_transaction(transaction_id, transaction)
    if not result:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Failed to update transaction")
    return HTTPStatus.OK