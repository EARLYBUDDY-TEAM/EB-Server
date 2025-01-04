def remove_last_station_name(
    station_name: str,
) -> str:
    if station_name.endswith("역"):
        return station_name[:-1]
    else:
        return station_name