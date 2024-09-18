from db import test_db_connection
from api import get_data_from_api

if __name__ == '__main__':
    print("Testing database connection...")
    test_db_connection()

    print("Fetching data from API...")
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = get_data_from_api(url)
    if data:
        print(f"API data: {data}")
