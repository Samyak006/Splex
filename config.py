from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    sqldb_url: str
    plaid_client_id: str
    plaid_secret: str
    plaid_base_url: str
    is_only_integration: bool = True
    '''
    Pydantic model configuration.
    model_config (SettingsConfigDict): Configuration for the Pydantic model.
    '''
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()