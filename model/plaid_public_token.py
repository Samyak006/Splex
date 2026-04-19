from Splex.config import settings

class PublicTokenRequestBody:
    def __init__(self, institution_id: str, initial_products: list[str], options: dict):
        self.client_id = settings.plaid_client_id
        self.secret = settings.plaid_secret
        self.institution_id = institution_id
        self.initial_products = initial_products
        self.options = options
    
    @property
    def dict(self):
        return {
            "client_id": self.client_id,
            "secret": self.secret,
            "institution_id": self.institution_id,
            "initial_products": self.initial_products,
            "options": self.options
        }
    
    @dict.setter
    def dict(self, value):
        self.institution_id = value.get("institution_id", self.institution_id)
        self.initial_products = value.get("initial_products", self.initial_products)
        self.options = value.get("options", self.options)

class PublicTokenResponseBody:
    def __init__(self, public_token: str, request_id: str):
        self.public_token = public_token
        self.request_id = request_id

    @property
    def dict(self):
        return {
            "public_token": self.public_token,
            "request_id": self.request_id
        }
    @dict.setter
    def dict(self, value):
        self.public_token = value.get("public_token", self.public_token)
        self.request_id = value.get("request_id", self.request_id)