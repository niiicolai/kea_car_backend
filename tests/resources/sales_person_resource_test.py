import pytest
from pydantic import ValidationError
from app.resources.sales_person_resource import SalesPersonLoginResource, SalesPersonCreateResource


# VALID test data for SalesPersonCreateResource
@pytest.mark.parametrize("props", [
    ({"email": "local@localhost.something", "password": "password", "first_name": "local", "last_name": "local"}),
])
def test_SalesPersonCreateResource_valid_partitions_and_boundaries(props):
    resource = SalesPersonCreateResource(**props)
    
    assert resource.email == props["email"]
    assert resource.password == props["password"]
    assert resource.first_name == props["first_name"]
    assert resource.last_name == props["last_name"]


# INVALID test data for SalesPersonCreateResource
@pytest.mark.parametrize("props, errorType, errorMessage", [
    ({"password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"email"),
    ({"email": None, "password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"email"),
    ({"email": [], "password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"email"),
    ({"email": {}, "password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"email"),
    ({"email": 0, "password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"email"),
    ({"email": "uP2aJoTnyXoM84iwqR5GItRpSioTgELv5I3Y3jSsRbhXq99zdlq2CER92KdhkRyfH2cFHjvDu84ahlXKoWVAhvUd9zJjfabWBuBN2@toooo.long", "password": "password", "first_name": "local", "last_name": "local"}, ValidationError, r"too long"),
    ({"email": "test@localhost.something", "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": None, "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": [], "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": {}, "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": " ", "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": "", "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": 0, "first_name": "local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": "password", "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": None, "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": [], "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": {}, "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": 0, "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": " ", "last_name": "local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local"}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local", "last_name": None}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local", "last_name": []}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local", "last_name": {}}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local", "last_name": 0}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "local", "last_name": " "}, ValidationError, r"last_name"),
])
def test_SalesPersonCreateResource_with_invalid_partitions_and_boundaries(props, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        SalesPersonCreateResource(**props)
        

# VALID TESTS FOR SalesPersonLoginResource
@pytest.mark.parametrize("props", [
    ({"email": "local@localhost.something", "password": "password"}),
])
def test_SalesPersonLoginResource_valid_partitions_and_boundaries(props):
    resource = SalesPersonLoginResource(**props)
    
    assert resource.email == props["email"]
    assert resource.password == props["password"]


# INVALID TESTS FOR SalesPersonLoginResource
@pytest.mark.parametrize("props, errorType, errorMessage", [
    ({"password": "password"}, ValidationError, r"email"),
    ({"email": None, "password": "password"}, ValidationError, r"email"),
    ({"email": [], "password": "password"}, ValidationError, r"email"),
    ({"email": {}, "password": "password"}, ValidationError, r"email"),
    ({"email": 0, "password": "password"}, ValidationError, r"email"),
    ({"email": "invalid", "password": "password"}, ValidationError, r"email"),
    ({"email": "test@localhost.something"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": None}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": []}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": {}}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": 0}, ValidationError, r"password"),
])
def test_SalesPersonLoginResource_with_invalid_partitions_and_boundaries(props, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        SalesPersonLoginResource(**props)

