from src.database import load_data
from src.logger import log

def extract():
    data = load_data()
    log("ETL Extract: Data loaded successfully.")
    return data
