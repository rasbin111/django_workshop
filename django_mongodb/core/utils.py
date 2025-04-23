import pymongo

def get_db_handle(db_name, username, password, host, port):
    client = pymongo.MongoClient(host=host, port=int(port), username=username, password=password)
    db_handle = client["django_mongo"]
    return db_handle, client