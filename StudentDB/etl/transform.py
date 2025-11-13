def transform(data):
    cleaned = [d for d in data if d.get("name") and d.get("major")]
    print("ETL Transform: Data cleaned.")
    return cleaned
