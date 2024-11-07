import pytest
from app.services import colors_service

@pytest.mark.parametrize("uuid, expected", [
    ("e2164054-4cb8-49d5-a0da-eca5b36a0b3b", {"name": "black"}),
])
def test_get_color_by_id_with_valid_partitions(mySQLColorRepository, uuid, expected):
    color = colors_service.get_by_id(mySQLColorRepository, uuid)
    assert color.name == expected["name"]

@pytest.mark.parametrize("uuid", [
    (None),
])
def test_get_color_by_id_with_invalid_partitions(mySQLColorRepository, uuid):
    with pytest.raises(TypeError):
        colors_service.get_by_id(mySQLColorRepository, uuid)
