import json

def get_settings(file_location) -> dict:
    with open(file_location, "r", encoding="utf-8") as config_file:
        configs = json.load(config_file)
        config_file.close()
        
        return configs
    
def dump_settings(file_location, configs_dict):
    with open(file_location, "w", encoding="utf-8") as config_file:
        json.dump(obj=configs_dict, fp=file_location)
        config_file.close()
        