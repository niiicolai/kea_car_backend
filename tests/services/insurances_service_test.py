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
        f"Expected insurance id: {valid_insurance_id}, but got: {insurance.id}"

    assert insurance.name == expected_insurance.get("name"), \
        f"Expected insurance name: {expected_insurance.get('name')}, but got: {insurance.name}"

    assert insurance.price == expected_insurance.get("price"), \
        f"Expected insurance price: {expected_insurance.get('price')}, but got: {insurance.price}"

# INVALID TESTS FOR get_insurance_by_id

# VALID TESTS FOR get_all_insurances

# INVALID TESTS FOR get_all_insurances
