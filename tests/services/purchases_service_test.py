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
@pytest.mark.parametrize("options", [
    ({"limit": 1}),
])
def test_get_all_with_valid_partitions_and_boundaries(mySQLPurchaseRepository, options):
    purchases = purchases_service.get_all(mySQLPurchaseRepository, options["limit"])
    
    assert isinstance(purchases, list) and all(isinstance(purchase, PurchaseReturnResource) for purchase in purchases) \
        , f"Purchases are not a list of PurchaseReturnResource objects, but {type(purchases).__name__}"
    assert len(purchases) <= options["limit"], f"Number of purchases is greater than the limit of {options['limit']}"    

# INVALID TESTS FOR get_purchase_by_id

# VALID TESTS FOR get_purchase_by_car_id

# INVALID TESTS FOR get_purchase_by_car_id

# VALID TESTS FOR get_all_purchases

# INVALID TESTS FOR get_all_purchases

# VALID TESTS FOR create_purchase

# INVALID TESTS FOR create_purchase
