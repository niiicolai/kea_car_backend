import main # Import main to ensure all classes are loaded
import pytest
import random
import string
from uuid import uuid4
from datetime import date, timedelta
from scripts.restore_mysql import restore

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

@pytest.fixture(scope="session", autouse=True)
def setup_once():
    restore("scripts/mysql.sql")

@pytest.fixture(scope="function")
def valid_customer_data() -> dict:
    domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
    domain = random.choice(domains)
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    phone_number = f"+45{random.randint(10000000, 99999999)}"
    first_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 10))).capitalize()
    last_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 10))).capitalize()
    address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(10, 30)))
    return \
        {
            "email": f"{username}@{domain}",
            "phone_number": phone_number,
            "first_name": first_name,
            "last_name": last_name,
            "address": address
        }
        
@pytest.fixture(scope="function")
def valid_car_data() -> dict[str, any]:
    purchase_deadline = date.today() + timedelta(days=1)
    model_id = uuid4()
    color_id = uuid4()
    customer_id = uuid4()
    sales_person_id = uuid4()
    accessories = [uuid4() for _ in range(random.randint(0, 5))]
    insurances = [uuid4() for _ in range(random.randint(0, 5))]
    return \
        {
            "purchase_deadline": purchase_deadline,
            "models_id": model_id,
            "colors_id": color_id,
            "customers_id": customer_id,
            "sales_people_id": sales_person_id,
            "accessory_ids": accessories,
            "insurance_ids": insurances
        }


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
    with get_db(is_test_db=True) as session:
        try:
            yield session
        finally:
            session.rollback()
