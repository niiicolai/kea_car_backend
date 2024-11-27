import pytest
from app.services import insurances_service
from app.exceptions.database_errors import UnableToFindIdError
from app.resources.insurance_resource import InsuranceReturnResource

# Mock data for testing
valid_insurance_data = [
    {"id": "37074fac-26da-4e38-9ae6-acbe755359e5", "name": "Earthquake", "price": 29.95},
    {"id": "3e9a0efb-f1a1-4757-b4c3-985fc856b8d5", "name": "Hauntings", "price": 39.95},
    {"id": "76b21d38-2103-4464-84f2-c87178e4a30c", "name": "Broken Window", "price": 19.95},
]

# Fixtures for repository and valid/invalid data
@pytest.fixture
def valid_insurance_repository(mocker):
    """
    Mocked InsuranceRepository that returns valid data for get_all and get_by_id.
    """
    repository = mocker.Mock()
    repository.get_all.return_value = [
        InsuranceReturnResource(**data) for data in valid_insurance_data
    ]
    repository.get_by_id.side_effect = lambda insurance_id: (
        InsuranceReturnResource(**next(item for item in valid_insurance_data if item["id"] == insurance_id))
        if any(item["id"] == insurance_id for item in valid_insurance_data)
        else None
    )
    return repository


@pytest.fixture
def invalid_repository():
    """
    Invalid repository for testing type errors.
    """
    return None


# TESTS FOR get_by_id

@pytest.mark.parametrize("insurance_id, expected_data", [
    ("1", valid_insurance_data[0]),
    ("2", valid_insurance_data[1]),
    ("3", valid_insurance_data[2]),
])
def test_get_insurance_by_id_valid(valid_insurance_repository, insurance_id, expected_data):
    insurance = insurances_service.get_by_id(
        repository=valid_insurance_repository,
        insurance_id=insurance_id,
    )
    assert isinstance(insurance, InsuranceReturnResource), "The returned object is not an InsuranceReturnResource"
    assert insurance.id == expected_data["id"], f"Expected ID {expected_data['id']}, got {insurance.id}"
    assert insurance.name == expected_data["name"], f"Expected name {expected_data['name']}, got {insurance.name}"
    assert insurance.price == expected_data["price"], f"Expected price {expected_data['price']}, got {insurance.price}"


@pytest.mark.parametrize("invalid_insurance_id, expected_error, expected_message", [
    (None, TypeError, "insurance_id must be of type str, not NoneType."),
    (123, TypeError, "insurance_id must be of type str, not int."),
    ("999", UnableToFindIdError, "Insurance with ID: 999 does not exist."),
])
def test_get_insurance_by_id_invalid(valid_insurance_repository, invalid_insurance_id, expected_error, expected_message):
    with pytest.raises(expected_error, match=expected_message):
        insurances_service.get_by_id(
            repository=valid_insurance_repository,
            insurance_id=invalid_insurance_id,
        )


@pytest.mark.parametrize("invalid_repository", [
    None, 123, "invalid_repository",
])
def test_get_insurance_by_id_invalid_repository(invalid_repository):
    with pytest.raises(TypeError, match="repository must be of type InsuranceRepository"):
        insurances_service.get_by_id(
            repository=invalid_repository,
            insurance_id="1",
        )


# TESTS FOR get_all

def test_get_all_insurances_valid(valid_insurance_repository):
    insurances = insurances_service.get_all(repository=valid_insurance_repository)

    assert isinstance(insurances, list), "The returned object is not a list"
    assert len(insurances) == len(valid_insurance_data), (
        f"Expected {len(valid_insurance_data)} insurances, got {len(insurances)}"
    )
    for insurance, expected_data in zip(insurances, valid_insurance_data):
        assert isinstance(insurance, InsuranceReturnResource), (
            f"Expected InsuranceReturnResource, got {type(insurance).__name__}"
        )
        assert insurance.id == expected_data["id"], f"Expected ID {expected_data['id']}, got {insurance.id}"
        assert insurance.name == expected_data["name"], f"Expected name {expected_data['name']}, got {insurance.name}"
        assert insurance.price == expected_data["price"], f"Expected price {expected_data['price']}, got {insurance.price}"


@pytest.mark.parametrize("insurances_limit, expected_count", [
    (None, len(valid_insurance_data)),
    (2, 2),
    (0, 0),
])
def test_get_all_insurances_with_limit(valid_insurance_repository, insurances_limit, expected_count):
    insurances = insurances_service.get_all(
        repository=valid_insurance_repository,
        insurances_limit=insurances_limit,
    )
    assert len(insurances) == expected_count, f"Expected {expected_count} insurances, got {len(insurances)}"


@pytest.mark.parametrize("invalid_insurances_limit, expected_error_message", [
    ("5", "insurances_limit must be of type int or None, not str."),
    (1.5, "insurances_limit must be of type int or None, not float."),
    (True, "insurances_limit must be of type int or None, not bool."),
])
def test_get_all_insurances_invalid_limit(valid_insurance_repository, invalid_insurances_limit, expected_error_message):
    with pytest.raises(TypeError, match=expected_error_message):
        insurances_service.get_all(
            repository=valid_insurance_repository,
            insurances_limit=invalid_insurances_limit,
        )


@pytest.mark.parametrize("invalid_repository", [
    None, 123, "invalid_repository",
])
def test_get_all_insurances_invalid_repository(invalid_repository):
    with pytest.raises(TypeError, match="repository must be of type InsuranceRepository"):
        insurances_service.get_all(
            repository=invalid_repository,
        )
