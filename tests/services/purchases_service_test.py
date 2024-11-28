import pytest
import datetime
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


# VALID TESTS FOR get_all
@pytest.mark.parametrize("options", [
    ({"limit": 1}),
    ({"limit": 2}),
    ({"limit": 3}),
    ({"limit": None}),
])
def test_get_all_with_valid_partitions_and_boundaries(mySQLPurchaseRepository, options):
    purchases = purchases_service.get_all(mySQLPurchaseRepository, options["limit"])
    
    assert isinstance(purchases, list), f"Purchases is not a list, but {type(purchases).__name__}"
    assert all(isinstance(purchase, PurchaseReturnResource) for purchase in purchases) \
        , f"Purchases are not a list of PurchaseReturnResource objects, but {type(purchases).__name__}"
    
    if options["limit"] is not None:
        assert len(purchases) <= options["limit"], f"Number of purchases is greater than the limit of {options['limit']}"
    

# INVALID TESTS FOR get_all
@pytest.mark.parametrize("options, errorType, errorMessage", [
    ({"limit": True}, TypeError, "purchases_limit must be of type int or None, not bool."),
    ({"limit": False}, TypeError, "purchases_limit must be of type int or None, not bool."),
    ({"limit": []}, TypeError, "purchases_limit must be of type int or None, not list."),
    ({"limit": {}}, TypeError, "purchases_limit must be of type int or None, not dict."),
    ({"limit": "a"}, TypeError, "purchases_limit must be of type int or None, not str."),
    ({"limit": ""}, TypeError, "purchases_limit must be of type int or None, not str."),
])
def test_get_all_with_invalid_partitions_and_boundaries(mySQLPurchaseRepository, options, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        purchases_service.get_all(mySQLPurchaseRepository, options["limit"])


# VALID TESTS FOR get_by_id
@pytest.mark.parametrize("id, expected", [
    ("bdfca7c4-e0ad-4618-8766-9bb355371c81", {
         "id": "bdfca7c4-e0ad-4618-8766-9bb355371c81", 
         "cars_id": "d4c7f1f8-4451-43bc-a827-63216a2ddece", 
         "date_of_purchase": "2024-11-04"
    }),
])
def test_get_by_id_with_valid_partitions_and_boundaries(mySQLPurchaseRepository, id, expected):
    purchase = purchases_service.get_by_id(mySQLPurchaseRepository, id)
    
    assert isinstance(purchase, PurchaseReturnResource), f"Purchase is not a PurchaseReturnResource object, but {type(purchase).__name__}"
    assert purchase.id == expected["id"], f"Purchase id is not {expected['id']}, but {purchase.id}"
    assert purchase.car.id == expected["cars_id"], f"Purchase cars_id is not {expected['cars_id']}, but {purchase.cars_id}"
    assert str(purchase.date_of_purchase) == expected["date_of_purchase"], f"Purchase date_of_purchase is not {expected['date_of_purchase']}, but {purchase.date_of_purchase}"


# INVALID TESTS FOR get_by_id
@pytest.mark.parametrize("id, errorType, errorMessage", [
    ("", UnableToFindIdError, "Purchase with ID:  does not exist."),
    ("fake_id", UnableToFindIdError, "Purchase with ID: fake_id does not exist."),
    (None, TypeError, "purchase_id must be of type str, not None."),
    ({}, TypeError, "purchase_id must be of type str, not dict."),
    ([], TypeError, "purchase_id must be of type str, not list."),
    (True, TypeError, "purchase_id must be of type str, not bool."),
    (False, TypeError, "purchase_id must be of type str, not bool."),
])
def test_get_by_id_with_invalid_partitions_and_boundaries(mySQLPurchaseRepository, id, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        purchases_service.get_by_id(mySQLPurchaseRepository, id)


# VALID TESTS FOR get_by_car_id
@pytest.mark.parametrize("id, expected", [
    ("d4c7f1f8-4451-43bc-a827-63216a2ddece", {
        "id": "bdfca7c4-e0ad-4618-8766-9bb355371c81", 
        "cars_id": "d4c7f1f8-4451-43bc-a827-63216a2ddece", 
        "date_of_purchase": "2024-11-04"
    }),
])
def test_get_by_car_id_with_valid_partitions_and_boundaries(mySQLPurchaseRepository, mySQLCarRepository, id, expected):
    purchase = purchases_service.get_by_car_id(mySQLPurchaseRepository, mySQLCarRepository, id)
    
    assert isinstance(purchase, PurchaseReturnResource), f"Purchase is not a PurchaseReturnResource object, but {type(purchase).__name__}"
    assert purchase.id == expected["id"], f"Purchase id is not {expected['id']}, but {purchase.id}"
    assert purchase.car.id == expected["cars_id"], f"Purchase cars_id is not {expected['cars_id']}, but {purchase.cars_id}"
    assert str(purchase.date_of_purchase) == expected["date_of_purchase"], f"Purchase date_of_purchase is not {expected['date_of_purchase']}, but {purchase.date_of_purchase}"


# INVALID TESTS FOR get_by_car_id
@pytest.mark.parametrize("id, errorType, errorMessage", [
    ("", UnableToFindIdError, "Car with ID:  does not exist."),
    ("fake_id", UnableToFindIdError, "Car with ID: fake_id does not exist."),
    (None, TypeError, "car_id must be of type str, not None."),
    ({}, TypeError, "car_id must be of type str, not dict."),
    ([], TypeError, "car_id must be of type str, not list."),
    (True, TypeError, "car_id must be of type str, not bool."),
    (False, TypeError, "car_id must be of type str, not bool."),
])
def test_get_by_car_id_with_invalid_partitions_and_boundaries(mySQLPurchaseRepository, mySQLCarRepository, id, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        purchases_service.get_by_car_id(mySQLPurchaseRepository, mySQLCarRepository, id)

# VALID TESTS FOR create
@pytest.mark.parametrize("purchaseCreateResource", [
    (PurchaseCreateResource(cars_id="0be86135-c58f-43b6-a369-a3c5445b9948", date_of_purchase=None)),
    (PurchaseCreateResource(cars_id="a1b1e305-1a89-4b06-86d1-21ac1fa3c8a6", date_of_purchase=datetime.datetime.now().date())),
])
def test_create_with_valid_partitions_and_boundaries(mySQLPurchaseRepository, mySQLCarRepository, purchaseCreateResource):
    purchase = purchases_service.create(mySQLPurchaseRepository, mySQLCarRepository, purchaseCreateResource)
    assert isinstance(purchase, PurchaseReturnResource), f"Purchase is not a PurchaseReturnResource object, but {type(purchase).__name__}"
    assert purchase.car.id == str(purchaseCreateResource.cars_id), f"Purchase cars_id is not {purchaseCreateResource.cars_id}, but {purchase.car.id}"
    assert purchase.date_of_purchase == purchaseCreateResource.date_of_purchase, f"Purchase date_of_purchase is not {purchaseCreateResource.date_of_purchase}, but {purchase.date_of_purchase}"


# INVALID TESTS FOR create
@pytest.mark.parametrize("purchaseCreateResource, errorType, errorMessage", [
    ("", TypeError, "purchase_create_data must be of type PurchaseCreateResource, not str."),
    (None, TypeError, "purchase_create_data must be of type PurchaseCreateResource, not None."),
    ({}, TypeError, "purchase_create_data must be of type PurchaseCreateResource, not dict."),
    ([], TypeError, "purchase_create_data must be of type PurchaseCreateResource, not list."),
    (True, TypeError, "purchase_create_data must be of type PurchaseCreateResource, not bool."),
    (False, TypeError, "purchase_create_data must be of type PurchaseCreateResource, not bool."),
    (False, TypeError, "purchase_create_data must be of type PurchaseCreateResource, not bool."),
])
def test_create_with_invalid_partitions_and_boundaries(mySQLPurchaseRepository, mySQLCarRepository, purchaseCreateResource, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        purchases_service.create(mySQLPurchaseRepository, mySQLCarRepository, purchaseCreateResource)

