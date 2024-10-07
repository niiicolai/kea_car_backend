import pytest
from tests import factory
from db import get_current_db_name

def test_get_colors(client, session):
    new_color = factory.create_color_in_test_db(session)
    response = client.get("/colors")
    assert response.status_code == 200, ('Failed to connect to the "/color" get endpoint.')
    
    actual_response_data = response.json()
    
    expected_response_data = [new_color.as_resource().model_dump(mode="json")]
    
    assert actual_response_data == expected_response_data, (f'Failed to return colors from the {get_current_db_name(session)}')