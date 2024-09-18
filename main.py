from db import test_db_connection
from api import get_data_from_api
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "<h1>Welcome to the Car Sales Shop</h1>"

# Add more routes as needed for different parts of the web application
@app.route('/inventory')
def inventory():
    return "<h1>Inventory Page</h1>"

if __name__ == '__main__':
    print("Testing database connection...")
    test_db_connection()

    print("Fetching data from API...")
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = get_data_from_api(url)
    if data:
        print(f"API data: {data}")
        app.run(debug=True)
