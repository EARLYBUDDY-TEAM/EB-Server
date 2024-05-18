from pydantic_settings import BaseSettings, SettingsConfigDict

dot_env = 'eb_server/env/.env'

class Settings(BaseSettings):
    kakao_rest_api_key: str

    model_config = SettingsConfigDict(env_file=dot_env, env_file_encoding='utf-8')

settings = Settings(_env_file=dot_env, _env_file_encoding='utf-8')