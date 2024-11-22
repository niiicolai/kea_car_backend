import pytest
from pydantic import ValidationError
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource



valid_email_test_data = [
    ("henrik@gmail.com", "henrik@gmail.com"),
    ("henrik@gmail.co.uk", "henrik@gmail.co.uk"),
    ("123henrik@gmail.com", "123henrik@gmail.com"),
    (" henrik@gmail.com ", "henrik@gmail.com"),
    ("a@b.c", "a@b.c"),
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
     "this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com"),
]

invalid_email_test_data = [
    (None, "Input should be a valid string"),
    ("henrikgmail.com", "is not a valid email address"),
    ("henrik@", "is not a valid email address"),
    ("", "is not a valid email address"),
    ("henrik@g mail.com", "is not a valid email address"),
    ("henrik.gmail@com", "is not a valid email address"),
    (123, "Input should be a valid string"),
    ("12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com", "too long")
]

valid_phone_number_test_data = [
    ("10203040", "10203040"),
    (" 10203040 ", "10203040"),
    (None, None),
    ("01234567", "01234567"),
    ("+4510203040", "+4510203040"),
    ("123456789012345678901234567890", "123456789012345678901234567890"),
]

invalid_phone_number_test_data = [
    ("", "empty string"),
    (" ", "empty string"),
    ("1A2B3C4D", "can only contain digits"),
    ("1@20304?", "can only contain digits"),
    ("102 3040", "contains whitespace"),
    ("45+10203040", "can only contain digits after the +"),
    ("+45@03040", "can only contain digits"),
    ("1234567", "is too short"),
    ("1234567890123456789012345678901", "is too long"),
    (10203040, "Input should be a valid string")
]

valid_first_name_test_data = [
    ("Henrik", "Henrik"),
    ("hEnRiK", "Henrik"),
    (" Henrik ", "Henrik"),
    ("henrik", "Henrik"),
    ("He", "He"),
    ("Maximilianaelizabethannamarialucreciavictoria", "Maximilianaelizabethannamarialucreciavictoria"),
]

invalid_first_name_test_data = [
    (None, "Input should be a valid string"),
    ("", "is an empty string"),
    ("Henr1k", "can only contain alphabetic characters"),
    ("H@nrik", "can only contain alphabetic characters"),
    ("Hen rik", "contains whitespace"),
    (True, "Input should be a valid string"),
    ("H", "is too short"),
    ("Maximilianaelizabethannamarialucreciavictorias", "is too long"),
]

valid_last_name_test_data = [
    ("Henriksen", "Henriksen"),
    ("hEnRiKsEn", "Henriksen"),
    (" Henriksen ", "Henriksen"),
    ("henriksen", "Henriksen"),
    ("He", "He"),
    ("Featherstonehaughworthingtonsmythenbishopsons", "Featherstonehaughworthingtonsmythenbishopsons"),
]

invalid_last_name_test_data = [
    (None, "Input should be a valid string"),
    ("", "is an empty string"),
    ("Henr1ksen", "can only contain alphabetic characters"),
    ("H@nriksen", "can only contain alphabetic characters"),
    ("Hen riksen", "contains whitespace"),
    (False, "Input should be a valid string"),
    ("H", "is too short"),
    ("Featherstonehaughworthingtonsmythenbishopsonss", "is too long"),
]

valid_address_test_data = [
    ("Randomgade nr. 10 4. tv.", "Randomgade nr. 10 4. tv."),
    (" Randomgade nr. 10 4. tv. ", "Randomgade nr. 10 4. tv."),
    (None, None),
    ("Rando", "Rando"),
    ("12345678 Long Street Name That Goes On Forever And Ever, Apartment 6789, "
     "Some Really Long City Name That Never Ends, A Particularly Long State "
     "Name With Extra Letters, 99999-1234, Country With A Very Long Name That "
     "Might Just Fit In Perfectly Here As Well",
     "12345678 Long Street Name That Goes On Forever And Ever, Apartment 6789, "
     "Some Really Long City Name That Never Ends, A Particularly Long State "
     "Name With Extra Letters, 99999-1234, Country With A Very Long Name That "
     "Might Just Fit In Perfectly Here As Well"),
]

invalid_address_test_data = [
    ("", "empty string"),
    (" ", "empty string"),
    ("Randomgade  nr. 10 4. tv.", "contains extra whitespace"),
    ("Randomgade   nr. 10 4. tv.", "contains extra whitespace"),
    (12345, "Input should be a valid string"),
    ("Rand", "is too short"),
    ("123456789 Long Avenue Name That Extends For A Very Long Distance, "
    "Apartment 1010101, The Very Long City Name Which Seems Nearly Endless, "
    "Another Extended State Name, 678901-1234567, Country That Has An Extremely "
    "Lengthy Name That Goes On And On Without End", "is too long"),
]

# VALID TESTS FOR CustomerCreateResource

def test_create_customer_resource_works_with_valid_customer_data(valid_customer_data):
    customer_create_data = CustomerCreateResource(
        email=valid_customer_data.get("email"),
        phone_number=valid_customer_data.get("phone_number"),
        first_name=valid_customer_data.get("first_name"),
        last_name=valid_customer_data.get("last_name"),
        address=valid_customer_data.get("address")
    )
    assert customer_create_data.email == valid_customer_data.get("email") \
        , (f"Email: {customer_create_data.email} does not match "
           f"expected email: {valid_customer_data.get('email')}")

    assert customer_create_data.phone_number == valid_customer_data.get("phone_number") \
        , (f"Phone number: {customer_create_data.phone_number} does not match "
           f"expected phone number: {valid_customer_data.get('phone_number')}")

    assert customer_create_data.first_name == valid_customer_data.get("first_name") \
        , (f"First name: {customer_create_data.first_name} does not match "
           f"expected first name: {valid_customer_data.get('first_name')}")

    assert customer_create_data.last_name == valid_customer_data.get("last_name") \
        , (f"Last name: {customer_create_data.last_name} does not match "
           f"expected last name: {valid_customer_data.get('last_name')}")

    assert customer_create_data.address == valid_customer_data.get("address") \
        , (f"Address: {customer_create_data.address} does not match "
           f"expected address: {valid_customer_data.get('address')}")


@pytest.mark.parametrize("valid_email, expected_outcome", valid_email_test_data)
def test_create_customer_resource_works_with_valid_email_data(
        valid_customer_data, valid_email, expected_outcome
):
    customer_create_data = CustomerCreateResource(
        email=valid_email,
        phone_number=valid_customer_data.get("phone_number"),
        first_name=valid_customer_data.get("first_name"),
        last_name=valid_customer_data.get("last_name"),
        address=valid_customer_data.get("address")
    )
    assert customer_create_data.email == expected_outcome \
        , (f"Email: {customer_create_data.email} "
           f"does not match expected email: {expected_outcome}")


@pytest.mark.parametrize("valid_phone_number, expected_outcome", valid_phone_number_test_data)
def test_create_customer_resource_works_with_valid_phone_number_data(
        valid_customer_data, valid_phone_number, expected_outcome
):
    customer_create_data = CustomerCreateResource(
        email=valid_customer_data.get("email"),
        phone_number=valid_phone_number,
        first_name=valid_customer_data.get("first_name"),
        last_name=valid_customer_data.get("last_name"),
        address=valid_customer_data.get("address")
    )
    assert customer_create_data.phone_number == expected_outcome \
        , (f"Phone number: {customer_create_data.phone_number} "
           f"does not match expected phone number: {expected_outcome}")


@pytest.mark.parametrize("valid_first_name, expected_outcome", valid_first_name_test_data)
def test_create_customer_resource_works_with_valid_first_name_data(
        valid_customer_data, valid_first_name, expected_outcome
):
    customer_create_data = CustomerCreateResource(
        email=valid_customer_data.get("email"),
        phone_number=valid_customer_data.get("phone_number"),
        first_name=valid_first_name,
        last_name=valid_customer_data.get("last_name"),
        address=valid_customer_data.get("address")
    )
    assert customer_create_data.first_name == expected_outcome \
        , (f"First name: {customer_create_data.first_name} does not match "
           f"expected first name: {expected_outcome}")


@pytest.mark.parametrize("valid_last_name, expected_outcome", valid_last_name_test_data)
def test_create_customer_resource_works_with_valid_last_name_data(
        valid_customer_data, valid_last_name, expected_outcome
):
    customer_create_data = CustomerCreateResource(
        email=valid_customer_data.get("email"),
        phone_number=valid_customer_data.get("phone_number"),
        first_name=valid_customer_data.get("first_name"),
        last_name=valid_last_name,
        address=valid_customer_data.get("address")
    )
    assert customer_create_data.last_name == expected_outcome \
        , (f"Last name: {customer_create_data.last_name} does not match "
           f"expected last name: {expected_outcome}")


@pytest.mark.parametrize("valid_address, expected_outcome", valid_address_test_data)
def test_create_customer_resource_works_with_valid_address_data(
        valid_customer_data, valid_address, expected_outcome
):
    customer_create_data = CustomerCreateResource(
        email=valid_customer_data.get("email"),
        phone_number=valid_customer_data.get("phone_number"),
        first_name=valid_customer_data.get("first_name"),
        last_name=valid_customer_data.get("last_name"),
        address=valid_address
    )
    assert customer_create_data.address == expected_outcome \
        , f"Address: {customer_create_data.address} does not match expected address: {expected_outcome}"


# INVALID TESTS FOR CustomerCreateResource

def test_create_customer_resource_does_not_work_without_setting_all_fields(valid_customer_data):
    with pytest.raises(ValidationError):
        CustomerCreateResource()

    with pytest.raises(ValidationError):
        CustomerCreateResource(email=valid_customer_data.get("email"))

    with pytest.raises(ValidationError):
        CustomerCreateResource(phone_number=valid_customer_data.get("phone_number"))

    with pytest.raises(ValidationError):
        CustomerCreateResource(first_name=valid_customer_data.get("first_name"))

    with pytest.raises(ValidationError):
        CustomerCreateResource(last_name=valid_customer_data.get("last_name"))

    with pytest.raises(ValidationError):
        CustomerCreateResource(address=valid_customer_data.get("address"))


@pytest.mark.parametrize("invalid_email, expecting_error_message", invalid_email_test_data)
def test_create_customer_resource_does_not_work_with_invalid_email(
        valid_customer_data, invalid_email, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=invalid_email,
            phone_number=valid_customer_data.get("phone_number"),
            first_name=valid_customer_data.get("first_name"),
            last_name=valid_customer_data.get("last_name"),
            address=valid_customer_data.get("address")
        ), f"Email: {invalid_email} should not be valid"


@pytest.mark.parametrize("invalid_phone_number, expecting_error_message", invalid_phone_number_test_data)
def test_create_customer_resource_does_not_work_with_invalid_phone_number_data(
        valid_customer_data, invalid_phone_number, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=valid_customer_data.get("email"),
            phone_number=invalid_phone_number,
            first_name=valid_customer_data.get("first_name"),
            last_name=valid_customer_data.get("last_name"),
            address=valid_customer_data.get("address")
        ), f"Phone number: {invalid_phone_number} should not be valid"


@pytest.mark.parametrize("invalid_first_name, expecting_error_message", invalid_first_name_test_data)
def test_create_customer_resource_does_not_work_with_invalid_first_name_data(
        valid_customer_data, invalid_first_name, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=valid_customer_data.get("email"),
            phone_number=valid_customer_data.get("phone_number"),
            first_name=invalid_first_name,
            last_name=valid_customer_data.get("last_name"),
            address=valid_customer_data.get("address")
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name, expecting_error_message", invalid_last_name_test_data)
def test_create_customer_resource_does_not_work_with_invalid_last_name_data(
        valid_customer_data, invalid_last_name, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=valid_customer_data.get("email"),
            phone_number=valid_customer_data.get("phone_number"),
            first_name=valid_customer_data.get("first_name"),
            last_name=invalid_last_name,
            address=valid_customer_data.get("address")
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_address, expecting_error_message", invalid_address_test_data)
def test_create_customer_resource_does_not_work_with_invalid_address_data(
        valid_customer_data, invalid_address, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=valid_customer_data.get("email"),
            phone_number=valid_customer_data.get("phone_number"),
            first_name=valid_customer_data.get("first_name"),
            last_name=valid_customer_data.get("last_name"),
            address=invalid_address
        ), f"Address: {invalid_address} should not be valid"


# VALID TESTS FOR CustomerUpdateResource

def test_update_customer_resource_works_without_setting_any_fields():
    customer_update_data = CustomerUpdateResource()
    updated_fields = customer_update_data.get_updated_fields()
    assert len(updated_fields) == 0, f"Updated fields should be empty, not {updated_fields}"


@pytest.mark.parametrize("valid_email, expected_outcome", valid_email_test_data)
def test_update_customer_resource_works_with_valid_email_data(
        valid_email, expected_outcome
):
    customer_update_data = CustomerUpdateResource(
        email=valid_email,
    )
    assert customer_update_data.email == expected_outcome \
        , (f"Email: {customer_update_data.email} does not match "
           f"expected email: {expected_outcome}")
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["email"] == customer_update_data.email \
        , (f"Email: {updated_fields['email']} does not match "
           f"updated customers email: {customer_update_data.email}")
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain email, not {updated_fields}"


@pytest.mark.parametrize("valid_phone_number, expected_outcome", valid_phone_number_test_data)
def test_update_customer_resource_works_with_valid_phone_number_data(
        valid_phone_number, expected_outcome
):
    customer_update_data = CustomerUpdateResource(
        phone_number=valid_phone_number,
    )
    assert customer_update_data.phone_number == expected_outcome \
        , (f"Phone number: {customer_update_data.phone_number} does not match "
           f"expected phone number: {expected_outcome}")
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["phone_number"] == customer_update_data.phone_number \
        , (f"Phone number: {updated_fields['phone_number']} does not match "
           f"updated customers phone number: {customer_update_data.phone_number}")
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain phone number, not {updated_fields}"


@pytest.mark.parametrize("valid_first_name, expected_outcome", valid_first_name_test_data)
def test_update_customer_resource_works_with_valid_first_name_data(
        valid_first_name, expected_outcome
):
    customer_update_data = CustomerUpdateResource(
        first_name=valid_first_name,
    )
    assert customer_update_data.first_name == expected_outcome \
        , (f"First name: {customer_update_data.first_name} does not match "
           f"expected first name: {expected_outcome}")
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["first_name"] == customer_update_data.first_name \
        , (f"First name: {updated_fields['first_name']} does not match "
           f"updated customers first name: {customer_update_data.first_name}")
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain first name, not {updated_fields}"


@pytest.mark.parametrize("valid_last_name, expected_outcome", valid_last_name_test_data)
def test_update_customer_resource_works_with_valid_last_name_data(
        valid_last_name, expected_outcome
):
    customer_update_data = CustomerUpdateResource(
        last_name=valid_last_name,
    )
    assert customer_update_data.last_name == expected_outcome \
        , f"Last name: {customer_update_data.last_name} does not match expected last name: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["last_name"] == customer_update_data.last_name \
        , (f"Last name: {updated_fields['last_name']} does not match "
           f"updated customers last name: {customer_update_data.last_name}")
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain last name, not {updated_fields}"


@pytest.mark.parametrize("valid_address, expected_outcome", valid_address_test_data)
def test_update_customer_resource_works_with_valid_address_data(
        valid_address, expected_outcome
):
    customer_update_data = CustomerUpdateResource(
        address=valid_address,
    )
    assert customer_update_data.address == expected_outcome \
        , f"Address: {customer_update_data.address} does not match expected address: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["address"] == customer_update_data.address \
        , f"Address: {updated_fields['address']} does not match updated customers address: {customer_update_data.address}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain address, not {updated_fields}"


# INVALID TESTS FOR CustomerUpdateResource

@pytest.mark.parametrize("invalid_email, expecting_error_message", invalid_email_test_data)
def test_update_customer_resource_does_not_work_with_invalid_email_data(
        invalid_email, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerUpdateResource(
            email=invalid_email
        ), f"Email: {invalid_email} should not be valid"


@pytest.mark.parametrize("invalid_phone_number, expecting_error_message", invalid_phone_number_test_data)
def test_update_customer_resource_does_not_work_with_invalid_phone_number_data(
        invalid_phone_number, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerUpdateResource(
            phone_number=invalid_phone_number
        ), f"Phone number: {invalid_phone_number} should not be valid"


@pytest.mark.parametrize("invalid_first_name, expecting_error_message", invalid_first_name_test_data)
def test_update_customer_resource_does_not_work_with_invalid_first_name_data(
        invalid_first_name, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerUpdateResource(
            first_name=invalid_first_name,
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name, expecting_error_message", invalid_last_name_test_data)
def test_update_customer_resource_does_not_work_with_invalid_last_name_data(
        invalid_last_name, expecting_error_message
):
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerUpdateResource(
            last_name=invalid_last_name
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_address, expecting_error_message", invalid_address_test_data)
def test_update_customer_resource_does_not_work_with_invalid_address_data(
        invalid_address, expecting_error_message
):
    with pytest.raises(ValidationError):
        CustomerCreateResource(
            address=invalid_address
        ), f"Address: {invalid_address} should not be valid"
