import pytest
from pydantic import ValidationError, UUID4
from uuid import uuid4
from app.resources.car_resource import CarCreateResource, DAYS_TO_DEADLINE
from datetime import date, timedelta, datetime

# VALID and INVALID test data for CarCreateResource
valid_purchase_deadline_data = [
    ("", date.today() + timedelta(days=DAYS_TO_DEADLINE)),
    (None, date.today() + timedelta(days=DAYS_TO_DEADLINE)),
    (date.today() + timedelta(days=1), date.today() + timedelta(days=1)),
    (date.today() + timedelta(days=DAYS_TO_DEADLINE), date.today() + timedelta(days=DAYS_TO_DEADLINE)),
    (date.today() + timedelta(days=DAYS_TO_DEADLINE-1), date.today() + timedelta(days=DAYS_TO_DEADLINE-1)),
]

invalid_purchase_deadline_data = [
    (date.today() + timedelta(days=DAYS_TO_DEADLINE+1), f"must be within {DAYS_TO_DEADLINE} days from the current date"),
    (date.today(), "must be after the current date"),
    (datetime.today() + timedelta(days=1), "Datetimes provided to dates should have zero time"),
    ("asjdansdjas", "Input should be a valid date"),
    (date.today() + timedelta(days=-1), "must be after the current date"),
]

generated_UUID = uuid4()
valid_accessories_ids_data = [
    ("", []),
    ([], []),
    ([generated_UUID], [generated_UUID]),
    (["e620ec3c-625d-4bde-9b77-f7449b6352d5"],[UUID4("e620ec3c-625d-4bde-9b77-f7449b6352d5")])
]
invalid_accessories_ids_data = [
    (["e620ec3c-625d-4bde-9b77-f7449b6352d5","e620ec3c-625d-4bde-9b77-f7449b6352d5","e620ec3c-625d-4bde-9b77-f7449b6352d5"], "accessories must be unique."),
    (generated_UUID, "Input should be a valid list"),
]

valid_insurance_ids_data = [
    ("", []),
    ([], []),
    ([generated_UUID], [generated_UUID]),
    (["8456043d-5fb0-49bf-ac2c-51567a32cc87"],[UUID4("8456043d-5fb0-49bf-ac2c-51567a32cc87")])
]
invalid_insurance_ids_data = [
    (["8456043d-5fb0-49bf-ac2c-51567a32cc87","8456043d-5fb0-49bf-ac2c-51567a32cc87","8456043d-5fb0-49bf-ac2c-51567a32cc87"], "insurances must be unique."),
    (generated_UUID, "Input should be a valid list"),
]

# VALID TESTS FOR CarCreateResource
def test_create_car_resource_works_with_valid_car_data(valid_car_data):
    car_create_data = CarCreateResource(**valid_car_data)
    assert car_create_data.purchase_deadline == valid_car_data.get("purchase_deadline") \
        , (f"Purchase deadline: {car_create_data.purchase_deadline} does not match "
           f"expected purchase deadline: {valid_car_data.get('purchase_deadline')}")

    assert car_create_data.models_id == valid_car_data.get("models_id") \
        , (f"Model id: {car_create_data.models_id} does not match "
           f"expected model id: {valid_car_data.get('models_id')}")

    assert car_create_data.colors_id == valid_car_data.get("colors_id") \
        , (f"color id: {car_create_data.colors_id} does not match "
           f"expected color id: {valid_car_data.get('colors_id')}")

    assert car_create_data.customers_id == valid_car_data.get("customers_id") \
        , (f"Customer id: {car_create_data.customers_id} does not match "
           f"expected customer id: {valid_car_data.get('customers_id')}")

    assert car_create_data.sales_people_id == valid_car_data.get("sales_people_id") \
        , (f"sales person id: {car_create_data.sales_people_id} does not match "
           f"expected sales person id: {valid_car_data.get('sales_people_id')}")
           
    assert car_create_data.accessory_ids == valid_car_data.get("accessory_ids") \
       , (f"Accessory IDs: {car_create_data.accessory_ids} do not match "
        f"expected accessory IDs: {valid_car_data.get('accessory_ids')}")

    assert car_create_data.insurance_ids == valid_car_data.get("insurance_ids") \
       , (f"Insurance IDs: {car_create_data.insurance_ids} do not match "
        f"expected insurance IDs: {valid_car_data.get('insurance_ids')}")



@pytest.mark.parametrize("valid_purchase_deadline, expected_outcome", valid_purchase_deadline_data)
def test_create_car_resource_works_with_valid_purchase_deadline_data(
        valid_car_data, valid_purchase_deadline, expected_outcome
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("purchase_deadline")
    
    if valid_purchase_deadline == "":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            purchase_deadline=valid_purchase_deadline
            , **valid_car_data
        )
    assert car_create_data.purchase_deadline == expected_outcome \
        , (f"Purchase deadline: {car_create_data.purchase_deadline.strftime('%d-%m-%Y')} "
        f"does not match expected purchase deadline: {expected_outcome.strftime('%d-%m-%Y')}")

@pytest.mark.parametrize("valid_accessories_ids, expected_outcome", valid_accessories_ids_data)
def test_create_car_resource_works_with_valid_accessories_ids_data(
        valid_car_data, valid_accessories_ids, expected_outcome
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("accessory_ids")
    
    if valid_accessories_ids == "":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            accessory_ids=valid_accessories_ids
            , **valid_car_data
        )
    assert car_create_data.accessory_ids == expected_outcome \
        , (f"Accessory IDs: {car_create_data.accessory_ids} do not match "
        f"expected accessory IDs: {expected_outcome}")
        
@pytest.mark.parametrize("valid_insurance_ids, expected_outcome", valid_insurance_ids_data)
def test_create_car_resource_works_with_valid_insurance_ids_data(
        valid_car_data, valid_insurance_ids, expected_outcome
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("insurance_ids")
    
    if valid_insurance_ids == "":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            insurance_ids=valid_insurance_ids
            , **valid_car_data
        )
    assert car_create_data.insurance_ids == expected_outcome \
        , (f"Insurance IDs: {car_create_data.insurance_ids} do not match "
        f"expected insurance IDs: {expected_outcome}")

# INVALID TESTS FOR CarCreateResource

@pytest.mark.parametrize("invalid_purchase_deadline, expected_error_message", invalid_purchase_deadline_data)
def test_create_car_resource_doesnt_work_with_invalid_purchase_deadline_data(
        valid_car_data, invalid_purchase_deadline, expected_error_message
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("purchase_deadline")
    
    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            purchase_deadline=invalid_purchase_deadline
            , **valid_car_data
        )
        
@pytest.mark.parametrize("invalid_accessories_ids, expected_error_message", invalid_accessories_ids_data)
def test_create_car_resource_doesnt_work_with_invalid_accessories_ids_data(
        valid_car_data, invalid_accessories_ids, expected_error_message
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("accessory_ids")
    
    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            accessory_ids=invalid_accessories_ids
            , **valid_car_data
        )
        
@pytest.mark.parametrize("invalid_insurance_ids, expected_error_message", invalid_insurance_ids_data)
def test_create_car_resource_doesnt_work_with_invalid_insurance_ids_data(
        valid_car_data, invalid_insurance_ids, expected_error_message
):
    valid_car_data = valid_car_data.copy()
    valid_car_data.pop("insurance_ids")
    
    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            insurance_ids=invalid_insurance_ids
            , **valid_car_data
        )
        
  
