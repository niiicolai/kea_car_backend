import pytest
from pydantic import ValidationError
from app.resources.sales_person_resource import SalesPersonLoginResource, SalesPersonCreateResource

# VALID and INVALID test data for SalesPersonCreateResource

valid_email_test_data = [
    ("hans@gmail.com", "No Change"),
    ("hans@gmail.co.uk", "No Change"),
    ("123hans@gmail.com", "No Change"),
    (" hans@gmail.com ", "hans@gmail.com"),
    ("ab@cd.ef", "No Change"),  # Valid lower boundary
    ("ab@cd.efg", "No Change"),  # Valid lower boundary
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.co",
     "No Change"),  # Valid upper boundary
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
     "No Change"),  # Valid upper boundary
]

invalid_email_test_data = [
    (None, "Input should be a valid string"),
    ("hansgmail.com", "is not a valid email address"),
    ("hans@", "is not a valid email address"),
    ("hans@g mail.com", "is not a valid email address"),
    ("hans.gmail@com", "is not a valid email address"),
    (12345678, "Input should be a valid string"),
    (True, "Input should be a valid string"),
    ("ab@cd.e", "too short"),  # Invalid lower boundary
    ("12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com",
     "too long")  # Invalid upper boundary
]

valid_first_name_test_data = [
    ("Hans", "No Change"),
    ("Hans Hansy", "No Change"),
    ("hAnS", "Hans"),
    ("hAnS hAnSy", "Hans Hansy"),
    ("Hans-Hansy", "No Change"),
    ("hAnS-hAnSy", "Hans-Hansy"),
    (" Hans ", "Hans"),
    (" Hans Hansy ", "Hans Hansy"),
    (" Hans-Hansy ", "Hans-Hansy"),
    ("hans", "Hans"),
    ("hans hansy", "Hans Hansy"),
    ("hans-hansy", "Hans-Hansy"),
    ("H", "No Change"),  # Valid lower boundary
    ("Ha", "No Change"),  # Valid lower boundary
    ("Hans Maximilian Elizabeth Anna-Maria Lucre-Victor",  # Valid upper boundary
     "No Change"),
    ("Hans Maximilian Elizabeth Anna-Maria Lucre-Victori",  # Valid upper boundary
     "No Change"),
]

invalid_first_name_test_data = [
    (None, "Input should be a valid string"),
    ("Henr1k", "can only contain alphabetic characters"),
    ("H@nrik", "can only contain alphabetic characters"),
    ("Henrik  Henry", "contains extra whitespaces"),
    ("-Henrik-Henry", "starts or ends with a hyphen"),
    ("Henrik-Henry-", "starts or ends with a hyphen"),
    ("-Henrik-Henry-", "starts or ends with a hyphen"),
    ("Henrik - Henry", "contains whitespace before or after a hyphen"),
    (True, "Input should be a valid string"),
    (1234, "Input should be a valid string"),
    ("", "is too short"),  # Invalid lower boundary
    ("Hans Maximilian Elizabeth Anna-Maria Lucre-Victoria", "is too long"),  # Invalid upper boundary
]

valid_last_name_test_data = [
    ("Hansen", "No Change"),
    (" Hansen ", "Hansen"),
    ("hansen", "Hansen"),
    ("hAnSeN", "Hansen"),
    ("Hanerson-Hansen", "No Change"),
    ("hAnErSoN-hAnSeN", "Hanerson-Hansen"),
    ("hanerson-hansen", "Hanerson-Hansen"),
    ("H", "No Change"),  # Valid lower boundary
    ("Ha", "No Change"),  # Valid lower boundary
    ("Hansenfeatherstonehaughworthingtonsmythenbishopso", "No Change"),  # Valid upper boundary
    ("Hansenfeatherstonehaughworthingtonsmythenbishopson", "No Change"),  # Valid upper boundary
]

invalid_last_name_test_data = [
    (None, "Input should be a valid string"),
    ("Hanerson Hansen", "contains whitespace"),
    ("-Hansen", "starts or ends with a hyphen"),
    ("Hansen-", "starts or ends with a hyphen"),
    ("Hans1n", "can only contain alphabetic characters"),
    ("H@nsen", "can only contain alphabetic characters"),
    (True, "Input should be a valid string"),
    (1234, "Input should be a valid string"),
    ("", "is too short"),  # Invalid lower boundary
    ("Hansenfeatherstonehaughworthingtonsmythenbishopsons", "is too long"),  # Invalid upper boundary
]

valid_password_test_data = [
    "password",
    "pAsSwOrD",
    "PASSWORD",
    "p@ssw0rd",
    "password123",
    "p@ssword",
    "P@ssWord123",
    "1234567",  # Valid lower boundary
    "12345678",  # Valid lower boundary
    "12345678901234567890123456789",  # Valid upper boundary
    "123456789012345678901234567890",  # Valid upper boundary
]

invalid_password_test_data = [
    (None, "Input should be a valid string"),
    ("pass word", "contains whitespace"),
    (12345678, "Input should be a valid string"),
    (True, "Input should be a valid string"),
    ("123456", "is too short"),  # Invalid lower boundary
    ("1234567890123456789012345678901", "is too long"),  # Invalid upper boundary
]


# VALID TESTS FOR SalesPersonCreateResource

def test_create_sales_person_resource_works_with_valid_sales_person_data(valid_sales_person_data):
    sales_person_create_data = SalesPersonCreateResource(
        **valid_sales_person_data
    )
    assert sales_person_create_data.email == valid_sales_person_data.get("email") \
        , (f"Email: {sales_person_create_data.email} does not match "
           f"expected email: {valid_sales_person_data.get('email')}")

    assert sales_person_create_data.first_name == valid_sales_person_data.get("first_name") \
        , (f"First name: {sales_person_create_data.first_name} does not match "
           f"expected first name: {valid_sales_person_data.get('first_name')}")

    assert sales_person_create_data.last_name == valid_sales_person_data.get("last_name") \
        , (f"Last name: {sales_person_create_data.last_name} does not match "
           f"expected last name: {valid_sales_person_data.get('last_name')}")

    assert sales_person_create_data.password == valid_sales_person_data.get("password") \
        , (f"Password: {sales_person_create_data.password} does not match "
           f"expected password: {valid_sales_person_data.get('password')}")


@pytest.mark.parametrize("valid_email, expected_output", valid_email_test_data)
def test_sales_person_create_resource_valid_email_data(valid_sales_person_data, valid_email, expected_output):
    valid_sales_person_data.pop("email")
    sales_person_create_data = SalesPersonCreateResource(
        email=valid_email,
        **valid_sales_person_data
    )
    expected_email = valid_email if expected_output == "No Change" else expected_output
    assert sales_person_create_data.email == expected_email \
        , (f"Email: {sales_person_create_data.email} does not match "
           f"expected email: {expected_email}")


@pytest.mark.parametrize("valid_first_name, expected_outcome", valid_first_name_test_data)
def test_create_sales_person_resource_works_with_valid_first_name_data(
        valid_sales_person_data, valid_first_name, expected_outcome
):
    valid_sales_person_data.pop("first_name")
    sales_person_create_data = SalesPersonCreateResource(
        first_name=valid_first_name,
        **valid_sales_person_data
    )
    expected_first_name = valid_first_name if expected_outcome == "No Change" else expected_outcome
    assert sales_person_create_data.first_name == expected_first_name \
        , (f"First name: {sales_person_create_data.first_name} does not match "
           f"expected first name: {expected_first_name}")


@pytest.mark.parametrize("valid_last_name, expected_outcome", valid_last_name_test_data)
def test_create_sales_person_resource_works_with_valid_last_name_data(
        valid_sales_person_data, valid_last_name, expected_outcome
):
    valid_sales_person_data.pop("last_name")
    sales_person_create_data = SalesPersonCreateResource(
        last_name=valid_last_name,
        **valid_sales_person_data
    )
    expected_last_name = valid_last_name if expected_outcome == "No Change" else expected_outcome
    assert sales_person_create_data.last_name == expected_last_name \
        , (f"Last name: {sales_person_create_data.last_name} does not match "
           f"expected last name: {expected_last_name}")


@pytest.mark.parametrize("valid_password", valid_password_test_data)
def test_create_sales_person_resource_works_with_valid_password_data(
        valid_sales_person_data, valid_password
):
    valid_sales_person_data.pop("password")
    sales_person_create_data = SalesPersonCreateResource(
        password=valid_password,
        **valid_sales_person_data
    )
    expected_password = valid_password
    assert sales_person_create_data.password == expected_password \
        , (f"Password: {sales_person_create_data.password} does not match "
           f"expected password: {expected_password}")




# INVALID TESTS FOR SalesPersonCreateResource

@pytest.mark.parametrize("missing_field",
                         ["all_fields", "email", "first_name", "last_name", "password"])
def test_create_sales_person_resource_does_not_work_without_setting_all_fields(valid_sales_person_data, missing_field):
    if missing_field == "all_fields":
        with pytest.raises(ValidationError, match="Field required"):
            SalesPersonCreateResource(), "All fields should be required"
    else:
        valid_sales_person_data.pop(missing_field)
        with pytest.raises(ValidationError, match=f"{missing_field}\n  Field required"):
            SalesPersonCreateResource(
                **valid_sales_person_data
            ), f"{missing_field} should be required"


@pytest.mark.parametrize("invalid_email, expecting_error_message", invalid_email_test_data)
def test_create_sales_person_resource_does_not_work_with_invalid_email(
        valid_sales_person_data, invalid_email, expecting_error_message
):
    valid_sales_person_data.pop("email")
    with pytest.raises(ValidationError, match=expecting_error_message):
        SalesPersonCreateResource(
            email=invalid_email,
            **valid_sales_person_data
        ), f"Email: {invalid_email} should not be valid"


@pytest.mark.parametrize("invalid_first_name, expecting_error_message", invalid_first_name_test_data)
def test_create_sales_person_resource_does_not_work_with_invalid_first_name_data(
        valid_sales_person_data, invalid_first_name, expecting_error_message
):
    valid_sales_person_data.pop("first_name")
    with pytest.raises(ValidationError, match=expecting_error_message):
        SalesPersonCreateResource(
            first_name=invalid_first_name,
            **valid_sales_person_data
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name, expecting_error_message", invalid_last_name_test_data)
def test_create_sales_person_resource_does_not_work_with_invalid_last_name_data(
        valid_sales_person_data, invalid_last_name, expecting_error_message
):
    valid_sales_person_data.pop("last_name")
    with pytest.raises(ValidationError, match=expecting_error_message):
        SalesPersonCreateResource(
            last_name=invalid_last_name,
            **valid_sales_person_data
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_password, expecting_error_message", invalid_password_test_data)
def test_create_sales_person_resource_does_not_work_with_invalid_password_data(
        valid_sales_person_data, invalid_password, expecting_error_message
):
    valid_sales_person_data.pop("password")
    with pytest.raises(ValidationError, match=expecting_error_message):
        SalesPersonCreateResource(
            password=invalid_password,
            **valid_sales_person_data
        ), f"Password: {invalid_password} should not be valid"




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
