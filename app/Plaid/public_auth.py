import httpx
from Splex.api import api
from Splex.model.plaid_public_token import PublicTokenResponseBody, PublicTokenRequestBody
from Splex.config import settings

async def get_public_token()->str:

    body = {
        "institution_id" : "ins_20",
        "initial_products" : ["transactions"],
        "options" : {
            "webhook": "https://www.genericwebhookurl.com/webhook",
        "override_username": "user_transactions_dynamic",
        "override_password": "test"
        }
    }
    req_body = PublicTokenRequestBody(**body)

    try:
        headers = {
            "Content-Type": "application/json"
        }
        print(f"Request body for public token: {req_body.dict}")
        async with httpx.AsyncClient() as client:
            response = await client.post(api.PUBLIC_TOKEN, json=req_body.dict, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            response_data = response.json()
            print(response_data)
            public_token_response = PublicTokenResponseBody(**response_data)
            print(f"Received public token response: {public_token_response.public_token}")
            return public_token_response.public_token
    
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        raise e
    
