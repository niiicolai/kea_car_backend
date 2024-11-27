import pytest
from app.services import accessories_service
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.accessory_repositories import AccessoryReturnResource, AccessoryRepository

# Seed data for integration testing
@pytest.fixture
def seed_accessory_data(mySQLAccessoriesRepository):
    """
    Seed the database with accessory data for integration testing.
    """
    accessories = [
        {"id": "0d61b4ee-2c27-400c-9ff5-38123284626c", "name": "Air Conditioning", "price": 99.95},
        {"id": "0f5a86c2-1db5-4486-b5e4-33b92fa3e741", "name": "Alloy Wheels", "price": 99.95},
        {"id": "31a9c926-cd49-4714-9be4-e145b982417e", "name": "Bluetooth Connectivity", "price": 99.95},
    ]
    for accessory in accessories:
        mySQLAccessoriesRepository.add(AccessoryReturnResource(**accessory))  # Assuming `add` is a repository method.
    yield accessories
    for accessory in accessories:
        mySQLAccessoriesRepository.delete(accessory["id"])  # Cleanup after tests.


# TESTS FOR get_by_id
@pytest.mark.parametrize("accessory_id, expected_data", [
    ("1", {"id": "1", "name": "Car Radio", "price": 50.0}),
    ("2", {"id": "2", "name": "GPS System", "price": 100.0}),
    ("3", {"id": "3", "name": "Roof Rack", "price": 200.0}),
])
def test_get_accessory_by_id_valid(mySQLAccessoriesRepository, seed_accessory_data, accessory_id, expected_data):
    accessory = accessories_service.get_by_id(
        repository=mySQLAccessoriesRepository,
        accessory_id=accessory_id,
    )
    assert isinstance(accessory, AccessoryReturnResource), "The returned object is not an AccessoryReturnResource"
    assert accessory.id == expected_data["id"], f"Expected ID {expected_data['id']}, got {accessory.id}"
    assert accessory.name == expected_data["name"], f"Expected name {expected_data['name']}, got {accessory.name}"
    assert accessory.price == expected_data["price"], f"Expected price {expected_data['price']}, got {accessory.price}"


@pytest.mark.parametrize("invalid_accessory_id, expected_error, expected_message", [
    ("999", UnableToFindIdError, "Accessory with ID: 999 does not exist."),
])
def test_get_accessory_by_id_invalid(mySQLAccessoriesRepository, seed_accessory_data, invalid_accessory_id, expected_error, expected_message):
    with pytest.raises(expected_error, match=expected_message):
        accessories_service.get_by_id(
            repository=mySQLAccessoriesRepository,
            accessory_id=invalid_accessory_id,
        )


# TESTS FOR get_all
def test_get_all_accessories_valid(mySQLAccessoriesRepository, seed_accessory_data):
    accessories = accessories_service.get_all(repository=mySQLAccessoriesRepository)

    assert isinstance(accessories, list), "The returned object is not a list"
    assert len(accessories) == len(seed_accessory_data), (
        f"Expected {len(seed_accessory_data)} accessories, got {len(accessories)}"
    )
    for accessory, expected_data in zip(accessories, seed_accessory_data):
        assert isinstance(accessory, AccessoryReturnResource), (
            f"Expected AccessoryReturnResource, got {type(accessory).__name__}"
        )
        assert accessory.id == expected_data["id"], f"Expected ID {expected_data['id']}, got {accessory.id}"
        assert accessory.name == expected_data["name"], f"Expected name {expected_data['name']}, got {accessory.name}"
        assert accessory.price == expected_data["price"], f"Expected price {expected_data['price']}, got {accessory.price}"
