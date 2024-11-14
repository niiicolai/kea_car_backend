#!/bin/bash

MYSQL_HOST="mysql"
MYSQL_PORT="3306"

MONGO_HOST="mongodb"
MONGO_PORT="27017"

NEO4J_HOST="neo4j"
NEO4J_PORT="7474"

if [ -z "$MYSQL_USER" ]; then
    echo "MYSQL_USER is not set. Exiting..."
    exit 1
fi

if [ -z "$MYSQL_ROOT_PASSWORD" ]; then
    echo "MYSQL_ROOT_PASSWORD is not set. Exiting..."
    exit 1
fi

until mysqladmin ping -h "$MYSQL_HOST" -P "$MYSQL_PORT" --user="$MYSQL_USER" --password="$MYSQL_ROOT_PASSWORD" --silent; do
     echo "Waiting for MySQL to be ready..."
     sleep 2
done

until mongosh --host "$MONGO_HOST" --port "$MONGO_PORT" --eval "db.adminCommand('ping')" > /dev/null 2>&1; do
    echo "Waiting for MongoDB to be ready..."
    sleep 2
done

until curl -s http://$NEO4J_HOST:$NEO4J_PORT/ | grep -q "neo4j"; do
    echo "Waiting for Neo4j to be ready..."
    sleep 2
done

echo "Waiting for MySQL to be available..."
bash ./scripts/wait-for-it.sh mysql:3306 --timeout=30 --strict -- echo "MySQL is up"

echo "Restoring MySQL dump..."
python ./scripts/restore_mysql.py --filepath="./scripts/mysql.sql"

echo "Restoring MongoDB dump..."
python ./scripts/seed_mongodb.py

echo "Starting FastAPI server..."
uvicorn main:app --host 0.0.0.0 --port 8000
