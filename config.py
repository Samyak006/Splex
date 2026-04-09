from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    '''
    Application configuration settings.
        Attributes:
        sqldb_url (str): The database connection URL.
    '''
    sqldb_url: str
    plaid_client_id: str
    plaid_secret: str

    '''
    Pydantic model configuration.
    model_config (SettingsConfigDict): Configuration for the Pydantic model.
    '''
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()