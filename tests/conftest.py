import os
from fastapi.testclient import TestClient
import pytest

from main import app
from db import get_db
from app.models.color import Color

os.environ["TESTING"] = "true"

@pytest.fixture(scope="module")
def client():
    # pytest fixture to set up the test environment
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def session():
    # Set up test session using the same method globally
    with get_db() as session:
        try:
            yield session  # Transaction starts
        finally:
            session.query(Color).delete()
            session.commit()
            session.close()