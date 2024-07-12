from pydantic_settings import BaseSettings, SettingsConfigDict

dot_env = 'eb_fast_api/env/.env'

class Settings(BaseSettings):
    kakaomap_local: str
    odsay: str

    model_config = SettingsConfigDict(env_file=dot_env, env_file_encoding='utf-8')

settings = Settings(_env_file=dot_env, _env_file_encoding='utf-8')