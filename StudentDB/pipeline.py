from etl.extract import extract
from etl.transform import transform
from etl.load import load
from src.logger import log

def run_pipeline():
    log("ETL Pipeline started.")
    data = extract()
    cleaned = transform(data)
    load(cleaned)
    log("ETL Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
