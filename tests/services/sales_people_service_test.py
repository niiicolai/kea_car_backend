import pytest
from app.services import sales_people_service
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.exceptions.invalid_credentials_errors import IncorrectEmailError, IncorrectPasswordError
from app.resources.sales_person_resource import (
    SalesPersonLoginResource, SalesPersonReturnResource, SalesPersonCreateResource
)
from app.core.security import Token


# VALID TESTS FOR get_sales_person_by_id

# INVALID TESTS FOR get_sales_person_by_id

# VALID TESTS FOR get_all_sales_people

# INVALID TESTS FOR get_all_sales_people

# VALID TESTS FOR login_sales_person

# INVALID TESTS FOR login_sales_person

# VALID TESTS FOR create_sales_person

# INVALID TESTS FOR create_sales_person
