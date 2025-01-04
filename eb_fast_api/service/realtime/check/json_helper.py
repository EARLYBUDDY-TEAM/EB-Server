import json
from datetime import datetime
from pathlib import Path


def filtered_json_name(
    station_name: str,
    now: datetime,
) -> str:
    file_path = Path(__file__).resolve().parent.joinpath("dummy")
    file_name = f"{station_name}_{now.strftime('%H:%M:%S')}.json"
    return f"{file_path}/{file_name}"


def json_to_dict(
    file_path: str,
) -> dict:
    with open(file_path, "r", encoding="utf-8-sig") as fp:
        return json.load(fp)


def save_dict_as_json_file(
    save_path: str,
    save_dict: dict,
):
    with open(
        save_path,
        "w",
        encoding="utf-8-sig",
    ) as fp:
        json.dump(
            save_dict,
            fp,
            ensure_ascii=False,
        )
