import pytest
from datetime import date, timedelta, datetime
from uuid import uuid4, UUID
from pydantic import ValidationError
from app.resources.purchase_resource import PurchaseCreateResource

# VALID and INVALID test data for CarCreateResource

current_date = date.today()

valid_date_of_purchase_data = [
    ("Field Not Set", current_date),
    (None, current_date),
    (date(2023, 1, 1), "No Change"),  # Valid lower boundary
    (date(2023, 1, 2), "No Change"),  # Valid lower boundary
    (current_date - timedelta(days=1), "No Change"),  # Valid upper boundary
    (current_date, "No Change"),  # Valid upper boundary
]

invalid_date_of_purchase_data = [
    (True, "Input should be a valid date"),
    (False, "Input should be a valid date"),
    (20230102, "input_type=int"),
    (datetime.today(), "Datetimes provided to dates should have zero time"),
    (date(2022, 12, 31), "cannot be before 01-01-2023"),
    (current_date + timedelta(days=1), "cannot be in the future"),
]

generated_car_UUID = uuid4()
string_car_UUID = "e620ec3c-625d-4bde-9b77-f7449b6352d5"
string_car_UUID_without_hyphens = "e620ec3c625d4bde9b77f7449b6352d5"
valid_lower_car_UUID_boundary = UUID("00000000-0000-4000-8000-000000000000")
valid_lower_car_UUID_boundary_plus_one = UUID("00000000-0000-4000-8000-000000000001")
valid_upper_car_UUID_boundary_minus_one = UUID("ffffffff-ffff-4fff-bfff-fffffffffffe")
valid_upper_car_UUID_boundary = UUID("ffffffff-ffff-4fff-bfff-ffffffffffff")
invalid_lower_car_UUID_boundary = "00000000-0000-4000-8000-00000000000"
invalid_upper_car_UUID_boundary = "ffffffff-ffff-4fff-bfff-ffffffffffff0"

valid_car_UUID_data = [
    (generated_car_UUID, "No Change"),
    (string_car_UUID, UUID(string_car_UUID)),
    (string_car_UUID_without_hyphens, UUID(string_car_UUID_without_hyphens)),
    (valid_lower_car_UUID_boundary, "No Change"),  # Valid lower boundary
    (valid_lower_car_UUID_boundary_plus_one, "No Change"),  # Valid lower boundary
    (valid_upper_car_UUID_boundary_minus_one, "No Change"),  # Valid upper boundary
    (valid_upper_car_UUID_boundary, "No Change"),  # Valid upper boundary
]

invalid_car_UUID_data = [
    (True, "UUID input should be a string"),
    (10000000000040008000000000000000, "UUID input should be a string"),
    ("Field Not Set", "cars_id\n  Field required"),
    (None, "UUID input should be a string"),
    (invalid_lower_car_UUID_boundary, "Input should be a valid UUID"),  # Invalid lower boundary
    (invalid_upper_car_UUID_boundary, "Input should be a valid UUID"),  # Invalid upper boundary
]


# VALID TESTS FOR PurchaseCreateResource

@pytest.mark.parametrize("valid_date_of_purchase, expected_outcome", valid_date_of_purchase_data)
def test_create_purchase_resource_works_with_valid_date_of_purchase_data(
        valid_date_of_purchase, expected_outcome
):
    if valid_date_of_purchase == "Field Not Set":
        purchase_create_data = PurchaseCreateResource(
            cars_id=generated_car_UUID
        )
    else:
        purchase_create_data = PurchaseCreateResource(
            cars_id=generated_car_UUID,
            date_of_purchase=valid_date_of_purchase
        )

    expected_date_of_purchase = valid_date_of_purchase if expected_outcome == "No Change" else expected_outcome

    assert purchase_create_data.date_of_purchase == expected_date_of_purchase \
        , (f"Date of Purchase: {purchase_create_data.date_of_purchase.strftime('%d-%m-%Y')} "
           f"does not match expected purchase deadline: {expected_date_of_purchase.strftime('%d-%m-%Y')}")


@pytest.mark.parametrize("valid_car_id, expected_outcome", valid_car_UUID_data)
def test_create_purchase_resource_works_with_valid_car_id_data(
        valid_car_id, expected_outcome
):
    purchase_create_data = PurchaseCreateResource(
        cars_id=valid_car_id
    )

    expected_car_id = valid_car_id if expected_outcome == "No Change" else expected_outcome
    assert purchase_create_data.cars_id == expected_car_id, (
        f"Car id: {purchase_create_data.cars_id} does not match "
        f"expected car id: {expected_car_id}"
    )


# INVALID TESTS FOR PurchaseCreateResource

@pytest.mark.parametrize("invalid_date_of_purchase, expected_error_message", invalid_date_of_purchase_data)
def test_create_purchase_resource_doesnt_work_with_invalid_date_of_purchase_data(
        invalid_date_of_purchase, expected_error_message
):
    with pytest.raises(ValidationError, match=expected_error_message):
        PurchaseCreateResource(
            date_of_purchase=invalid_date_of_purchase,
            cars_id=generated_car_UUID
        )


@pytest.mark.parametrize("invalid_car_id, expected_error_message", invalid_car_UUID_data)
def test_create_purchase_resource_doesnt_work_with_invalid_car_id_data(
        invalid_car_id, expected_error_message
):
    if invalid_car_id == "Field Not Set":
        with pytest.raises(ValidationError, match=expected_error_message):
            PurchaseCreateResource()
    else:
        with pytest.raises(ValidationError, match=expected_error_message):
            PurchaseCreateResource(
                cars_id=invalid_car_id
            )
