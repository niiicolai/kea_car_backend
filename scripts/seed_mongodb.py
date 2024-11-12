import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database

load_dotenv()

MONGO_DB_HOST=os.getenv("MONGO_DB_HOST")
MONGO_DB_PORT=os.getenv("MONGO_DB_PORT")
MONGO_DB_NAME=os.getenv("MONGO_DB_NAME")

accessories_file_path = "mongodb_insert_data.json"

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


