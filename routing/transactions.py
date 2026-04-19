from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from pydantic import EmailStr
from typing import Optional, Annotated
from Splex.service.plaid.transactions import get_transactions
from Splex.service.plaid.access_auth import get_access_token
from http import HTTPStatus 
from Splex.model.results import Result

router = APIRouter(
    prefix="/plaid_transactions",
    tags=["plaid_transactions"],
)

@router.get("/")
async def fetch_transactions(access_token: Annotated[str, Depends(get_access_token)]):
    '''
        Endpoint to fetch transactions from Plaid.
    '''
    try:
        transactions = await get_transactions(access_token)
        return  Result(data=transactions, http_status=HTTPStatus.OK, message="Transactions fetched successfully.", is_success=True)
    except Exception as e:
        return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR