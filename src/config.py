import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = Field("development", validation_alias="ENVIRONMENT")
    api_key: str = Field(..., validation_alias="API_KEY")

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

if os.environ.get("ENVIRONMENT") == "test":
    settings = Settings(_env_file='.env.test', _env_file_encoding='utf-8')
else:
    settings = Settings()