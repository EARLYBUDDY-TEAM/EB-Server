from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv = str(Path(__file__).parent.absolute()) + '/.env'

class Settings(BaseSettings):
    kakaomap: str
    odsay: str

    model_config = SettingsConfigDict(
        env_file=dotenv,
        env_file_encoding="utf-8",
    )

ENV = Settings()