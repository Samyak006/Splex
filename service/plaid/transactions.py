import httpx
from Splex.api import api
from typing import Annotated
from fastapi import Depends
from Splex.model.plaid_access_token import AccessTokenResponseBody
from Splex.service.plaid.access_auth import get_access_token
from Splex.config import settings
import asyncio

async def get_transactions(access_token: Annotated[str, Depends(get_access_token)]) -> dict:
    body = {
        "client_id": settings.plaid_client_id,
        "secret": settings.plaid_secret,
        "access_token": access_token,
        "count": 10,
    }

    try:
        headers = {
            "Content-Type": "application/json"
        }
        print(f"Request body for transactions: {body}")
        async with httpx.AsyncClient() as client:
            for _ in range(5):
                response = await client.post(api.TRANSACTIONS_SYNC, json=body, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                response_data = response.json()
                if response_data["transactions_update_status"] != "HISTORICAL_UPDATE_COMPLETE":
                    await asyncio.sleep(2)  
                    continue
                print(f"Received transactions response: {response_data}")
                return response_data
    
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        raise e
