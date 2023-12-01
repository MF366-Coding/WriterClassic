import json

def get_settings(file_location) -> dict:
    with open(file_location, "r", encoding="utf-8") as config_file:
        configs = json.load(config_file)
        config_file.close()
        
        return configs
    
def dump_settings(file_location, configs_dict: dict):
    with open(file_location, mode="wt", encoding="utf-8") as config_file:
        json.dump(configs_dict, config_file, indent=4)
        config_file.close()
        