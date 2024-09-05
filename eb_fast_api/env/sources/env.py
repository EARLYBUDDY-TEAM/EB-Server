from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


dot_env_dir = Path(__file__).parent.parent.absolute().joinpath("dot_env_files")
dot_api = dot_env_dir.joinpath(".api")
dot_mysql = dot_env_dir.joinpath(".mysql")


def API_VALUE(env_file: Path):
    class API_BaseSettings(BaseSettings):
        kakaomap: str
        odsay: str

        model_config = SettingsConfigDict(
            env_file=env_file,
            env_file_encoding="utf-8",
        )

    return API_BaseSettings()


def MYSQL_VALUE(env_file: Path):
    class MYSQL_BaseSettings(BaseSettings):
        MYSQL_PORT: int
        MYSQL_DATABASE: str
        MYSQL_USER: str
        MYSQL_PASSWORD: str

        model_config = SettingsConfigDict(
            env_file=env_file,
            env_file_encoding="utf-8",
            extra="ignore",
        )

    return MYSQL_BaseSettings()


ENV_API = API_VALUE(env_file=dot_api)
ENV_MYSQL = MYSQL_VALUE(env_file=dot_mysql)