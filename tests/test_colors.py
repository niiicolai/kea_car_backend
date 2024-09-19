import pytest
import factory

def test_get_colors(client, session):
    new_color = factory.create_color_in_test_db(session)
    response = client.get(f"/colors")
    assert response.status_code == 200
    assert response.json()["data"] == [
        new_color.as_resource()
    ]