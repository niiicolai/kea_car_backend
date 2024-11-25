import pytest
from app.services import cars_service
from app.exceptions.database_errors import (
    UnableToFindIdError,
    TheColorIsNotAvailableInModelToGiveToCarError,
    UnableToDeleteCarWithoutDeletingPurchaseTooError
)
from app.resources.car_resource import CarCreateResource, CarReturnResource

# VALID TESTS FOR get_car_by_id

# INVALID TESTS FOR get_car_by_id

# VALID TESTS FOR get_all_cars

# INVALID TESTS FOR get_all_cars

# VALID TESTS FOR create_car

# INVALID TESTS FOR create_car

# VALID TESTS FOR delete_car

# INVALID TESTS FOR delete_car
