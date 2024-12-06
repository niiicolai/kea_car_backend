import pytest
from pydantic import ValidationError
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource

# VALID and INVALID test data for CustomerCreateResource and CustomerUpdateResource

valid_email_test_data = [
    ("henrik@gmail.com", "No Change"),
    ("henrik@gmail.co.uk", "No Change"),
    ("123henrik@gmail.com", "No Change"),
    (" henrik@gmail.com ", "henrik@gmail.com"),
    ("ab@cd.ef", "No Change"),  # Valid lower boundary
    ("ab@cd.efg", "No Change"),  # Valid lower boundary
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.co",
     "No Change"),  # Valid upper boundary
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
     "No Change"),  # Valid upper boundary
]

invalid_email_test_data = [
    (None, "Input should be a valid string"),
    ("henrikgmail.com", "is not a valid email address"),
    ("henrik@", "is not a valid email address"),
    ("henrik@g mail.com", "is not a valid email address"),
    ("henrik.gmail@com", "is not a valid email address"),
    (12345678, "Input should be a valid string"),
    (True, "Input should be a valid string"),
    ("ab@cd.e", "too short"),  # Invalid lower boundary
    ("12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com",
     "too long")  # Invalid upper boundary
]

valid_phone_number_test_data = [
    ("10203040", "No Change"),
    (" 10203040 ", "10203040"),
    (None, "No Change"),
    ("01234567", "No Change"),
    ("+4510203040", "No Change"),
    ("", None),
    (" ", None),
    ("12345678", "No Change"),  # Valid lower boundary
    ("123456789", "No Change"),  # Valid lower boundary
    ("123456789012345678901234567890", "No Change"),  # Valid upper boundary
    ("+45123456789012345678901234567", "No Change"),  # Valid upper boundary
]

invalid_phone_number_test_data = [
    ("1A2B3C4D", "can only contain digits"),
    ("1@20304?", "can only contain digits"),
    ("102 3040", "contains whitespace"),
    ("45+10203040", "can only contain digits after the +"),
    ("+45+10203040", "can only contain digits after the +"),
    ("+4510@03040", "can only contain digits"),
    ("+451020304", "is too short"),
    (10203040, "Input should be a valid string"),
    ("1234567", "is too short"),  # Invalid lower boundary
    ("+451234567890123456789012345678", "is too long"),  # Invalid upper boundary

]

valid_first_name_test_data = [
    ("Henrik", "No Change"),
    ("Henrik Henry", "No Change"),
    ("hEnRiK", "Henrik"),
    ("hEnRiK hEnRy", "Henrik Henry"),
    ("Henrik-Henry", "No Change"),
    ("hEnRik-hEnRy", "Henrik-Henry"),
    (" Henrik ", "Henrik"),
    (" Henrik-Henry ", "Henrik-Henry"),
    (" Henrik-Henry ", "Henrik-Henry"),
    ("henrik", "Henrik"),
    ("henrik henry", "Henrik Henry"),
    ("henrik-henry", "Henrik-Henry"),
    ("H", "No Change"),  # Valid lower boundary
    ("He", "No Change"),  # Valid lower boundary
    ("Maximilian Elizabeth Anna-Maria Lucre-Victor",  # Valid upper boundary
     "No Change"),
    ("Maximilian Elizabeth Anna-Maria Lucre-Victori",  # Valid upper boundary
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
    ("Maximilian Elizabeth Anna-Maria Lucre-Victoria", "is too long"),  # Invalid upper boundary
]

valid_last_name_test_data = [
    ("Henriksen", "No Change"),
    (" Henriksen ", "Henriksen"),
    ("henriksen", "Henriksen"),
    ("hEnRiKsEn", "Henriksen"),
    ("Henderson-Henriksen", "No Change"),
    ("hEnDeRsOn-hEnRiKsEn", "Henderson-Henriksen"),
    ("henderson-henriksen", "Henderson-Henriksen"),
    ("H", "No Change"),  # Valid lower boundary
    ("He", "No Change"),  # Valid lower boundary
    ("Featherstonehaughworthingtonsmythenbishopson", "No Change"),  # Valid upper boundary
    ("Featherstonehaughworthingtonsmythenbishopsons", "No Change"),  # Valid upper boundary
]

invalid_last_name_test_data = [
    (None, "Input should be a valid string"),
    ("Henderson Henriksen", "contains whitespace"),
    ("-Henriksen", "starts or ends with a hyphen"),
    ("Henriksen-", "starts or ends with a hyphen"),
    ("Henr1ksen", "can only contain alphabetic characters"),
    ("H@nriksen", "can only contain alphabetic characters"),
    (True, "Input should be a valid string"),
    (1234, "Input should be a valid string"),
    ("", "is too short"),  # Invalid lower boundary
    ("Featherstonehaughworthingtonsmythenbishopsonss", "is too long"),  # Invalid upper boundary
]

valid_address_test_data = [
    ("Randomgade nr. 10 4. tv.", "No Change"),
    (" Randomgade nr. 10 4. tv. ", "Randomgade nr. 10 4. tv."),
    ("", None),
    (" ", None),
    (None, "No Change"),
    ("Rando", "No Change"),  # Valid lower boundary
    ("Random", "No Change"),  # Valid lower boundary
    ("1234567 Long Street Name That Goes On Forever And Ever, Apartment 6789, "
     "Some Really Long City Name That Never Ends, A Particularly Long State "
     "Name With Extra Letters, 99999-1234, Country With A Very Long Name That "
     "Might Just Fit In Perfectly Here As Well",
     "No Change"),  # Valid upper boundary
    ("12345678 Long Street Name That Goes On Forever And Ever, Apartment 6789, "
     "Some Really Long City Name That Never Ends, A Particularly Long State "
     "Name With Extra Letters, 99999-1234, Country With A Very Long Name That "
     "Might Just Fit In Perfectly Here As Well",
     "No Change"),  # Valid upper boundary
]

invalid_address_test_data = [
    ("Randomgade  nr. 10 4. tv.", "contains extra whitespace"),
    ("Randomgade   nr. 10 4. tv.", "contains extra whitespace"),
    (True, "Input should be a valid string"),
    (12345, "Input should be a valid string"),
    ("Rand", "is too short"),  # Invalid lower boundary
    ("123456789 Long Avenue Name That Extends For A Very Long Distance, "
     "Apartment 1010101, The Very Long City Name Which Seems Nearly Endless, "
     "Another Extended State Name, 678901-1234567, Country That Has An Extremely "
     "Lengthy Name That Goes On And On Without End",
     "is too long"),  # Invalid upper boundary
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
    valid_customer_data.pop("email")
    customer_create_data = CustomerCreateResource(
        email=valid_email,
        **valid_customer_data
    )
    expected_email = valid_email if expected_outcome == "No Change" else expected_outcome
    assert customer_create_data.email == expected_email \
        , (f"Email: {customer_create_data.email} "
           f"does not match expected email: {expected_email}")


@pytest.mark.parametrize("valid_phone_number, expected_outcome", valid_phone_number_test_data)
def test_create_customer_resource_works_with_valid_phone_number_data(
        valid_customer_data, valid_phone_number, expected_outcome
):
    valid_customer_data.pop("phone_number")
    customer_create_data = CustomerCreateResource(
        phone_number=valid_phone_number,
        **valid_customer_data
    )
    expected_phone_number = valid_phone_number if expected_outcome == "No Change" else expected_outcome
    assert customer_create_data.phone_number == expected_phone_number \
        , (f"Phone number: {customer_create_data.phone_number} "
           f"does not match expected phone number: {expected_phone_number}")


@pytest.mark.parametrize("valid_first_name, expected_outcome", valid_first_name_test_data)
def test_create_customer_resource_works_with_valid_first_name_data(
        valid_customer_data, valid_first_name, expected_outcome
):
    valid_customer_data.pop("first_name")
    customer_create_data = CustomerCreateResource(
        first_name=valid_first_name,
        **valid_customer_data
    )
    expected_first_name = valid_first_name if expected_outcome == "No Change" else expected_outcome
    assert customer_create_data.first_name == expected_first_name \
        , (f"First name: {customer_create_data.first_name} does not match "
           f"expected first name: {expected_first_name}")


@pytest.mark.parametrize("valid_last_name, expected_outcome", valid_last_name_test_data)
def test_create_customer_resource_works_with_valid_last_name_data(
        valid_customer_data, valid_last_name, expected_outcome
):
    valid_customer_data.pop("last_name")
    customer_create_data = CustomerCreateResource(
        last_name=valid_last_name,
        **valid_customer_data
    )
    expected_last_name = valid_last_name if expected_outcome == "No Change" else expected_outcome
    assert customer_create_data.last_name == expected_last_name \
        , (f"Last name: {customer_create_data.last_name} does not match "
           f"expected last name: {expected_last_name}")


@pytest.mark.parametrize("valid_address, expected_outcome", valid_address_test_data)
def test_create_customer_resource_works_with_valid_address_data(
        valid_customer_data, valid_address, expected_outcome
):
    valid_customer_data.pop("address")
    customer_create_data = CustomerCreateResource(
        address=valid_address,
        **valid_customer_data
    )
    expected_address = valid_address if expected_outcome == "No Change" else expected_outcome
    assert customer_create_data.address == expected_address \
        , f"Address: {customer_create_data.address} does not match expected address: {expected_address}"


# INVALID TESTS FOR CustomerCreateResource

@pytest.mark.parametrize("missing_field",
                         ["all_fields", "email", "phone_number", "first_name", "last_name", "address"])
def test_create_customer_resource_does_not_work_without_setting_all_fields(valid_customer_data, missing_field):
    if missing_field == "all_fields":
        with pytest.raises(ValidationError, match="Field required"):
            CustomerCreateResource(), "All fields should be required"
    else:
        valid_customer_data.pop(missing_field)
        with pytest.raises(ValidationError, match=f"{missing_field}\n  Field required"):
            CustomerCreateResource(
                **valid_customer_data
            ), f"{missing_field} should be required"


@pytest.mark.parametrize("invalid_email, expecting_error_message", invalid_email_test_data)
def test_create_customer_resource_does_not_work_with_invalid_email(
        valid_customer_data, invalid_email, expecting_error_message
):
    valid_customer_data.pop("email")
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            email=invalid_email,
            **valid_customer_data
        ), f"Email: {invalid_email} should not be valid"


@pytest.mark.parametrize("invalid_phone_number, expecting_error_message", invalid_phone_number_test_data)
def test_create_customer_resource_does_not_work_with_invalid_phone_number_data(
        valid_customer_data, invalid_phone_number, expecting_error_message
):
    valid_customer_data.pop("phone_number")
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            phone_number=invalid_phone_number,
            **valid_customer_data
        ), f"Phone number: {invalid_phone_number} should not be valid"


@pytest.mark.parametrize("invalid_first_name, expecting_error_message", invalid_first_name_test_data)
def test_create_customer_resource_does_not_work_with_invalid_first_name_data(
        valid_customer_data, invalid_first_name, expecting_error_message
):
    valid_customer_data.pop("first_name")
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            first_name=invalid_first_name,
            **valid_customer_data
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name, expecting_error_message", invalid_last_name_test_data)
def test_create_customer_resource_does_not_work_with_invalid_last_name_data(
        valid_customer_data, invalid_last_name, expecting_error_message
):
    valid_customer_data.pop("last_name")
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            last_name=invalid_last_name,
            **valid_customer_data
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_address, expecting_error_message", invalid_address_test_data)
def test_create_customer_resource_does_not_work_with_invalid_address_data(
        valid_customer_data, invalid_address, expecting_error_message
):
    valid_customer_data.pop("address")
    with pytest.raises(ValidationError, match=expecting_error_message):
        CustomerCreateResource(
            address=invalid_address,
            **valid_customer_data
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
    expected_email = valid_email if expected_outcome == "No Change" else expected_outcome
    assert customer_update_data.email == expected_email \
        , (f"Email: {customer_update_data.email} does not match "
           f"expected email: {expected_email}")
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields.get('email') == customer_update_data.email \
        , (f"Email: {updated_fields.get('email')} does not match "
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
    expected_phone_number = valid_phone_number if expected_outcome == "No Change" else expected_outcome
    assert customer_update_data.phone_number == expected_phone_number \
        , (f"Phone number: {customer_update_data.phone_number} does not match "
           f"expected phone number: {expected_phone_number}")
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
    expected_first_name = valid_first_name if expected_outcome == "No Change" else expected_outcome
    assert customer_update_data.first_name == expected_first_name \
        , (f"First name: {customer_update_data.first_name} does not match "
           f"expected first name: {expected_first_name}")
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
    expected_last_name = valid_last_name if expected_outcome == "No Change" else expected_outcome
    assert customer_update_data.last_name == expected_last_name \
        , f"Last name: {customer_update_data.last_name} does not match expected last name: {expected_last_name}"
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
    expected_address = valid_address if expected_outcome == "No Change" else expected_outcome
    assert customer_update_data.address == expected_address \
        , f"Address: {customer_update_data.address} does not match expected address: {expected_address}"
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
