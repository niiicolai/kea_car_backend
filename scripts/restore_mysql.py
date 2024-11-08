import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import logging
import argparse

load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

def restore(filepath: str):
    if host is None or database is None or username is None or password is None:
        return logging.error("DB_HOST, DB_NAME, DB_USER, or DB_PASSWORD is not set in the .env file")
    if filepath is None:
        raise ValueError("filepath is required")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
        
    print(f"MYSQL_RESTORE: {datetime.now()}: Starting MySQL restore")
    try:
        mysql_command = [
            'mysql',
            f'--user={username}',
            f'--password={password}',
            f'--host={host}'
        ]
        
        if port: mysql_command.append(f'--port={port}')
        else: mysql_command.append(f'--port=3306')
        
        mysql_command.append(database)
        
        # Run the restore command
        with open(filepath, 'r') as dump_file:
            print(f"Restoring dump from: {filepath}")
            print(f"Command: {' '.join(mysql_command)}")
            result = subprocess.run(mysql_command, stdin=dump_file, stderr=subprocess.PIPE, text=True)
            
        # Check if the restore was successful
        if result.returncode != 0:
            print(f"Error restoring dump: {result.stderr}")
            return
        
        print(f"MYSQL_RESTORE: {datetime.now()}: Finished MySQL restore")

    except Exception as error:
        print(f"MYSQL_RESTORE: {datetime.now()}: Error during MySQL restore: {error}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the restore function with a specified directory.")
    parser.add_argument('--filepath', type=str, required=True, help="The file path to the dump file to restore")  
    
    args = parser.parse_args()

    restore(args.filepath)