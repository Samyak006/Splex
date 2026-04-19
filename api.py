# config/endpoints.py
from Splex.config import settings  # your env loader object

class PlaidEndpoints:
    BASE = settings.plaid_base_url  # reads from .env (sandbox or production)
    
    PUBLIC_TOKEN = f"{BASE}/sandbox/public_token/create"
    ACCESS_TOKEN = f"{BASE}/item/public_token/exchange"
    TRANSACTIONS_GET = f"{BASE}/transactions/get"
    TRANSACTIONS_SYNC = f"{BASE}/transactions/sync"
    ITEM_PUBLIC_TOKEN_EXCHANGE = f"{BASE}/item/public_token/exchange"

api = PlaidEndpoints()  # instantiate to use as api.PUBLIC_TOKEN, etc.
