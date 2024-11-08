import os
from dotenv import load_dotenv
from contextlib import contextmanager
from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session

load_dotenv()

Base = declarative_base()

def get_db_connection_string() -> str:
    """
    Creates a database engine using individual environment variables.
    """
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')

    # When using docker, we don't need to specify the port.
    # Instead, we only specify the host as the service name.
    port = f':{db_port}' if db_port else '' 
    
    connection_string = f'mysql://{db_user}:{db_password}@{db_host}{port}/{db_name}'
    
    return connection_string

def get_engine() -> Engine:
    connection_string = get_db_connection_string()
    engine = create_engine(connection_string, echo=True, pool_pre_ping=True)
    return engine

session_local = sessionmaker(autocommit=False, autoflush=False)

@contextmanager
def get_db() -> Session:
    engine = get_engine()
    session = session_local(bind=engine)
    try:
        yield session
    finally:
        session.close()
