import pytest
from app.services import insurances_service
from app.exceptions.database_errors import UnableToFindIdError
from app.resources.insurance_resource import InsuranceReturnResource


# VALID TESTS FOR get_insurance_by_id

@pytest.mark.parametrize("valid_insurance_id, expected_insurance", [
    ("37074fac-26da-4e38-9ae6-acbe755359e5",
     {"name": "Earthquake", "price": 29.95}),
    ("3e9a0efb-f1a1-4757-b4c3-985fc856b8d5",
     {"name": "Hauntings", "price": 39.95}),
    ("76b21d38-2103-4464-84f2-c87178e4a30c",
     {"name": "Broken Window", "price": 19.95}),
    ("8456043d-5fb0-49bf-ac2c-51567a32cc87",
     {"name": "Flat Tire", "price": 9.95}),
    ("a80a8bed-e1a2-462f-8a77-9483e757c0f2",
     {"name": "Water Damage", "price": 49.95}),
])
def test_get_insurance_by_id_with_valid_partitions(
        mySQLInsuranceRepository, valid_insurance_id, expected_insurance
):
    insurance = insurances_service.get_by_id(
        repository=mySQLInsuranceRepository,
        insurance_id=valid_insurance_id
    )

    assert isinstance(insurance, InsuranceReturnResource), \
        f"Expected instance of InsuranceReturnResource, but got: {type(insurance).__name__}"

    assert insurance.id == valid_insurance_id, \
        (f"The actual insurance id: '{insurance.id}' does not match "
         f"the expected insurance id: '{valid_insurance_id}'")

    assert insurance.name == expected_insurance.get("name"), \
        (f"The actual insurance name: '{insurance.name}' does not match "
         f"the expected insurance name: '{expected_insurance.get('name')}")

    assert insurance.price == expected_insurance.get("price"), \
        f"The actual insurance price: '{insurance.price}' does not match " \
        f"the expected insurance price: '{expected_insurance.get('price')}'"

# INVALID TESTS FOR get_insurance_by_id

@pytest.mark.parametrize("invalid_insurance_id, expected_error, expected_error_message", [
    (None, TypeError, "insurance_id must be of type str, not NoneType."),
    (1, TypeError, "insurance_id must be of type str, not int."),
    (True, TypeError, "insurance_id must be of type str, not bool."),
    ("invalid_id", UnableToFindIdError, "Insurance with ID: invalid_id does not exist."),
])
def test_get_insurance_by_id_with_invalid_repository_id_partitions(
        mySQLInsuranceRepository, invalid_insurance_id, expected_error, expected_error_message
):
    with pytest.raises(expected_error, match=expected_error_message):
        insurances_service.get_by_id(
            repository=mySQLInsuranceRepository,
            insurance_id=invalid_insurance_id
        )

@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type InsuranceRepository, not NoneType."),
    ("repository", "repository must be of type InsuranceRepository, not str."),
    (True, "repository must be of type InsuranceRepository, not bool."),
    (123, "repository must be of type InsuranceRepository, not int."),
])
def test_get_insurance_by_id_with_invalid_repository_partitions(
        invalid_repository, expected_error_message
):
    valid_insurance_id = "37074fac-26da-4e38-9ae6-acbe755359e5"

    with pytest.raises(TypeError, match=expected_error_message):
        insurances_service.get_by_id(
            repository=invalid_repository,
            insurance_id=valid_insurance_id
        )


def test_get_insurance_by_id_with_invalid_repository_partition_types(
        mySQLAccessoryRepository, mySQLCustomerRepository, mySQLBrandRepository
):
    valid_insurance_id = "37074fac-26da-4e38-9ae6-acbe755359e5"

    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLAccessoryRepository).__name__}."):
        insurances_service.get_by_id(
            repository=mySQLAccessoryRepository,
            insurance_id=valid_insurance_id
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLCustomerRepository).__name__}."):
        insurances_service.get_by_id(
            repository=mySQLCustomerRepository,
            insurance_id=valid_insurance_id
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."):
        insurances_service.get_by_id(
            repository=mySQLBrandRepository,
            insurance_id=valid_insurance_id
        )
# VALID TESTS FOR get_all_insurances

def test_get_all_insurances_with_valid_partitions(mySQLInsuranceRepository):
    insurances = insurances_service.get_all(repository=mySQLInsuranceRepository)

    assert isinstance(insurances, list), \
        (f"Expected instance of list, "
         f"but got: {type(insurances).__name__}")

    expected_amount_of_insurances = 5
    actual_amount_of_insurances = len(insurances)

    assert actual_amount_of_insurances == expected_amount_of_insurances, \
        (f"Expected {expected_amount_of_insurances} insurances, "
         f"but got: {actual_amount_of_insurances}")

    for insurance in insurances:
        assert isinstance(insurance, InsuranceReturnResource), \
            (f"Expected instance of InsuranceReturnResource, "
             f"but got: {type(insurance).__name__}")

@pytest.mark.parametrize("valid_insurances_limit, expected_amount_of_insurances", [
    (-1, 5),
    (0, 5),
    (1, 1),
    (5, 5),
    (None, 5),
    (6, 5)
])
def test_get_all_insurances_with_valid_insurances_limit_partitions(
        mySQLInsuranceRepository, valid_insurances_limit, expected_amount_of_insurances
):
    insurances = insurances_service.get_all(
        repository=mySQLInsuranceRepository,
        insurances_limit=valid_insurances_limit
    )

    assert isinstance(insurances, list), \
        f"Expected instance of list, but got: {type(insurances).__name__}"

    actual_amount_of_insurances = len(insurances)

    assert actual_amount_of_insurances == expected_amount_of_insurances, \
        f"Expected {expected_amount_of_insurances} insurances, but got: {actual_amount_of_insurances}"

    for insurance in insurances:
        assert isinstance(insurance, InsuranceReturnResource), \
            f"Expected instance of InsuranceReturnResource, but got: {type(insurance).__name__}"


# INVALID TESTS FOR get_all_insurances

@pytest.mark.parametrize("invalid_insurances_limit, expected_error_message", [
    ("1", "insurances_limit must be of type int or None, not str."),
    (1.0, "insurances_limit must be of type int or None, not float."),
    (True, "insurances_limit must be of type int or None, not bool."),
    (False, "insurances_limit must be of type int or None, not bool."),
])
def test_get_all_insurances_with_invalid_insurances_limit_partitions(
        mySQLInsuranceRepository, invalid_insurances_limit, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        insurances_service.get_all(
            repository=mySQLInsuranceRepository,
            insurances_limit=invalid_insurances_limit
        )


@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type InsuranceRepository, not NoneType."),
    ("repository", "repository must be of type InsuranceRepository, not str."),
    (True, "repository must be of type InsuranceRepository, not bool."),
    (123, "repository must be of type InsuranceRepository, not int."),
])
def test_get_all_insurance_with_invalid_repository_partitions(
        invalid_repository, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        insurances_service.get_all(repository=invalid_repository)


def test_get_all_insurances_with_invalid_repository_partition_types(
        mySQLAccessoryRepository, mySQLCustomerRepository, mySQLBrandRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLAccessoryRepository).__name__}."):
        insurances_service.get_all(repository=mySQLAccessoryRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLCustomerRepository).__name__}."):
        insurances_service.get_all(repository=mySQLCustomerRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type InsuranceRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."):
        insurances_service.get_all(repository=mySQLBrandRepository)