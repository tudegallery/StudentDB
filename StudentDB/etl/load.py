import json
import yaml

with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

PROCESSED_PATH = config["paths"]["processed_data"]

def load(cleaned_data):
    with open(PROCESSED_PATH, "w") as f:
        json.dump(cleaned_data, f, indent=4)
    print(f"ETL Load: Data saved to {PROCESSED_PATH}")
