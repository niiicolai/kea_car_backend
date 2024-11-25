import pytest
from app.services import purchases_service
from app.exceptions.database_errors import (
    PurchaseDeadlineHasPastError,
    AlreadyTakenFieldValueError,
    UnableToFindEntityError,
    UnableToFindIdError
)
from app.resources.purchase_resource import (
    PurchaseCreateResource,
    PurchaseReturnResource
)

# VALID TESTS FOR get_purchase_by_id

# INVALID TESTS FOR get_purchase_by_id

# VALID TESTS FOR get_purchase_by_car_id

# INVALID TESTS FOR get_purchase_by_car_id

# VALID TESTS FOR get_all_purchases

# INVALID TESTS FOR get_all_purchases

# VALID TESTS FOR create_purchase

# INVALID TESTS FOR create_purchase
