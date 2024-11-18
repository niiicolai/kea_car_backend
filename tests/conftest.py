import main # Import main to ensure all classes are loaded
import pytest

from db import get_db
from app.repositories.color_repositories import MySQLColorRepository
from app.repositories.customer_repositories import MySQLCustomerRepository
from app.repositories.accessory_repositories import MySQLAccessoryRepository
from app.repositories.brand_repositories import MySQLBrandRepository
from app.repositories.car_repositories import MySQLCarRepository
from app.repositories.insurance_repository import MySQLInsuranceRepository
from app.repositories.model_repositories import MySQLModelRepository
from app.repositories.purchase_repositories import MySQLPurchaseRepository
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository

@pytest.fixture(scope="function")
def mySQLColorRepository(session):
    return MySQLColorRepository(session)

@pytest.fixture(scope="function")
def mySQLCustomerRepository(session):
    return MySQLCustomerRepository(session)

@pytest.fixture(scope="function")
def mySQLAccessoryRepository(session):
    return MySQLAccessoryRepository(session)

@pytest.fixture(scope="function")
def mySQLBrandRepository(session):
    return MySQLBrandRepository(session)

@pytest.fixture(scope="function")
def mySQLCarRepository(session):
    return MySQLCarRepository(session)

@pytest.fixture(scope="function")
def mySQLInsuranceRepository(session):
    return MySQLInsuranceRepository(session)

@pytest.fixture(scope="function")
def mySQLModelRepository(session):
    return MySQLModelRepository(session)

@pytest.fixture(scope="function")
def mySQLPurchaseRepository(session):
    return MySQLPurchaseRepository(session)

@pytest.fixture(scope="function")
def mySQLSalesPersonRepository(session):
    return MySQLSalesPersonRepository(session)

@pytest.fixture(scope="function")
def session():
    with get_db() as session:
        try:
            yield session
        finally:
            session.rollback()