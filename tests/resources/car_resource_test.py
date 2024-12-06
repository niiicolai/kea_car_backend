import pytest
from pydantic import ValidationError, UUID4
from uuid import uuid4, UUID
from app.resources.car_resource import CarCreateResource, DAYS_TO_DEADLINE
from datetime import date, timedelta, datetime

# VALID and INVALID test data for CarCreateResource

valid_purchase_deadline_data = [
    ("Field Not Set", date.today() + timedelta(days=DAYS_TO_DEADLINE)),
    (None, date.today() + timedelta(days=DAYS_TO_DEADLINE)),
    (date.today() + timedelta(days=DAYS_TO_DEADLINE / 2), "No Change"),
    (date.today() + timedelta(days=1), "No Change"),  # Valid lower boundary
    (date.today() + timedelta(days=2), "No Change"),  # Valid lower boundary
    (date.today() + timedelta(days=DAYS_TO_DEADLINE), "No Change"),  # Valid upper boundary
    (date.today() + timedelta(days=DAYS_TO_DEADLINE - 1), "No Change"),  # Valid upper boundary
]

invalid_purchase_deadline_data = [
    (date.today(), "must be after the current date"),
    (True, "Input should be a valid date"),
    (20250101, "input_type=int"),
    (datetime.today() + timedelta(days=1), "Datetimes provided to dates should have zero time"),
    (date.today() + timedelta(days=-1), "must not be in the past"),
    (date.today() + timedelta(days=DAYS_TO_DEADLINE + 1),
     f"must be within {DAYS_TO_DEADLINE} days from the current date"),
]

generated_UUID = uuid4()
string_UUID = "e620ec3c-625d-4bde-9b77-f7449b6352d5"
string_UUID_without_hyphens = "e620ec3c625d4bde9b77f7449b6352d5"
valid_lower_boundary_UUID = UUID("00000000-0000-4000-8000-000000000000")
valid_lower_boundary_UUID_plus_one = UUID("00000000-0000-4000-8000-000000000001")
valid_upper_boundary_UUID_minus_one = UUID("ffffffff-ffff-4fff-bfff-fffffffffffe")
valid_upper_boundary_UUID = UUID("ffffffff-ffff-4fff-bfff-ffffffffffff")
invalid_lower_boundary_UUID = "00000000-0000-4000-8000-00000000000"
invalid_upper_boundary_UUID = "ffffffff-ffff-4fff-bfff-ffffffffffff0"

valid_UUID_data = [
    (uuid4(), "No Change"),
    (string_UUID, UUID(string_UUID)),
    (string_UUID_without_hyphens, UUID(string_UUID_without_hyphens)),
    (valid_lower_boundary_UUID, "No Change"),  # Valid lower boundary
    (valid_lower_boundary_UUID_plus_one, "No Change"),  # Valid lower boundary
    (valid_upper_boundary_UUID_minus_one, "No Change"),  # Valid upper boundary
    (valid_upper_boundary_UUID, "No Change"),  # Valid upper boundary
]

invalid_UUID_data = [
    (True, "UUID input should be a string"),
    (10000000000040008000000000000000, "UUID input should be a string"),
    (None, "UUID input should be a string"),
    (invalid_lower_boundary_UUID, "Input should be a valid UUID"),  # Invalid lower boundary
    (invalid_upper_boundary_UUID, "Input should be a valid UUID"),  # Invalid upper boundary
]

valid_accessories_ids_data = [
    ("Field Not Set", []),
    ([uuid4(), uuid4(), uuid4()], "No Change"),
    ([string_UUID], [UUID4(string_UUID)]),
    ([string_UUID_without_hyphens], [UUID4(string_UUID_without_hyphens)]),
    ([], "No Change"),  # Valid lower boundary
    ([generated_UUID], "No Change"),  # Valid lower boundary
    ([uuid4() for _ in range(9)], "No Change"),  # Valid upper boundary
    ([uuid4() for _ in range(10)], "No Change"),  # Valid upper boundary
]

invalid_accessories_ids_data = [
    (None, "Input should be a valid list"),
    ([None], "UUID input should be a string, bytes or UUID object"),
    (True, "Input should be a valid list"),
    ([True], "UUID input should be a string, bytes or UUID object"),
    (10000000000040008000000000000000, "Input should be a valid list"),
    ([10000000000040008000000000000000], "UUID input should be a string, bytes or UUID object"),
    ([generated_UUID, uuid4(), generated_UUID], "accessories must be unique."),
    (generated_UUID, "Input should be a valid list"),
    ([uuid4() for _ in range(11)], "Too many accessories by 1, the maximum amount of accessories is 10.") # Invalid upper boundary
]

valid_insurance_ids_data = [
    ("Field Not Set", []),
    ([], "No Change"),
    ([generated_UUID], "No Change"),
    ([uuid4(), uuid4(), uuid4()], "No Change"),
    ([string_UUID], [UUID4(string_UUID)]),
    ([string_UUID_without_hyphens], [UUID4(string_UUID_without_hyphens)]),
    ([valid_lower_boundary_UUID], "No Change"),  # Valid lower boundary
    ([valid_lower_boundary_UUID_plus_one], "No Change"),  # Valid lower boundary
    ([valid_upper_boundary_UUID_minus_one], "No Change"),  # Valid upper boundary
    ([valid_upper_boundary_UUID], "No Change"),  # Valid upper boundary
]

invalid_insurance_ids_data = [
    (None, "Input should be a valid list"),
    ([None], "UUID input should be a string, bytes or UUID object"),
    (True, "Input should be a valid list"),
    ([True], "UUID input should be a string, bytes or UUID object"),
    (10000000000040008000000000000000, "Input should be a valid list"),
    ([10000000000040008000000000000000], "UUID input should be a string, bytes or UUID object"),
    ([generated_UUID, uuid4(), generated_UUID], "insurances must be unique."),
    (generated_UUID, "Input should be a valid list"),
    ([invalid_lower_boundary_UUID], "Input should be a valid UUID"),  # Invalid lower boundary
    ([invalid_upper_boundary_UUID], "Input should be a valid UUID"),  # Invalid upper boundary
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
    valid_car_data.pop("purchase_deadline")

    if valid_purchase_deadline == "Field Not Set":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            purchase_deadline=valid_purchase_deadline
            , **valid_car_data
        )

    expected_purchase_deadline = valid_purchase_deadline if expected_outcome == "No Change" else expected_outcome

    assert car_create_data.purchase_deadline == expected_purchase_deadline \
        , (f"Purchase deadline: {car_create_data.purchase_deadline.strftime('%d-%m-%Y')} "
           f"does not match expected purchase deadline: {expected_purchase_deadline.strftime('%d-%m-%Y')}")


@pytest.mark.parametrize("valid_model_id, expected_outcome", valid_UUID_data)
def test_create_car_resource_works_with_valid_model_id_data(
        valid_car_data, valid_model_id, expected_outcome
):
    valid_car_data.pop("models_id")

    car_create_data = CarCreateResource(
        models_id=valid_model_id
        , **valid_car_data
    )

    expected_model_id = valid_model_id if expected_outcome == "No Change" else expected_outcome
    assert car_create_data.models_id == expected_model_id, (
        f"Model id: {car_create_data.models_id} does not match "
        f"expected model id: {expected_model_id}"
    )


@pytest.mark.parametrize("valid_color_id, expected_outcome", valid_UUID_data)
def test_create_car_resource_works_with_valid_color_id_data(
        valid_car_data, valid_color_id, expected_outcome
):
    valid_car_data.pop("colors_id")

    car_create_data = CarCreateResource(
        colors_id=valid_color_id
        , **valid_car_data
    )

    expected_color_id = valid_color_id if expected_outcome == "No Change" else expected_outcome
    assert car_create_data.colors_id == expected_color_id, (
        f"Color id: {car_create_data.colors_id} does not match "
        f"expected color id: {expected_color_id}"
    )


@pytest.mark.parametrize("valid_customer_id, expected_outcome", valid_UUID_data)
def test_create_car_resource_works_with_valid_customer_id_data(
        valid_car_data, valid_customer_id, expected_outcome
):
    valid_car_data.pop("customers_id")

    car_create_data = CarCreateResource(
        customers_id=valid_customer_id
        , **valid_car_data
    )

    expected_customer_id = valid_customer_id if expected_outcome == "No Change" else expected_outcome
    assert car_create_data.customers_id == expected_customer_id, (
        f"Customer id: {car_create_data.customers_id} does not match "
        f"expected customer id: {expected_customer_id}"
    )


@pytest.mark.parametrize("valid_sales_person_id, expected_outcome", valid_UUID_data)
def test_create_car_resource_works_with_valid_sales_person_id_data(
        valid_car_data, valid_sales_person_id, expected_outcome
):
    valid_car_data.pop("sales_people_id")

    car_create_data = CarCreateResource(
        sales_people_id=valid_sales_person_id
        , **valid_car_data
    )

    expected_sales_person_id = valid_sales_person_id if expected_outcome == "No Change" else expected_outcome
    assert car_create_data.sales_people_id == expected_sales_person_id, (
        f"Sales person id: {car_create_data.sales_people_id} does not match "
        f"expected sales person id: {expected_sales_person_id}"
    )


@pytest.mark.parametrize("valid_accessory_ids, expected_outcome", valid_accessories_ids_data)
def test_create_car_resource_works_with_valid_accessories_ids_data(
        valid_car_data, valid_accessory_ids, expected_outcome
):
    valid_car_data.pop("accessory_ids")

    if valid_accessory_ids == "Field Not Set":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            accessory_ids=valid_accessory_ids
            , **valid_car_data
        )
    expected_accessory_ids = valid_accessory_ids if expected_outcome == "No Change" else expected_outcome

    assert car_create_data.accessory_ids == expected_accessory_ids \
        , (f"Accessory IDs: {car_create_data.accessory_ids} do not match "
           f"expected accessory IDs: {expected_accessory_ids}")


@pytest.mark.parametrize("valid_insurance_ids, expected_outcome", valid_insurance_ids_data)
def test_create_car_resource_works_with_valid_insurance_ids_data(
        valid_car_data, valid_insurance_ids, expected_outcome
):
    valid_car_data.pop("insurance_ids")

    if valid_insurance_ids == "Field Not Set":
        car_create_data = CarCreateResource(
            **valid_car_data
        )
    else:
        car_create_data = CarCreateResource(
            insurance_ids=valid_insurance_ids
            , **valid_car_data
        )

    expected_insurance_ids = valid_insurance_ids if expected_outcome == "No Change" else expected_outcome

    assert car_create_data.insurance_ids == expected_insurance_ids \
        , (f"Insurance IDs: {car_create_data.insurance_ids} do not match "
           f"expected insurance IDs: {expected_insurance_ids}")


# INVALID TESTS FOR CarCreateResource

@pytest.mark.parametrize("missing_field",
                         ["all_fields", "models_id", "colors_id", "customers_id", "sales_people_id"])
def test_create_sales_person_resource_does_not_work_without_setting_model_id_color_id_customer_id_sales_person_id_fields(
        valid_car_data, missing_field
):
    if missing_field == "all_fields":
        with pytest.raises(ValidationError, match="Field required"):
            CarCreateResource()
    else:
        valid_car_data.pop(missing_field)
        with pytest.raises(ValidationError, match=f"{missing_field}\n  Field required"):
            CarCreateResource(
                **valid_car_data
            ), f"{missing_field} should be required"


@pytest.mark.parametrize("invalid_purchase_deadline, expected_error_message", invalid_purchase_deadline_data)
def test_create_car_resource_doesnt_work_with_invalid_purchase_deadline_data(
        valid_car_data, invalid_purchase_deadline, expected_error_message
):
    valid_car_data.pop("purchase_deadline")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            purchase_deadline=invalid_purchase_deadline
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_model_id, expected_error_message", invalid_UUID_data)
def test_create_car_resource_doesnt_work_with_invalid_model_id_data(
        valid_car_data, invalid_model_id, expected_error_message
):
    valid_car_data.pop("models_id")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            models_id=invalid_model_id
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_color_id, expected_error_message", invalid_UUID_data)
def test_create_car_resource_doesnt_work_with_invalid_color_id_data(
        valid_car_data, invalid_color_id, expected_error_message
):
    valid_car_data.pop("colors_id")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            colors_id=invalid_color_id
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_customer_id, expected_error_message", invalid_UUID_data)
def test_create_car_resource_doesnt_work_with_invalid_customer_id_data(
        valid_car_data, invalid_customer_id, expected_error_message
):
    valid_car_data.pop("customers_id")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            customers_id=invalid_customer_id
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_sales_person_id, expected_error_message", invalid_UUID_data)
def test_create_car_resource_doesnt_work_with_invalid_sales_person_id_data(
        valid_car_data, invalid_sales_person_id, expected_error_message
):
    valid_car_data.pop("sales_people_id")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            sales_people_id=invalid_sales_person_id
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_accessory_ids, expected_error_message", invalid_accessories_ids_data)
def test_create_car_resource_doesnt_work_with_invalid_accessory_ids_data(
        valid_car_data, invalid_accessory_ids, expected_error_message
):
    valid_car_data.pop("accessory_ids")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            accessory_ids=invalid_accessory_ids
            , **valid_car_data
        )


@pytest.mark.parametrize("invalid_insurance_ids, expected_error_message", invalid_insurance_ids_data)
def test_create_car_resource_doesnt_work_with_invalid_insurance_ids_data(
        valid_car_data, invalid_insurance_ids, expected_error_message
):
    valid_car_data.pop("insurance_ids")

    with pytest.raises(ValidationError, match=expected_error_message):
        CarCreateResource(
            insurance_ids=invalid_insurance_ids
            , **valid_car_data
        )
