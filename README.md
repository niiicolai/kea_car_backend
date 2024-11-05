# Python Project

## Setup Instructions

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. pip install -r requirements.txt
4. Create a .env file with these keys and ask for values:
   DB_HOST=your_host
   DB_NAME=your_db
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_PORT=your_port
   TESTING=false
   TEST_DB_HOST=your_test_host
   TEST_DB_NAME=your_test_db
   TEST_DB_USER=your_test_user
   TEST_DB_PASSWORD=your_test_password
   TEST_DB_PORT=your_test_port
   SECRET_KEY=Ask for the key
5. Run the project:
   python main.py

## Coverage
Generate coverage report:
```bash
scripts/coverage.sh           # Generate coverage report for default directory
scripts/coverage.sh path      # Generate coverage report for specific directory
```
