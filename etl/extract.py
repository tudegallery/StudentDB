from src.database import load_data
from Development.Python.StudentDB.src.utils.logger import log

def extract():
    data = load_data()
    log("ETL Extract: Data loaded successfully.")
    return data
