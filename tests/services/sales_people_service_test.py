import pytest
from app.services import sales_people_service
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.exceptions.invalid_credentials_errors import IncorrectEmailError, IncorrectPasswordError
from app.resources.sales_person_resource import (
    SalesPersonLoginResource, SalesPersonReturnResource, SalesPersonCreateResource
)
from app.core.security import Token


# VALID TESTS FOR get_all
@pytest.mark.parametrize("options", [
    ({"limit": 1}),
    ({"limit": 2}),
    ({"limit": 3}),
    ({"limit": None}),
])
def test_get_all_with_valid_partitions_and_boundaries(mySQLSalesPersonRepository, options):
    sales_people = sales_people_service.get_all(mySQLSalesPersonRepository, options["limit"])
    
    assert isinstance(sales_people, list), f"Sales_people is not a list, but {type(sales_people).__name__}"
    assert all(isinstance(purchase, SalesPersonReturnResource) for purchase in sales_people) \
        , f"sales_people are not a list of SalesPersonReturnResource objects, but {type(sales_people).__name__}"
    
    if options["limit"] is not None:
        assert len(sales_people) <= options["limit"], f"Number of Sales_people is greater than the limit of {options['limit']}"


# INVALID TESTS FOR get_all
@pytest.mark.parametrize("options, errorType, errorMessage", [
    ({"limit": True}, TypeError, "sales_people_limit must be of type int or None, not bool."),
    ({"limit": False}, TypeError, "sales_people_limit must be of type int or None, not bool."),
    ({"limit": []}, TypeError, "sales_people_limit must be of type int or None, not list."),
    ({"limit": {}}, TypeError, "sales_people_limit must be of type int or None, not dict."),
    ({"limit": "a"}, TypeError, "sales_people_limit must be of type int or None, not str."),
    ({"limit": ""}, TypeError, "sales_people_limit must be of type int or None, not str."),
])
def test_get_all_with_invalid_partitions_and_boundaries(mySQLSalesPersonRepository, options, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.get_all(mySQLSalesPersonRepository, options["limit"])


@pytest.mark.parametrize("repository, errorType, errorMessage", [
    ({}, TypeError, "repository must be of type SalesPersonRepository, not dict."),
    ([], TypeError, "repository must be of type SalesPersonRepository, not list."),
    (True, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (False, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (None, TypeError, "repository must be of type SalesPersonRepository, not None."),
    (1, TypeError, "repository must be of type SalesPersonRepository, not int."),
    ("", TypeError, "repository must be of type SalesPersonRepository, not str."),
])
def test_get_all_with_invalid_repository(repository, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.get_all(repository)


# VALID TESTS FOR get_by_id
@pytest.mark.parametrize("id, expected", [
    ("d096d2e1-f06a-4555-9cd1-afa9f930f10c", {
         "id": "d096d2e1-f06a-4555-9cd1-afa9f930f10c", 
         "email": "james@gmail.com", 
         "first_name": "James",
         "last_name": "Jamesen",
    }),
    ("f9097a97-eca4-49b6-85a0-08423789c320", {
         "id": "f9097a97-eca4-49b6-85a0-08423789c320", 
         "email": "hans@gmail.com", 
         "first_name": "Hans",
         "last_name": "Hansen",
    }),
])
def test_get_by_id_with_valid_partitions_and_boundaries(mySQLSalesPersonRepository, id, expected):
    sales_person = sales_people_service.get_by_id(mySQLSalesPersonRepository, id)
    
    assert isinstance(sales_person, SalesPersonReturnResource), f"Purchase is not a PurchaseReturnResource object, but {type(sales_person).__name__}"
    assert sales_person.id == expected["id"], f"Sales_person id is not {expected['id']}, but {sales_person.id}"
    assert sales_person.email == expected["email"], f"Sales_person email is not {expected['email']}, but {sales_person.email}"
    assert sales_person.first_name == expected["first_name"], f"Sales_person first_name is not {expected['first_name']}, but {sales_person.first_name}"
    assert sales_person.last_name == expected["last_name"], f"Sales_person last_name is not {expected['last_name']}, but {sales_person.last_name}"


# INVALID TESTS FOR get_all_sales_people
@pytest.mark.parametrize("id, errorType, errorMessage", [
    ("", UnableToFindIdError, "Sales Person with ID:  does not exist."),
    ("fake_id", UnableToFindIdError, "Sales Person with ID: fake_id does not exist."),
    (None, TypeError, "sales_person_id must be of type str, not None."),
    ({}, TypeError, "sales_person_id must be of type str, not dict."),
    ([], TypeError, "sales_person_id must be of type str, not list."),
    (True, TypeError, "sales_person_id must be of type str, not bool."),
    (False, TypeError, "sales_person_id must be of type str, not bool."),
    (1, TypeError, "sales_person_id must be of type str, not int."),
])
def test_get_by_id_with_invalid_partitions_and_boundaries(mySQLSalesPersonRepository, id, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.get_by_id(mySQLSalesPersonRepository, id)
        
        
@pytest.mark.parametrize("repository, errorType, errorMessage", [
    ({}, TypeError, "repository must be of type SalesPersonRepository, not dict."),
    ([], TypeError, "repository must be of type SalesPersonRepository, not list."),
    (True, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (False, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (None, TypeError, "repository must be of type SalesPersonRepository, not None."),
    (1, TypeError, "repository must be of type SalesPersonRepository, not int."),
    ("", TypeError, "repository must be of type SalesPersonRepository, not str."),
])
def test_get_by_id_with_invalid_repository(repository, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.get_by_id(repository, "d096d2e1-f06a-4555-9cd1-afa9f930f10c")


# VALID TESTS FOR login
@pytest.mark.parametrize("salesPersonResource, expected", [
    (SalesPersonLoginResource(email="james@gmail.com", password="12345678"), {
        "id": "d096d2e1-f06a-4555-9cd1-afa9f930f10c",
        "email": "james@gmail.com",
        "first_name": "James",
        "last_name": "Jamesen",        
    }),
])
def test_login_with_valid_partitions_and_boundaries(mySQLSalesPersonRepository, salesPersonResource, expected):
    token = sales_people_service.login(mySQLSalesPersonRepository, salesPersonResource)
    
    assert isinstance(token, Token), f"token is not a Token, but {type(token).__name__}"
    assert token.access_token is not None, f"Token access_token is None."
    assert token.token_type == "bearer", f"Token token_type is not 'bearer', but {token.token_type}"
    assert isinstance(token.sales_person, SalesPersonReturnResource), f"Token sales_person is not a SalesPersonReturnResource, but {type(token.sales_person).__name__}"
    assert token.sales_person.id == expected["id"], f"Sales_person id is not {expected['id']}, but {token.sales_person.id}"
    assert token.sales_person.email == expected["email"], f"Sales_person email is not {expected['email']}, but {token.sales_person.email}"
    assert token.sales_person.first_name == expected["first_name"], f"Sales_person first_name is not {expected['first_name']}, but {token.sales_person.first_name}"
    assert token.sales_person.last_name == expected["last_name"], f"Sales_person last_name is not {expected['last_name']}, but {token.sales_person.last_name}"    


# INVALID TESTS FOR login
@pytest.mark.parametrize("salesPersonResource, errorType, errorMessage", [
    ("", TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not str."),
    (None, TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not NoneType."),
    ({}, TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not dict."),
    ([], TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not list."),
    (True, TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not bool."),
    (False, TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not bool."),
    (1, TypeError, "sales_person_login_data must be of type SalesPersonLoginResource, not int."),
    (SalesPersonLoginResource(email="no_user@gmail.com", password="1234"), IncorrectEmailError, 'IncorrectEmailException: The email "no_user@gmail.com" is incorrect."'),
    (SalesPersonLoginResource(email="james@gmail.com", password="not_correct"), IncorrectPasswordError, 'The password not_correct is incorrect for the email james@gmail.com.'),
])
def test_login_with_invalid_partitions_and_boundaries(mySQLSalesPersonRepository, salesPersonResource, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.login(mySQLSalesPersonRepository, salesPersonResource)


@pytest.mark.parametrize("repository, errorType, errorMessage", [
    ({}, TypeError, "repository must be of type SalesPersonRepository, not dict."),
    ([], TypeError, "repository must be of type SalesPersonRepository, not list."),
    (True, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (False, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (None, TypeError, "repository must be of type SalesPersonRepository, not None."),
    (1, TypeError, "repository must be of type SalesPersonRepository, not int."),
    ("", TypeError, "repository must be of type SalesPersonRepository, not str."),
])
def test_login_with_invalid_repository(repository, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.login(repository, SalesPersonLoginResource(email="james@gmail.com", password="12345678"))


# VALID TESTS FOR create
@pytest.mark.parametrize("salesPersonCreateResource", [
    (SalesPersonCreateResource(
        email="test@localhost.something", 
        password="12345678",
        first_name="Test",
        last_name="Tester",
    )),
    (SalesPersonCreateResource(
        email="test2@localhost.something", 
        password="12345678",
        first_name="Testtwo",
        last_name="Testertwo",
    )),
])
def test_create_with_valid_partitions_and_boundaries(mySQLSalesPersonRepository, salesPersonCreateResource):
    sales_person = sales_people_service.create(mySQLSalesPersonRepository, salesPersonCreateResource)
    
    assert isinstance(sales_person, SalesPersonReturnResource), f"Token sales_person is not a SalesPersonReturnResource, but {type(sales_person).__name__}"
    assert sales_person.email == salesPersonCreateResource.email, f"Sales_person email is not {salesPersonCreateResource.email}, but {sales_person.email}"
    assert sales_person.first_name == salesPersonCreateResource.first_name, f"Sales_person first_name is not {salesPersonCreateResource.first_name}, but {sales_person.first_name}"
    assert sales_person.last_name == salesPersonCreateResource.last_name, f"Sales_person last_name is not {salesPersonCreateResource.last_name}, but {sales_person.last_name}"
    assert sales_person.id is not None, f"Sales_person id is None."


# INVALID TESTS FOR create
@pytest.mark.parametrize("salesPersonCreateResource, errorType, errorMessage", [
    ("", TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not str."),
    (None, TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not NoneType."),
    ({}, TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not dict."),
    ([], TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not list."),
    (True, TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not bool."),
    (False, TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not bool."),
    (1, TypeError, "sales_person_create_data must be of type SalesPersonCreateResource, not int."),
    (SalesPersonCreateResource(
        email="james@gmail.com", 
        password="12345678",
        first_name="Testthree",
        last_name="Testerthree",
    ), AlreadyTakenFieldValueError, 'Sales Person with email: james@gmail.com is already taken.'),
])
def test_create_with_invalid_partitions_and_boundaries(mySQLSalesPersonRepository, salesPersonCreateResource, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.create(mySQLSalesPersonRepository, salesPersonCreateResource)


@pytest.mark.parametrize("repository, errorType, errorMessage", [
    ({}, TypeError, "repository must be of type SalesPersonRepository, not dict."),
    ([], TypeError, "repository must be of type SalesPersonRepository, not list."),
    (True, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (False, TypeError, "repository must be of type SalesPersonRepository, not bool."),
    (None, TypeError, "repository must be of type SalesPersonRepository, not None."),
    (1, TypeError, "repository must be of type SalesPersonRepository, not int."),
    ("", TypeError, "repository must be of type SalesPersonRepository, not str."),
])
def test_create_with_invalid_repository(repository, errorType, errorMessage):
    with pytest.raises(errorType, match=errorMessage):
        sales_people_service.create(repository, SalesPersonCreateResource(
            email="test123@localhost.something", 
            password="12345678",
            first_name="Test",
            last_name="Tester",
        ))
        
