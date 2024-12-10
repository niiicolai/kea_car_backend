import pytest
from app.services import brands_service
from app.exceptions.database_errors import UnableToFindIdError
from app.resources.brand_resource import BrandReturnResource

valid_brand_test_data = [
    {
        "name": "Mercedes",
        "logo_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/Mercedes-logo.png",
        "id": "83e36635-548d-491a-9e5f-3fafaab02ba0"
    },
    {
        "name": "Ford",
        "logo_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/Ford-logo.png",
        "id": "8bb880b8-e336-4039-ad86-2f758539e454"
    },
    {
        "name": "Skoda",
        "logo_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/Skoda-logo.png",
        "id": "fadeb491-9cde-4534-b855-b1ada31e2b47"
    },
    {
        "name": "BMW",
        "logo_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/bmw-logo.png",
        "id": "feb2efdb-93ee-4f45-88b1-5e4086c00334"
    },
    {
        "name": "Audi",
        "logo_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/Audi-logo.png",
        "id": "fff14a06-dc2a-447d-a707-9c03fe00c7a0"
    }
]


# VALID TESTS FOR get_brand_by_id
@pytest.mark.parametrize("brand_data", valid_brand_test_data)
def test_get_brand_by_id_valid(mySQLBrandRepository, brand_data):
    valid_brand_id = brand_data.get("id")
    brand = brands_service.get_by_id(repository=mySQLBrandRepository, brand_id=valid_brand_id)
    assert isinstance(brand, BrandReturnResource), \
        (f"The car is not a CarReturnResource instance, "
         f"but a {type(brand).__name__}")

    assert brand.id == valid_brand_id, (
        f"The actual brand id '{brand.id}' is not the same as "
        f"the expected brand id {valid_brand_id}"
    )

    assert brand.name == brand_data.get("name"), (
        f"The actual brand name '{brand.name}' is not the same as "
        f"the expected brand name {brand_data.get('name')}"
    )

    assert brand.logo_url == brand_data.get("logo_url"), (
        f"The actual brand logo url '{brand.logo_url}' is not the same as "
        f"the expected brand logo url {brand_data.get('logo_url')}"
    )


# INVALID TESTS FOR get_brand_by_id
@pytest.mark.parametrize("invalid_id, expected_error, expecting_error_message", [
    (None, TypeError, "brand_id must be of type str, not NoneType."),
    (123, TypeError, "brand_id must be of type str, not int."),
    (True, TypeError, "brand_id must be of type str, not bool."),
    ("unknown-id", UnableToFindIdError, "Accessory with ID: unknown-id does not exist."),
])
def test_get_brand_by_id_invalid_id(mySQLBrandRepository, invalid_id, expected_error, expecting_error_message):
    with pytest.raises(expected_error, match=expecting_error_message):
        brands_service.get_by_id(repository=mySQLBrandRepository, brand_id=invalid_id)


@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type BrandRepository, not NoneType."),
    (123, "repository must be of type BrandRepository, not int."),
    (True, "repository must be of type BrandRepository, not bool."),
    ("repository", "repository must be of type BrandRepository, not str."),
    (object(), "repository must be of type BrandRepository, not object."),
])
def test_get_brand_by_id_with_invalid_repository_type(
        invalid_repository, expected_error_message
):
    valid_brand_id = valid_brand_test_data[0]["id"]
    with pytest.raises(TypeError, match=expected_error_message):
        brands_service.get_by_id(repository=invalid_repository, brand_id=valid_brand_id)


# VALID TESTS FOR get_all_brands

def test_get_all_brands_with_valid_partitions(mySQLBrandRepository):
    brands = brands_service.get_all(repository=mySQLBrandRepository)
    assert isinstance(brands, list), "Expected a list of BrandReturnResource instances"

    for brand, expected in zip(brands, valid_brand_test_data):
        assert isinstance(brand, BrandReturnResource), "Expected a BrandReturnResource instance"
        assert brand.id == expected.get('id'), (
            f"The actual brand ID: '{brand.id}', does not match "
            f"the expected brand ID: '{expected.get('id')}'"
        )


@pytest.mark.parametrize("valid_brand_limit, expected_amount_of_brands", [
    (-1, 5),
    (0, 5),
    (None, 5),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 5),
])
def test_get_all_brand_with_valid_brand_limit_partitions(
        mySQLBrandRepository, valid_brand_limit, expected_amount_of_brands
):
    brands = brands_service.get_all(
        repository=mySQLBrandRepository,
        brands_limit=valid_brand_limit
    )

    assert isinstance(brands, list), (
        f"Expected a list of BrandReturnResource instances, "
        f"but got {type(brands).__name__}"
    )

    actual_amount_of_brands = len(brands)

    assert actual_amount_of_brands == expected_amount_of_brands, (
        f"Actual amount of brands {actual_amount_of_brands} does not match "
        f"the expected amount of brands {expected_amount_of_brands}"
    )

    for brand in brands:
        assert isinstance(brand, BrandReturnResource), (
            f"Expected a BrandReturnResource instance, "
            f"but got {type(brand).__name__}"
        )


# INVALID TESTS FOR get_all_brands
@pytest.mark.parametrize("invalid_repository, expected_error_message", [
    (None, "repository must be of type BrandRepository, not NoneType."),
    (123, "repository must be of type BrandRepository, not int."),
    (True, "repository must be of type BrandRepository, not bool."),
    ("repository", "repository must be of type BrandRepository, not str."),
    (object(), "repository must be of type BrandRepository, not object."),
])
def test_get_all_brands_with_invalid_repository_type(
        invalid_repository, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        brands_service.get_all(repository=invalid_repository)


@pytest.mark.parametrize("invalid_brands_limit, expected_error_message", [
    ("10", "brands_limit must be of type int or None, not str."),
    (1.5, "brands_limit must be of type int or None, not float."),
    (True, "brands_limit must be of type int or None, not bool."),
    (object(), "brands_limit must be of type int or None, not object."),
])
def test_get_all_brands_invalid_brands_limit(
        mySQLBrandRepository, invalid_brands_limit, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        brands_service.get_all(repository=mySQLBrandRepository, brands_limit=invalid_brands_limit)
