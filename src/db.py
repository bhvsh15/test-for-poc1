import json

def connect():
    return {"host": "localhost", "port": 5432}

def get_all_records(db, table):
    ids = db.list_ids(table)
    return [db.get(table, i) for i in ids]

def clone_record(record):
    return json.loads(json.dumps(record))
