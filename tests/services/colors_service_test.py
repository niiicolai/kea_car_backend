import pytest
from app.services import colors_service
from app.resources.color_resource import ColorReturnResource
from app.exceptions.database_errors import UnableToFindIdError

valid_colors = [
    ("e2164054-4cb8-49d5-a0da-eca5b36a0b3b",
     {
         "name": "black",
         "price": 0.0,
         "red_value": 0,
         "green_value": 0,
         "blue_value": 0
     }),
    ("7bb35b1d-37ff-43c2-988a-cf85c5b6d690",
     {
         "name": "white",
         "price": 399.95,
         "red_value": 255,
         "green_value": 255,
         "blue_value": 255
     }),
    ("74251648-a7b1-492a-ab2a-f2248c58da00",
     {
         "name": "red",
         "price": 199.95,
         "red_value": 255,
         "green_value": 0,
         "blue_value": 0
     }),
    ("5e755eb3-0099-4cdd-b064-d8bd95968109",
     {
         "name": "blue",
         "price": 99.95,
         "red_value": 0,
         "green_value": 0,
         "blue_value": 255
     }),
    ("14382aba-6fe6-405d-a5e2-0b8cfd1f9582",
     {
         "name": "silver",
         "price": 299.95,
         "red_value": 192,
         "green_value": 192,
         "blue_value": 192
     }),
]

# VALID TESTS FOR get_color_by_id

@pytest.mark.parametrize("valid_color_id, expected_color", valid_colors)
def test_get_color_by_id_with_valid_partitions(mySQLColorRepository, valid_color_id, expected_color):
    color = colors_service.get_by_id(
        repository=mySQLColorRepository,
        color_id=valid_color_id
    )

    assert isinstance(color, ColorReturnResource)\
        , f"Color is not of type ColorReturnResource, but {type(color).__name__}"

    assert color.id == valid_color_id\
        , f"Color ID {color.id} does not match {valid_color_id}"

    assert color.name == expected_color['name']\
        , f"Color name {color.name} does not match {expected_color['name']}"

    assert color.price == expected_color['price']\
        , f"Color price {color.price} does not match {expected_color['price']}"

    assert color.red_value == expected_color['red_value']\
        , f"Color red value {color.red_value} does not match {expected_color['red_value']}"

    assert color.green_value == expected_color['green_value']\
        , f"Color green value {color.green_value} does not match {expected_color['green_value']}"

    assert color.blue_value == expected_color['blue_value']\
        , f"Color blue value {color.blue_value} does not match {expected_color['blue_value']}"


# INVALID TESTS FOR get_color_by_id

@pytest.mark.parametrize("invalid_color_id, expected_error, expecting_error_message", [
    (None, TypeError, "color_id must be of type str, not NoneType."),
    (1, TypeError, "color_id must be of type str, not int."),
    (True, TypeError, "color_id must be of type str, not bool."),
    ("unknown-id", UnableToFindIdError, "Color with ID: unknown-id does not exist."),
])
def test_get_color_by_id_with_invalid_color_id_partitions(
        mySQLColorRepository, invalid_color_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        colors_service.get_by_id(
            repository=mySQLColorRepository,
            color_id=invalid_color_id
        )

@pytest.mark.parametrize("invalid_color_repository, expecting_error_message", [
    (None, "repository must be of type ColorRepository, not NoneType."),
    (1, "repository must be of type ColorRepository, not int."),
    (True, "repository must be of type ColorRepository, not bool."),
    ("repository", "repository must be of type ColorRepository, not str."),
])
def test_get_color_by_id_with_invalid_repository_type_partitions(
        invalid_color_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_by_id(
            repository=invalid_color_repository,
            color_id="e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
        )


def test_get_color_by_id_with_invalid_repository_types_partitions(
        mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLAccessoryRepository).__name__}."
                       ):
        colors_service.get_by_id(
            repository=mySQLAccessoryRepository,
            color_id="e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."
                       ):
        colors_service.get_by_id(
            repository=mySQLBrandRepository,
            color_id="e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLInsuranceRepository).__name__}."
                       ):
        colors_service.get_by_id(
            repository=mySQLInsuranceRepository,
            color_id="e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
        )


# VALID TESTS FOR get_all_colors

@pytest.mark.parametrize("valid_color_id, expected_color", valid_colors)
def test_get_all_colors_with_valid_partitions(mySQLColorRepository, valid_color_id, expected_color):
    expected_color_name = expected_color.get('name')
    expected_color_price = expected_color.get('price')
    expected_color_red_value = expected_color.get('red_value')
    expected_color_green_value = expected_color.get('green_value')
    expected_color_blue_value = expected_color.get('blue_value')


    colors = colors_service.get_all(repository=mySQLColorRepository)

    assert isinstance(colors, list) and all(isinstance(color, ColorReturnResource) for color in colors)\
        , f"Colors are not a list of ColorReturnResource objects, but {type(colors).__name__}"

    assert len(colors) == 5, \
        f"There should be 5 colors, not '{len(colors)}'"

    assert any(color.id == valid_color_id for color in colors) == True, \
        f"Color ID {valid_color_id} not found"

    assert next((color.name for color in colors if color.id == valid_color_id), None) == expected_color_name\
        , f"Color name {expected_color_name} not found"

    assert next((color.price for color in colors if color.id == valid_color_id), None) == expected_color_price\
        , f"Color price {expected_color_price} not found"

    assert next((color.red_value for color in colors if color.id == valid_color_id), None) == expected_color_red_value\
        , f"Color red value {expected_color_red_value} not found"

    assert next((color.green_value for color in colors if color.id == valid_color_id), None) == expected_color_green_value\
        , f"Color green value {expected_color_green_value} not found"

    assert next((color.blue_value for color in colors if color.id == valid_color_id), None) == expected_color_blue_value\
        , f"Color blue value {expected_color_blue_value} not found"


@pytest.mark.parametrize("valid_colors_limit, expecting_color_amount", [
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
def test_get_all_colors_with_valid_colors_limit_values_partitions(
        mySQLColorRepository, valid_colors_limit, expecting_color_amount
):
    colors = colors_service.get_all(
        repository=mySQLColorRepository,
        colors_limit=valid_colors_limit
    )

    assert isinstance(colors, list) and all(isinstance(color, ColorReturnResource) for color in colors)\
        , f"Colors are not a list of ColorReturnResource objects, but {type(colors).__name__}"

    assert len(colors) == expecting_color_amount \
        , f"There should be {expecting_color_amount} colors, not '{len(colors)}'"


# INVALID TESTS FOR get_all_colors

@pytest.mark.parametrize("invalid_colors_limit, expecting_error_message", [
    ("1", "colors_limit must be of type int or None, not str."),
    (1.0, "colors_limit must be of type int or None, not float."),
    (True, "colors_limit must be of type int or None, not bool."),
])
def test_get_all_colors_with_invalid_colors_limit_values_partitions(
        mySQLColorRepository, invalid_colors_limit, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_all(
            repository=mySQLColorRepository,
            colors_limit=invalid_colors_limit
        )


@pytest.mark.parametrize("invalid_color_repository, expecting_error_message", [
    (None, "repository must be of type ColorRepository, not NoneType."),
    (1, "repository must be of type ColorRepository, not int."),
    ("repository", "repository must be of type ColorRepository, not str."),
])
def test_get_all_colors_with_invalid_repository_type_partitions(
        invalid_color_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_all(repository=invalid_color_repository)


def test_get_all_colors_with_invalid_repository_types_partitions(
        mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLAccessoryRepository).__name__}."
                       ):
        colors_service.get_all(repository=mySQLAccessoryRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."
                       ):
        colors_service.get_all(repository=mySQLBrandRepository)

    with pytest.raises(TypeError,
                       match=f"repository must be of type ColorRepository, "
                             f"not {type(mySQLInsuranceRepository).__name__}."
                       ):
        colors_service.get_all(repository=mySQLInsuranceRepository)
