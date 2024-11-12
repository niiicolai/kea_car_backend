import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne


load_dotenv()

MONGO_DB_HOST = os.getenv("MONGO_DB_HOST")
MONGO_DB_PORT = os.getenv("MONGO_DB_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

collections = [
    'accessories',
    'insurances',
    'customers',
    'sales_people',
    'colors',
    'brands',
    'models'
]


def read_json():
    with open("mongodb_insert_data.json", 'r') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data = read_json()
    client = MongoClient(host=MONGO_DB_HOST, port=int(MONGO_DB_PORT))
    db = client[MONGO_DB_NAME]

    for collection_name in collections:
        bulk_operations = [
            UpdateOne({'_id': doc['_id']}, {'$set': doc}, upsert=True)
            for doc in data[collection_name]
        ]
        db.get_collection(collection_name).bulk_write(bulk_operations)

    client.close()
