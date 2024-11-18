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
    'models',
    'cars',
    'purchases'
]


def read_json():
    with open("./scripts/mongodb_insert_data.json", 'r') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data = read_json()
    client = MongoClient(host=MONGO_DB_HOST, port=int(MONGO_DB_PORT))
    db = client.get_database(MONGO_DB_NAME)

    db.drop_collection('accessories')
    db.create_collection('accessories').create_index('name', unique=True)
    db.drop_collection('brands')
    db.create_collection('brands').create_index('name', unique=True)
    db.drop_collection('cars')
    db.create_collection('cars')
    db.drop_collection('colors')
    db.create_collection('colors').create_index('name', unique=True)
    db.drop_collection('customers')
    db.create_collection('customers').create_index('email', unique=True)
    db.drop_collection('insurances')
    db.create_collection('insurances').create_index('name', unique=True)
    db.drop_collection('models')
    db.create_collection('models')
    db.drop_collection('purchases')
    db.create_collection('purchases').create_index('car._id', unique=True)
    db.drop_collection('sales_people')
    db.create_collection('sales_people').create_index('email', unique=True)

    for collection_name in collections:      
        bulk_operations = [
            UpdateOne({'_id': doc['_id']}, {'$set': doc}, upsert=True)
            for doc in data[collection_name]
        ]
        db.get_collection(collection_name).bulk_write(bulk_operations)

    client.close()
