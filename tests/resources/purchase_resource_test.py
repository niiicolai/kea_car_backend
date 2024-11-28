import pytest
import datetime
from pydantic import ValidationError, UUID4
from app.resources.purchase_resource import PurchaseCreateResource


# VALID test data for PurchaseCreateResource
@pytest.mark.parametrize("props", [
    ({"cars_id": "e7bd48c2-f1c4-4e1a-b0fc-dc09f2d8f28a", "date_of_purchase": datetime.date.today()}),
])
def test_PurchaseCreateResource_valid_partitions_and_boundaries(props):
    resource = PurchaseCreateResource(**props)
    
    assert resource.date_of_purchase == props["date_of_purchase"]
    assert str(resource.cars_id) == props["cars_id"]


# INVALID test data for PurchaseCreateResource
@pytest.mark.parametrize("props, errorType, errorMessage", [
    ({}, ValidationError, r"cars_id"),
    ({ "cars_id": None }, ValidationError, r"cars_id"),
    ({ "cars_id": True }, ValidationError, r"cars_id"),
    ({ "cars_id": False }, ValidationError, r"cars_id"),
    ({ "cars_id": {} }, ValidationError, r"cars_id"),
    ({ "cars_id": [] }, ValidationError, r"cars_id"),
    ({ "cars_id": 1 }, ValidationError, r"cars_id"),
    ({ "date_of_purchase": "2024-04-04" }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": None }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": True }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": False }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": {} }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": [] }, ValidationError, r"date_of_purchase"),
    ({ "date_of_purchase": 1 }, ValidationError, r"date_of_purchase"),
])
def test_PurchaseCreateResource_with_invalid_partitions_and_boundaries(props, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        PurchaseCreateResource(**props)

