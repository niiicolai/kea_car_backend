import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    return connection

def test_db_connection():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"Connected to database: {db_name[0]}")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    test_db_connection()
