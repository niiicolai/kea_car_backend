import pytest
from pydantic import ValidationError
from app.resources.sales_person_resource import SalesPersonLoginResource, SalesPersonCreateResource


# VALID test data for SalesPersonCreateResource
@pytest.mark.parametrize("props", [
    ({"email": "local@localhost.something", "password": "password", "first_name": "Local", "last_name": "Local"}),
])
def test_SalesPersonCreateResource_valid_partitions_and_boundaries(props):
    resource = SalesPersonCreateResource(**props)
    
    assert resource.email == props["email"]
    assert resource.password == props["password"]
    assert resource.first_name == props["first_name"]
    assert resource.last_name == props["last_name"]


# INVALID test data for SalesPersonCreateResource
@pytest.mark.parametrize("props, errorType, errorMessage", [
    ({"password": "password", "first_name": "Local", "last_name": "Local"}, ValidationError, r"email"),
    ({"email": None, "password": "password", "first_name": "Local", "last_name": "Local"}, ValidationError, r"email"),
    ({"email": [], "password": "password", "first_name": "Local", "last_name": "Local"}, ValidationError, r"email"),
    ({"email": {}, "password": "password", "first_name": "Local", "last_name": "Local"}, ValidationError, r"email"),
    ({"email": 0, "password": "password", "first_name": "Local", "last_name": "Local"}, ValidationError, r"email"),
    ({"email": "test@localhost.something", "first_name": "Local", "last_name": "local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": None, "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": [], "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": {}, "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": " ", "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": "", "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": 0, "first_name": "Local", "last_name": "Local"}, ValidationError, r"password"),
    ({"email": "test@localhost.something", "password": "password", "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": None, "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": [], "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": {}, "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": 0, "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": " ", "last_name": "Local"}, ValidationError, r"first_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local"}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local", "last_name": None}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local", "last_name": []}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local", "last_name": {}}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local", "last_name": 0}, ValidationError, r"last_name"),
    ({"email": "test@localhost.something", "password": "password", "first_name": "Local", "last_name": " "}, ValidationError, r"last_name"),
])
def test_SalesPersonCreateResource_with_invalid_partitions_and_boundaries(props, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        SalesPersonCreateResource(**props)
        
        
def test_SalesPersonCreateResource_with_email_too_long():
    email = "12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com"
    with pytest.raises(ValueError, match="The given email .* is .* characters too long, it can only be maximum 100 characters and not .*"):
        SalesPersonCreateResource(email=email, password="password", first_name="Local", last_name="Local")
        

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

