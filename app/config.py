from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
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
    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parent.parent / '.env')

settings = Settings()