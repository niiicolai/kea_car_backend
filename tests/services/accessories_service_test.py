from pickle import FALSE

import pytest
from app.services import accessories_service
from app.exceptions.database_errors import UnableToFindIdError
from app.resources.accessory_resource import AccessoryReturnResource


# VALID TESTS FOR get_accessory_by_id

@pytest.mark.parametrize(
    "valid_accessory_id, expected_accessory", [
        ("0d61b4ee-2c27-400c-9ff5-38123284626c", {
            "id": "0d61b4ee-2c27-400c-9ff5-38123284626c",
            "name": "Air Conditioning",
            "price": 99.95,
        }),
        ("0f5a86c2-1db5-4486-b5e4-33b92fa3e741", {
            "id": "0f5a86c2-1db5-4486-b5e4-33b92fa3e741",
            "name": "Alloy Wheels",
            "price": 99.95,
        }),
        ("31a9c926-cd49-4714-9be4-e145b982417e", {
            "id": "31a9c926-cd49-4714-9be4-e145b982417e",
            "name": "Bluetooth Connectivity",
            "price": 99.95,
        }),
        ("5b55aa29-8eb8-4f83-8110-f2bb50e7d08c", {
            "id": "5b55aa29-8eb8-4f83-8110-f2bb50e7d08c",
            "name": "Sport Package",
            "price": 99.95,
        })
    ]
)
def test_get_accessory_by_id_with_valid_partitions(
        mySQLAccessoryRepository, valid_accessory_id, expected_accessory
):
    accessory = accessories_service.get_by_id(
        repository=mySQLAccessoryRepository,
        accessory_id=valid_accessory_id
    )

    assert isinstance(accessory, AccessoryReturnResource), \
        f"Expected instance of AccessoryReturnResource, but got: {type(accessory).__name__}"

    assert accessory.id == expected_accessory.get("id"), \
        f"Expected accessory id: {expected_accessory.get('id')}, but got: {accessory.id}"

    assert accessory.name == expected_accessory.get("name"), \
        f"Expected accessory name: {expected_accessory.get('name')}, but got: {accessory.name}"

    assert accessory.price == expected_accessory.get("price"), \
        f"Expected accessory price: {expected_accessory.get('price')}, but got: {accessory.price}"


# INVALID TESTS FOR get_accessory_by_id

@pytest.mark.parametrize("invalid_accessory_id, expected_error, expected_error_message", [
    (None, TypeError, "accessory_id must be of type str, not NoneType."),
    (1, TypeError, "accessory_id must be of type str, not int."),
    (True, TypeError, "accessory_id must be of type str, not bool."),
    ("invalid_id", UnableToFindIdError, "Accessory with ID: invalid_id does not exist."),
])
def test_get_accessory_by_id_with_invalid_accessory_id_partitions(
        mySQLAccessoryRepository, invalid_accessory_id, expected_error, expected_error_message
):
    with pytest.raises(expected_error, match=expected_error_message):
        accessories_service.get_by_id(
            repository=mySQLAccessoryRepository,
            accessory_id=invalid_accessory_id
        )


@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type AccessoryRepository, not NoneType."),
    ("repository", "repository must be of type AccessoryRepository, not str."),
    (True, "repository must be of type AccessoryRepository, not bool."),
    (123, "repository must be of type AccessoryRepository, not int."),
])
def test_get_accessory_by_id_with_invalid_repository_partitions(
        invalid_repository, expected_error_message
):
    valid_accessory_id = "0d61b4ee-2c27-400c-9ff5-38123284626c"

    with pytest.raises(TypeError, match=expected_error_message):
        accessories_service.get_by_id(
            repository=invalid_repository,
            accessory_id=valid_accessory_id
        )


def test_get_accessory_by_id_with_invalid_repository_partition_types(
        mySQLInsuranceRepository, mySQLCustomerRepository, mySQLBrandRepository
):
    valid_accessory_id = "0d61b4ee-2c27-400c-9ff5-38123284626c"

    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLInsuranceRepository).__name__}."):
        accessories_service.get_by_id(
            repository=mySQLInsuranceRepository,
            accessory_id=valid_accessory_id
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLCustomerRepository).__name__}."):
        accessories_service.get_by_id(
            repository=mySQLCustomerRepository,
            accessory_id=valid_accessory_id
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLBrandRepository).__name__}."):
        accessories_service.get_by_id(
            repository=mySQLBrandRepository,
            accessory_id=valid_accessory_id
        )


# VALID TESTS FOR get_all_accessories

def test_get_all_accessories_with_valid_partitions(mySQLAccessoryRepository):
    accessories = accessories_service.get_all(repository=mySQLAccessoryRepository)

    assert isinstance(accessories, list), \
        f"Expected instance of list, but got: {type(accessories).__name__}"

    expected_amount_of_accessories = 20
    actual_amount_of_accessories = len(accessories)

    assert actual_amount_of_accessories == expected_amount_of_accessories, \
        f"Expected {expected_amount_of_accessories} accessories, but got: {actual_amount_of_accessories}"

    for accessory in accessories:
        assert isinstance(accessory, AccessoryReturnResource), \
            f"Expected instance of AccessoryReturnResource, but got: {type(accessory).__name__}"


@pytest.mark.parametrize("valid_accessory_limit, expected_amount_of_accessories", [
    (-1, 20),
    (0, 20),
    (None, 20),
    (1, 1),
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (21, 20),
])
def test_get_all_accessories_with_valid_accessory_limit_partitions(
        mySQLAccessoryRepository, valid_accessory_limit, expected_amount_of_accessories
):
    accessories = accessories_service.get_all(
        repository=mySQLAccessoryRepository,
        accessory_limit=valid_accessory_limit
    )

    assert isinstance(accessories, list), \
        f"Expected instance of list, but got: {type(accessories).__name__}"

    actual_amount_of_accessories = len(accessories)

    assert actual_amount_of_accessories == expected_amount_of_accessories, \
        f"Expected {expected_amount_of_accessories} accessories, but got: {actual_amount_of_accessories}"

    for accessory in accessories:
        assert isinstance(accessory, AccessoryReturnResource), \
            f"Expected instance of AccessoryReturnResource, but got: {type(accessory).__name__}"


# INVALID TESTS FOR get_all_accessories

@pytest.mark.parametrize("invalid_accessory_limit, expected_error_message", [
    ("1", "accessory_limit must be of type int or None, not str."),
    (1.0, "accessory_limit must be of type int or None, not float."),
    (True, "accessory_limit must be of type int or None, not bool."),
    (False, "accessory_limit must be of type int or None, not bool."),
])
def test_get_all_accessories_with_invalid_accessory_limit_partitions(
        mySQLAccessoryRepository, invalid_accessory_limit, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        accessories_service.get_all(
            repository=mySQLAccessoryRepository,
            accessory_limit=invalid_accessory_limit
        )


@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type AccessoryRepository, not NoneType."),
    ("repository", "repository must be of type AccessoryRepository, not str."),
    (True, "repository must be of type AccessoryRepository, not bool."),
    (123, "repository must be of type AccessoryRepository, not int."),
])
def test_get_all_accessories_with_invalid_repository_partitions(
        invalid_repository, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        accessories_service.get_all(repository=invalid_repository)


def test_get_all_accessories_with_invalid_repository_partition_types(
        mySQLInsuranceRepository, mySQLCustomerRepository, mySQLBrandRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLInsuranceRepository).__name__}."):
        accessories_service.get_all(repository=mySQLInsuranceRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLCustomerRepository).__name__}."):
        accessories_service.get_all(repository=mySQLCustomerRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type AccessoryRepository, not {type(mySQLBrandRepository).__name__}."):
        accessories_service.get_all(repository=mySQLBrandRepository)
