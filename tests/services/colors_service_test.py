import pytest
from app.services import colors_service
from app.exceptions.database_errors import UnableToFindIdError

@pytest.mark.parametrize("color_id, expected_color", [
    ("e2164054-4cb8-49d5-a0da-eca5b36a0b3b", {"name": "black"}),
    ("7bb35b1d-37ff-43c2-988a-cf85c5b6d690", {"name": "white"}),
    ("74251648-a7b1-492a-ab2a-f2248c58da00", {"name": "red"}),
    ("5e755eb3-0099-4cdd-b064-d8bd95968109", {"name": "blue"}),
    ("14382aba-6fe6-405d-a5e2-0b8cfd1f9582", {"name": "silver"}),
])
def test_get_color_by_id_with_valid_partitions(mySQLColorRepository, color_id, expected_color):
    color = colors_service.get_by_id(mySQLColorRepository, color_id)
    assert color.name == expected_color["name"]

@pytest.mark.parametrize("color_id, expected_error, expecting_error_message", [
    (None, TypeError, "color_id must be of type str, not NoneType."),
    (1, TypeError, "color_id must be of type str, not int."),
    ("unknown-id", UnableToFindIdError, "Color with ID: unknown-id does not exist."),
    ("", UnableToFindIdError, "Color with ID:  does not exist."),
    ("14382aba-6fe6-405d-a5e2-0b8cfd1f9583", UnableToFindIdError, "Color with ID: 14382aba-6fe6-405d-a5e2-0b8cfd1f9583 does not exist."),
])
def test_get_color_by_id_with_invalid_color_id_partitions(mySQLColorRepository, color_id, expected_error, expecting_error_message):
    with pytest.raises(expected_error, match=expecting_error_message):
        colors_service.get_by_id(mySQLColorRepository, color_id)

@pytest.mark.parametrize("repository, expecting_error_message", [
    (None, "repository must be of type ColorRepository, not NoneType."),
    (1, "repository must be of type ColorRepository, not int."),
    ("repository", "repository must be of type ColorRepository, not str."),
])
def test_get_color_by_id_with_invalid_repository_type_partitions(mySQLAccessoryRepository, repository, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_by_id(repository, "e2164054-4cb8-49d5-a0da-eca5b36a0b3b")

def test_get_color_by_id_with_invalid_repository_types_partitions(mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository):
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLAccessoryRepository).__name__}."):
        colors_service.get_by_id(mySQLAccessoryRepository, "e2164054-4cb8-49d5-a0da-eca5b36a0b3b")
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLBrandRepository).__name__}."):
        colors_service.get_by_id(mySQLBrandRepository, "e2164054-4cb8-49d5-a0da-eca5b36a0b3b")
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLInsuranceRepository).__name__}."):
        colors_service.get_by_id(mySQLInsuranceRepository, "e2164054-4cb8-49d5-a0da-eca5b36a0b3b")

@pytest.mark.parametrize("color_id, color_name", [
    ("e2164054-4cb8-49d5-a0da-eca5b36a0b3b", "black"),
    ("7bb35b1d-37ff-43c2-988a-cf85c5b6d690", "white"),
    ("74251648-a7b1-492a-ab2a-f2248c58da00", "red"),
    ("5e755eb3-0099-4cdd-b064-d8bd95968109", "blue"),
    ("14382aba-6fe6-405d-a5e2-0b8cfd1f9582", "silver"),
])
def test_get_all_colors_with_valid_partitions(mySQLColorRepository, color_id, color_name):
    colors = colors_service.get_all(mySQLColorRepository)
    assert len(colors) >= 5, "There should be at least 5 colors"
    assert any(color.id == color_id for color in colors) == True, f"Color ID {color_id} not found"
    assert next((color.name for color in colors if color.id == color_id), None) == color_name, f"Color name {color_name} not found"

@pytest.mark.parametrize("colors_limit, comparison_operator, expecting_color_amount", [
    (-6, ">=", 5),
    (-5, ">=", 5),
    (-4, ">=", 5),
    (-3, ">=", 5),
    (-2, ">=", 5),
    (-1, ">=", 5),
    (None, ">=", 5),
    (0, ">=", 5),
    (1, "==", 1),
    (2, "==", 2),
    (3, "==", 3),
    (4, "==", 4),
    (5, "==", 5),
    (6, ">=", 5),
])
def test_get_all_colors_with_valid_colors_limit_values_partitions(mySQLColorRepository, colors_limit, comparison_operator, expecting_color_amount):
    colors = colors_service.get_all(mySQLColorRepository, colors_limit)
    if comparison_operator == ">=":
        assert len(colors) >= expecting_color_amount, f"There should be at least {expecting_color_amount} colors"
    elif comparison_operator == "==":
        assert len(colors) == expecting_color_amount, f"There should be {expecting_color_amount} colors"


@pytest.mark.parametrize("colors_limit, expecting_error_message", [
    ("1", "colors_limit must be of type int or None, not str."),
    (1.0, "colors_limit must be of type int or None, not float."),
    (True, "colors_limit must be of type int or None, not bool."),
])
def test_get_all_colors_with_invalid_colors_limit_values_partitions(mySQLColorRepository, colors_limit, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_all(mySQLColorRepository, colors_limit)


@pytest.mark.parametrize("repository, expecting_error_message", [
    (None, "repository must be of type ColorRepository, not NoneType."),
    (1, "repository must be of type ColorRepository, not int."),
    ("repository", "repository must be of type ColorRepository, not str."),
])
def test_get_all_colors_with_invalid_repository_type_partitions(repository, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        colors_service.get_all(repository)


def test_get_all_colors_with_invalid_repository_types_partitions(mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository):
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLAccessoryRepository).__name__}."):
        colors_service.get_all(mySQLAccessoryRepository)
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLBrandRepository).__name__}."):
        colors_service.get_all(mySQLBrandRepository)
    with pytest.raises(TypeError, match=f"repository must be of type ColorRepository, not {type(mySQLInsuranceRepository).__name__}."):
        colors_service.get_all(mySQLInsuranceRepository)
