from app.services import colors_service
from app.repositories.color_repositories import MySQLColorRepository

def test_get_color_by_id(session):
    # This test does not work, we need a structure of how we do tests.
    color_repo = MySQLColorRepository(session)
    color = colors_service.get_by_id(color_repo, "e2164054-4cb8-49d5-a0da-eca5b36a0b3b")
    assert color.name == "black"