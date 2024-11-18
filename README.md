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

## CI/CD
The CI/CD pipeline is configured using GitHub Actions.

The pipeline consists of the following stages:
1. pre-test
2. deploy-staging
3. load-test
4. deploy-production

The `pre-test` pipeline consists of following checks that must pass:
1. All pytest
2. Coverage must be at least 80%
3. Pylint score must be at least 7.0
4. All API tests must pass
5. All End-to-end tests must pass

The `deploy-staging` pipeline consists of following checks that must pass:
1. Copy the application to the staging server
2. Build the Docker image using the Dockerfile
3. Run the `docker-compose.yaml` file to start all required services

The `load-test` pipeline consists of following checks that must pass:
1. Run the load test on the staging server
2. All CPU Thresholds must pass

The `deploy-production` pipeline consists of following checks that must pass:
1. Copy the application to the production server
2. Build the Docker image using the Dockerfile
3. Run the `docker-compose.yaml` file to start all required services

## Demonstration Flow
The project contains a GitHub Action that can be used to demonstrate a minifed version of the CI/CD pipeline.
The file is called `short-ci-cd.yaml` and can be found in the `.github/workflows` directory.
It is designed to run on push events to a branch called `demo`.

The GitHub Action contains a single job called `test` that runs the following checks:
1. All pytest
2. Pylint score must be at least 7.0
3. All API tests must pass
4. All End-to-end tests must pass  

### Example

1. Create a new branch or use an existing branch called `demo`
```bash	
# Create a new branch called demo
git checkout -b demo 

# Use an existing branch called demo
git checkout demo
```

2. Make some changes to the code and push the changes to the `demo` branch on GitHub
```bash
git add .
git commit -m "I changed ..."
git push origin demo
```

The GitHub action will automatically run the checks at this point and can be found under the Actions tab on GitHub.
To clean up after the demonstration, merge the `demo` branch into the `main` branch by creating a pull request on GitHub.

