import pytest
from app.services import accessories_service
from app.exceptions.database_errors import UnableToFindIdError
from app.resources.accessory_resource import AccessoryReturnResource

# VALID TESTS FOR get_accessory_by_id

@pytest.mark.parametrize("expected_accessory", [
    accessory_radio,
    accessory_gps,
    accessory_spoiler,
    accessory_floor_mats,
    accessory_roof_rack,
])
def test_get_by_id_with_valid_partitions(mySQLAccessoryRepository, expected_accessory):
    expected_accessory_data, accessory_fields, expected_accessory_id = prepare_accessory_data(expected_accessory)

    accessory = accessory_service.get_by_id(
        repository=mySQLAccessoryRepository,
        accessory_id=expected_accessory_id
    )

    # Assert the returned object is of the correct type
    assert isinstance(accessory, AccessoryReturnResource), \
        (f"Accessory is not of type AccessoryReturnResource, "
         f"but {type(accessory).__name__}")

    # Assert the returned object's ID matches the expected ID
    assert accessory.id == expected_accessory_id, \
        (f"Accessory ID {accessory.id} does not match "
         f"expected accessory ID {expected_accessory_id}")

    # Assert all fields match the expected data
    for field in accessory_fields:
        assert getattr(accessory, field) == expected_accessory_data.get(field), \
            (f"Accessory {field}: {getattr(accessory, field)} does not match "
             f"the expected data: {expected_accessory_data.get(field)}")

# INVALID TESTS FOR get_accessory_by_id

@pytest.mark.parametrize("invalid_accessory_id, expected_error, expected_error_message", [
    (None, TypeError, "accessory_id must be of type str, not NoneType."),
    (True, TypeError, "accessory_id must be of type str, not bool."),
    (12345, TypeError, "accessory_id must be of type str, not int."),
    ("non-existent-id", UnableToFindIdError, "Accessory with ID: non-existent-id does not exist."),
])
def test_get_by_id_with_invalid_accessory_id_partitions(
        mySQLAccessoryRepository, invalid_accessory_id, expected_error, expected_error_message):
    with pytest.raises(expected_error, match=expected_error_message):
        accessory_service.get_by_id(
            repository=mySQLAccessoryRepository,
            accessory_id=invalid_accessory_id
        )

# VALID TESTS FOR get_all_accessories

@pytest.mark.parametrize("valid_accessory_limit, expecting_accessory_amount", [
    (-1, 5),
    (None, 5),
    (0, 5),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 5),
])
def test_get_all_accessories_with_valid_limit_values_partitions(
        mySQLAccessoryRepository, valid_accessory_limit, expecting_accessory_amount
):
    accessories = accessory_service.get_all(
        repository=mySQLAccessoryRepository,
        accessory_limit=valid_accessory_limit
    )

    # Assert the returned object is a list of AccessoryReturnResource objects
    assert isinstance(accessories, list) and all(isinstance(accessory, AccessoryReturnResource) for accessory in accessories), \
        f"Accessories are not a list of AccessoryReturnResource objects, but {type(accessories).__name__}"

    # Assert the returned list has the expected number of items
    assert len(accessories) == expecting_accessory_amount, \
        f"There should be {expecting_accessory_amount} accessories, not '{len(accessories)}'"

# INVALID TESTS FOR get_all_accessories

@pytest.mark.parametrize("invalid_accessory_limit, expecting_error_message", [
    ("1", "accessory_limit must be of type int or None, not str."),
    (1.0, "accessory_limit must be of type int or None, not float."),
    (True, "accessory_limit must be of type int or None, not bool."),
])
def test_get_all_accessories_with_invalid_limit_values_partitions(
        mySQLAccessoryRepository, invalid_accessory_limit, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        accessory_service.get_all(
            repository=mySQLAccessoryRepository,
            accessory_limit=invalid_accessory_limit
        )
