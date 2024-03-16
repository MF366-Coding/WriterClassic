import json


def get_settings(file_location: str) -> dict[str, dict[str, str | int | bool] | bool | str | list[str] | int]:    
    with open(file_location, "r", encoding="utf-8") as config_file:
        configs: dict[str, dict[str, str | int | bool] | bool | str | list[str] | int] = json.load(config_file)
    
    return configs


def dump_settings(file_location: str, configs_dict: dict) -> None:
    with open(file_location, mode="wt", encoding="utf-8") as config_file:
        json.dump(configs_dict, config_file, indent=4)
