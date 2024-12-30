# Python Project
[![CI/CD](https://github.com/niiicolai/kea_car_backend/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/niiicolai/kea_car_backend/actions/workflows/ci-cd.yaml) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

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
```
   * DB_HOST=your_local_mysql_host (localhost)
   * DB_NAME=your_local_mysql_db_name (kea_cars_dev)
   * DB_USER=your_local_mysql_user_name (root)
   * DB_PASSWORD=your_local_mysql_password
   * DB_PORT=your_local_mysql_port (3306)
   * TEST_DB_NAME=kea_cars_test
   * MONGO_DB_HOST=your_local_mongo_host (localhost)
   * MONGO_DB_PORT=your_local_mongo_db_port (27017)
   * MONGO_DB_NAME=your_local_mongo_db_name (kea_cars_dev)
   * NEO4J_URI=your_local_neo4j_uri (bolt://localhost:7687)
   * NEO4J_USER=your_local_neo4j_db_user_name (neo4j)
   * NEO4J_PASSWORD=your_local_neo4j_db_password
   * SECRET_KEY=Ask for the key
```
5. Run the project:
   ```bash
   uvicorn main:app --reload --log-level debug
    ```


## Coverage
Generate coverage report:
```bash
coverage run --source=app -m pytest  # Run the tests and generate the coverage report
coverage report --fail-under=80      # Show the coverage report and fail if the coverage is under 80%
coverage html                        # Generate the HTML coverage report
```

Generate coverage using the `coverage.sh` script (combine the above commands):
```bash
scripts/coverage.sh           # Generate coverage report for default directory
scripts/coverage.sh path      # Generate coverage report for specific directory
```

## Pylint
For linting the project, run the following command:
```bash	
pylint app/*                  # Lint the app directory
pylint app/* --fail-under=7.0 # Lint the app directory and fail if the score is under 7.0
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

## Load Testing
The project include test plans for stress-testing, load-testing and spike-testing of the frontend and backend implemented with JMeter. The test plans are located in the `performance-tests` directory.
```bash
# Run the stress test and generate the report
jmeter -n -t ./performance-tests/stress-test/Stress-Test-Plan.jmx -l log.jtl -e -o ./stress-test-html-report

# Run the load test and generate the report
jmeter -n -t ./performance-tests/load-test/Load-Test-Plan.jmx -l log.jtl -e -o ./load-test-html-report

# Run the spike test and generate the report
jmeter -n -t ./performance-tests/spike-test/Spike-Test-Plan.jmx -l log.jtl -e -o ./spike-test-html-report
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

## MySQL Restore
To restore the database from a MySQL dump, run the following command:
```bash
# Restore the database using the specified file
python scripts/restore_mysql.py --filepath="path/to/dump" 

# Show the help message
python scripts/restore_mysql.py --help
```

**Examples**:
```bash
# Restore the database using the mysql dump file in the '/scripts' directory
python scripts/restore_mysql.py --filepath="./scripts/mysql.sql"

# Restore the database using the mysql dump file in the '/backups' directory. Replace <INSERT_DUMP_NAME> with the name of the dump file.
python scripts/restore_mysql.py --filepath="./backups/<INSERT_DUMP_NAME>.sql"
```

Note: The script will overwrite the existing database with the data from the dump file.

## Mongo Database Restore
To restore the database from a Mongo dump, do remember to have a local mongodb called kea_cars_dev, 
run the following command:
```bash
# Restore the database using the specified file
python scripts/seed_mongodb.py
```

Note: The script will overwrite the existing database with the data from the seed file.

## Neo4j Database Restore
To restore the database from a Neo4j dump, do remember to have a local neo4j database called kea_cars_dev and have it running, 
run the following command:
```bash
# Restore the database using the specified file
python scripts/seed_neo4j.py
```

Note: The script will overwrite the existing database with the data from the seed file.

## Docker
To build the Docker image, run the following command:
```bash
docker build -t kea_car_backend:v1.0 .
```

To run the Docker container, run the following command:
```bash
docker run -p 8000:8000 kea_car_backend:v1.0
```

## Docker Compose
You must build the Docker image before running the Docker Compose command.
The docker-compose.yml file is designed to run the backend and the database together.
When you start the Docker Compose, it will restore the database from the dump file found in the 'scripts' directory.
```bash
docker-compose -f docker-compose.yml up
```
