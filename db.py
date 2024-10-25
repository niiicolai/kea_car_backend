import os
from dotenv import load_dotenv
from contextlib import contextmanager
from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session

load_dotenv()

Base = declarative_base()

def get_db_connection_string(is_test: bool = False) -> str:
    """
    Creates a database engine using individual environment variables.
    """
    if is_test:
        db_user = os.getenv('TEST_DB_USER')
        db_password = os.getenv('TEST_DB_PASSWORD')
        db_host = os.getenv('TEST_DB_HOST')
        db_port = os.getenv('TEST_DB_PORT')
        db_name = os.getenv('TEST_DB_NAME')
    else:
        db_host = os.getenv('DB_HOST')
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_port = os.getenv('DB_PORT')

    connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return connection_string

def get_engine(is_test: bool = False) -> Engine:
    connection_string = get_db_connection_string(is_test)
    engine = create_engine(connection_string)
    return engine

session_local = sessionmaker(autocommit=False, autoflush=False)

@contextmanager
def get_db() -> Session:
    is_test = os.getenv('TESTING') == 'true'
    engine = get_engine(is_test)
    session = session_local(bind=engine)

    try:
        yield session
    finally:
        session.close()

def get_current_db_name(session: Session) -> str:
    # Use text() to create a text-based SQL expression
        result = session.execute(text("SELECT DATABASE();"))
        # Fetch the result
        return str(result.scalar())