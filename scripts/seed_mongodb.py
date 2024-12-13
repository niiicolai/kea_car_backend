import json
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
from pymongo import MongoClient, UpdateOne, IndexModel


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
    try:
        with open('./scripts/mongodb_insert_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        with open('mongodb_insert_data.json', 'r') as file:
            return json.load(file)


if __name__ == '__main__':
    start_time = datetime.now()
    print(f"SEED_MONGODB: {start_time}: Starting MongoDB restore:\n"
          f"MongoDB host: {MONGO_DB_HOST}\n"
          f"MongoDB port: {MONGO_DB_PORT}\n"
          f"MongoDB name: {MONGO_DB_NAME}")

    try:
        data = read_json()
        future_date = date.today() + timedelta(days=30)
        formatted_date = future_date.strftime("%Y-%m-%d")
        car_id = "a5503fbb-c388-4789-a10c-d7ae7bdf7408"
        for car in data['cars']:
            if car['_id'] == car_id:
                car['purchase_deadline'] = formatted_date
                break

        client = MongoClient(host=MONGO_DB_HOST, port=int(MONGO_DB_PORT))
        db = client.get_database(MONGO_DB_NAME)

        db.drop_collection('accessories')
        db.create_collection('accessories').create_index('name', unique=True)
        db.drop_collection('brands')
        db.create_collection('brands').create_index('name', unique=True)
        db.drop_collection('cars')
        db.create_collection('cars').create_indexes([IndexModel('customer._id'), IndexModel('sales_person._id')])
        db.drop_collection('colors')
        db.create_collection('colors').create_index('name', unique=True)
        db.drop_collection('customers')
        db.create_collection('customers').create_index('email', unique=True)
        db.drop_collection('insurances')
        db.create_collection('insurances').create_index('name', unique=True)
        db.drop_collection('models')
        db.create_collection('models').create_indexes([IndexModel('brand._id'), IndexModel('name')])
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
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"Successfully restored the MongoDB database, it took {duration} seconds.")
    except Exception as error:
        print(f"Error {error.__class__.__name__} caught during Mongo Database restore:\n"
              f"{error}")
