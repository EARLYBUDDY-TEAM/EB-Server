# from pathlib import Path
# from pydantic_settings import BaseSettings, SettingsConfigDict

# dotenv = str(Path(__file__).parent.absolute()) + '/.env'

# class Settings(BaseSettings):
#     kakaomap: str
#     odsay: str

#     model_config = SettingsConfigDict(
#         env_file=dotenv,
#         env_file_encoding="utf-8",
#     )

# ENV = Settings()

import yaml
from pathlib import Path
from typing import Optional
from enum import Enum


class KEY(str, Enum):
    kakaomap = "kakaomap"
    odsay = "odsay"
    port = "port"
    postgres_id = "postgres_id"
    postgres_pwd = "postgres_pwd"


current_dir = Path(__file__).absolute().parent
file_name = "env.yaml"
env_file_path = current_dir.joinpath(file_name)


def read_yaml() -> Optional[dict]:
    try:
        with open(env_file_path, "r") as f:
            yaml_file = yaml.safe_load(f)
        return yaml_file
    except:
        return None


def write_yaml(env_dict: dict):
    with open(env_file_path, "w") as f:
        yaml.dump(env_dict, f)
    return


def get_value(
    key: KEY,
    env_dict: Optional[dict] = read_yaml(),
):
    if env_dict == None:
        return None
    else:
        return env_dict.get(key.value)


class VALUE:
    kakaomap: str
    odsay: str
    port: int
    postgres_id: str
    postgres_pwd: str

    def __init__(self):
        self.kakaomap = get_value(KEY.kakaomap) or "kakaomap"
        self.odsay = get_value(KEY.odsay) or "odsay"
        self.port = get_value(KEY.port)
        self.postgres_id = get_value(KEY.postgres_id) or "postgres_id"
        self.postgres_pwd = get_value(KEY.postgres_pwd) or "postgres_pwd"


ENV = VALUE()


if __name__ == "__main__":
    import sys

    port = sys.argv[1]
    env_dict = read_yaml()
    to_update = {KEY.port.value: port}
    if env_dict:
        env_dict.update(to_update)
        write_yaml(env_dict)
