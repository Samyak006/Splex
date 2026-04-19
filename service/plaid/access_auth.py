import httpx
from Splex.api import api
from Splex.config import settings
from Splex.model.plaid_access_token import  AccessTokenResponseBody,AccessTokenRequestBody 
from Splex.model.plaid_public_token import PublicTokenResponseBody, PublicTokenRequestBody
from Splex.service.plaid.public_auth import get_public_token
from typing import Annotated
from fastapi import Depends

async def get_access_token(public_token: Annotated[str, Depends(get_public_token)]) -> str:
    body = {
        "public_token": public_token
    }
    req_body = AccessTokenRequestBody(**body)

    try:
        headers = {
            "Content-Type": "application/json"
        }
        print(f"Request body for access token: {req_body}")
        async with httpx.AsyncClient() as client:
            response = await client.post(api.ACCESS_TOKEN, json=req_body.dict, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            response_data = response.json()
            print(f"Received access token response: {response_data}")
            access_token = AccessTokenResponseBody(**response_data)
            print(f"Extracted access token: {access_token.access_token}")
            return access_token.access_token
    
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        raise e