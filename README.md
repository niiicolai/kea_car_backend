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

