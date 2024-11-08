#!/bin/bash
ls -la
ls -la scripts
echo "Waiting for MySQL to be available..."
bash ./scripts/wait-for-it.sh mysql:3306 --timeout=30 --strict -- echo "MySQL is up"

echo "Restoring MySQL dump..."
python ./scripts/restore_mysql.py --filepath="./scripts/mysql.sql"

echo "Starting FastAPI server..."
uvicorn main:app --host 0.0.0.0 --port 8000
