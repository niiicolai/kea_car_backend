import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import logging
import argparse

load_dotenv()

host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
root_user = os.getenv('MYSQL_USER')
username = root_user if root_user else os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

def dump(backup_dir: str, backup_name: str = None):
    if host is None or database is None or username is None or password is None or port is None:
        return logging.error("DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, or DB_PORT is not set in the .env file")
    if backup_dir is None:
        raise ValueError("backup_dir is required")
    
    print(f"MYSQL_BACKUP: {datetime.now()}: Starting MySQL backup")
    try:
        # Create the backup directory if it does not exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        # Define the dump file name
        if backup_name:
            dump_file_name = os.path.join(backup_dir, f"{backup_name}.sql")
        else:
            unix_timestamp = int(datetime.now().timestamp())
            dump_file_name = os.path.join(backup_dir, f"backup_{unix_timestamp}.sql")
        
        print(f"Dump file will be saved to: {dump_file_name}")

        # Define the mysqldump command
        mysqldump_command = [
            'mysqldump',
            f'--user={username}',
            f'--password={password}',
            f'--host={host}',
            f'--port={port}',
            '--no-tablespaces',
            database
        ]
        
        # Run the mysqldump command
        with open(dump_file_name, 'w') as dump_file:
            result = subprocess.run(mysqldump_command, stdout=dump_file, stderr=subprocess.PIPE, text=True)

        # Check if the dump was successful
        if result.returncode != 0:
            print(f"Error creating dump: {result.stderr}")
            return

        print(f"MYSQL_BACKUP: {datetime.now()}: Finished MySQL backup")

    except Exception as error:
        print(f"MYSQL_BACKUP: {datetime.now()}: Error during MySQL backup: {error}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the dump function with a specified directory.")
    parser.add_argument('--directory', type=str, required=True, help="The directory to use for the dump")    
    parser.add_argument('--filename', type=str, required=False, help="The name of the dump file")    
    
    args = parser.parse_args()

    dump(args.directory, args.filename)