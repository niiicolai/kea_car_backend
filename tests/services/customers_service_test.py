import pytest
from pydantic import ValidationError
from app.services import customers_service
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource
from app.exceptions.database_errors import UnableToFindIdError

