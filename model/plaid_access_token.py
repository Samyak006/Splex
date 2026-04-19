from Splex.config import settings

class AccessTokenRequestBody:
    def __init__(self, public_token: str):
        self.client_id = settings.plaid_client_id
        self.secret = settings.plaid_secret
        self.public_token = public_token
    
    @property
    def dict(self):
        return {
            "client_id": self.client_id,
            "secret": self.secret,
            "public_token": self.public_token
        }
    @dict.setter
    def dict(self, value):
        self.client_id = value.get("client_id", self.client_id)
        self.secret = value.get("secret", self.secret)
        self.public_token = value.get("public_token", self.public_token)
        
class AccessTokenResponseBody:
    def __init__(self, access_token: str, item_id: str, request_id: str):
        self.access_token = access_token
        self.item_id = item_id
        self.request_id = request_id
    
    @property
    def dict(self):
        return {
            "access_token": self.access_token,
            "item_id": self.item_id,
            "request_id": self.request_id
        }
    @dict.setter
    def dict(self, value):
        self.access_token = value.get("access_token", self.access_token)
        self.item_id = value.get("item_id", self.item_id)
        self.request_id = value.get("request_id", self.request_id)