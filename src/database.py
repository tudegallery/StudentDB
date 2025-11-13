import json
import os
import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

RAW_DATA_PATH = config["paths"]["raw_data"]

def load_data():
    if not os.path.exists(RAW_DATA_PATH) or os.path.getsize(RAW_DATA_PATH) == 0:
        return []
    with open(RAW_DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(RAW_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)
