import json

def load_config(config_filepath: str):
    with open(config_filepath) as f:
        config_data = json.load(f)
    return config_data