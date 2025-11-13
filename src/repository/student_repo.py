import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.json')


def load_students():
    """Membaca data mahasiswa dari file JSON."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    """Menyimpan data mahasiswa ke file JSON."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(students, file, indent=4, ensure_ascii=False)
