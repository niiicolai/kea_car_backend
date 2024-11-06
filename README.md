# Python Project
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## Setup Instructions

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies in the requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file with these keys and ask for values:
   DB_HOST=your_host
   DB_NAME=your_db
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_PORT=your_port
   SECRET_KEY=Ask for the key
5. Run the project:
   python main.py


## Coverage
Generate coverage report:
```bash
scripts/coverage.sh           # Generate coverage report for default directory
scripts/coverage.sh path      # Generate coverage report for specific directory
```

## Pylint
For linting the project, run the following command:
```bash	
pylint app                    # Lint the app directory
```
Note: The configuration file for pylint is `.pylintrc`.

## API Testing
To test the API tests, you can either import the collection and environment files into Postman or use newman to run the tests from the command line and the `scripts/api_test.py` script.
```bash
# Install newman globally if you haven't already
# Note: This requires Node.js to be installed on your system
# Note: Only required the first time
npm install -g newman

# Usage
newman run <collection> -e <environment>
```

**Examples**:
```bash
# Run the API tests with the MySQL environment
newman run "./api-tests/KEA Car API Test.postman_collection.json" -e "./api-tests/KEA Car Mysql.postman_environment.json"
```

## MySQL Dump
To dump the database, run the following command:
```bash
# Dump the database to the specified directory
python scripts/dump_mysql.py --directory="path/to/dump" 

# Dump the database to the specified directory with the specified filename
python scripts/dump_mysql.py --directory="path/to/dump" --filename="filename"

# Show the help message
python scripts/dump_mysql.py --help
```

**Examples**:
```bash
# Dump the database to the '/scripts' directory with the name 'mysql'
# to update the MySQL script used in the CI pipeline.
python scripts/dump_mysql.py --directory="./scripts" --filename="mysql"

# Create a backup of the database in the '/backups' directory with the default name.
# The default name is a timestamp to keep track of the backups.
python scripts/dump_mysql.py --directory="./backups/mysql"
```

Note: The script will create the output directory if it does not exist.