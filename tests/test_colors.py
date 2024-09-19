import pytest
from tests import factory
from db import get_current_db_name

def test_get_colors(client, session):
    new_color_one = factory.create_color_in_test_db(session, "Green")
    new_color_two = factory.create_color_in_test_db(session)
    response = client.get("/colors")
    assert response.status_code == 200, ('Failed to connect to the "/color" get endpoint.')
    
    assert response.json()["data"] == [
        new_color_one.as_resource(),
        new_color_two.as_resource()
    ], (f'Failed to return the two colors "{new_color_one.color}", "{new_color_two.color}" from the {get_current_db_name(session)}')