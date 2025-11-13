import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DB_DIR, exist_ok=True)

DB_FILE = os.path.join(DB_DIR, "students.json")

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("File rusak, membuat ulang.")
                return []
    return []

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
