import pytest
from pydantic import ValidationError
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource

@pytest.mark.parametrize("email, phone_number, first_name, last_name, address, expected_outcome", [
    ("henrik@gmail.com", "10203040", "Henrik", "Henriksen", "Randomgade nr. 10 4. tv.",
     {
         "email": "henrik@gmail.com",
         "phone_number": "10203040",
         "first_name": "Henrik",
         "last_name": "Henriksen",
         "address": "Randomgade nr. 10 4. tv."
     }),
    ("henrik@gmail.co.uk", " 10203040 ", "hEnRiK", "hEnRiKsEn", " Randomgade nr. 10 4. tv. ",
     {
         "email": "henrik@gmail.co.uk",
         "phone_number": "10203040",
         "first_name": "Henrik",
         "last_name": "Henriksen",
         "address": "Randomgade nr. 10 4. tv."
     }),
    ("123henrik@gmail.com", None, " Henrik ", " Henriksen ", None,
     {
         "email": "123henrik@gmail.com",
         "phone_number": None,
         "first_name": "Henrik",
         "last_name": "Henriksen",
         "address": None
     }),
    (" henrik@gmail.com ", "01234567", "henrik", "henriksen", None,
     {
         "email": "henrik@gmail.com",
         "phone_number": "01234567",
         "first_name": "Henrik",
         "last_name": "Henriksen",
         "address": None
     }),
    ("a@b.c", "1234", "He", "He", "Rando",
     {
         "email": "a@b.c",
         "phone_number": "1234",
         "first_name": "He",
         "last_name": "He",
         "address": "Rando"
     }),
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
     "123456789012345678901234567890",
     "Maximilianaelizabethannamarialucreciavictoria",
     "Featherstonehaughworthingtonsmythenbishopsons",
     "12345678 Long Street Name That Goes On Forever And Ever, Apartment 6789, Some Really Long "
     "City Name That Never Ends, A Particularly Long State Name With Extra Letters, 99999-1234, "
     "Country With A Very Long Name That Might Just Fit In Perfectly Here As Well",
     {
         "email": "this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
         "phone_number": "123456789012345678901234567890",
         "first_name": "Maximilianaelizabethannamarialucreciavictoria",
         "last_name": "Featherstonehaughworthingtonsmythenbishopsons",
         "address": "12345678 Long Street Name That Goes On Forever And Ever, Apartment 6789, Some Really Long "
                    "City Name That Never Ends, A Particularly Long State Name With Extra Letters, 99999-1234, "
                    "Country With A Very Long Name That Might Just Fit In Perfectly Here As Well"
     }),
])
def test_create_customer_resource_works_with_valid_data(email, phone_number, first_name, last_name, address, expected_outcome):
    customer_create_data = CustomerCreateResource(
        email=email,
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name,
        address=address
    )
    assert customer_create_data.email == expected_outcome["email"] \
        , f"Email: {customer_create_data.email} does not match expected email: {expected_outcome['email']}"

    assert customer_create_data.phone_number == expected_outcome["phone_number"] \
        , f"Phone number: {customer_create_data.phone_number} does not match expected phone number: {expected_outcome['phone_number']}"

    assert customer_create_data.first_name == expected_outcome["first_name"] \
        , f"First name: {customer_create_data.first_name} does not match expected first name: {expected_outcome['first_name']}"

    assert customer_create_data.last_name == expected_outcome["last_name"] \
        , f"Last name: {customer_create_data.last_name} does not match expected last name: {expected_outcome['last_name']}"

    assert customer_create_data.address == expected_outcome["address"] \
        , f"Address: {customer_create_data.address} does not match expected address: {expected_outcome['address']}"


def test_create_customer_resource_does_not_work_without_setting_all_fields():
    with pytest.raises(ValidationError):
        CustomerCreateResource()
    with pytest.raises(ValidationError):
        CustomerCreateResource(email="henrik@gmail.com")
    with pytest.raises(ValidationError):
        CustomerCreateResource(phone_number="10203040")
    with pytest.raises(ValidationError):
        CustomerCreateResource(first_name="Henrik")
    with pytest.raises(ValidationError):
        CustomerCreateResource(last_name="Henriksen")
    with pytest.raises(ValidationError):
        CustomerCreateResource(address="Randomgade nr. 10 4. tv.")


@pytest.mark.parametrize("invalid_email", [
    None,
    "henrikgmail.com",
    "henrik@",
    "",
    "henrik@g mail.com",
    "henrik.gmail@com",
    123,
    "12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com"
])
def test_create_customer_resource_does_not_work_with_invalid_email(invalid_email):
    valid_phone_number = "10203040"
    valid_first_name = "Henrik"
    valid_last_name = "Henriksen"
    valid_address = "Randomgade nr. 10 4. tv."

    with pytest.raises(ValidationError):
        CustomerCreateResource(
            email=invalid_email,
            phone_number=valid_phone_number,
            first_name=valid_first_name,
            last_name=valid_last_name,
            address=valid_address
        ), f"Email: {invalid_email} should not be valid"


@pytest.mark.parametrize("invalid_phone_number", [
    "",
    " ",
    "1A2B3C4D",
    "1@2+3.4?",
    "102 3040",
    "123",
    "1234567890123456789012345678901",
    10203040
])
def test_create_customer_resource_does_not_work_with_invalid_phone_number(invalid_phone_number):
    valid_email = "henrik@gmail.com"
    valid_first_name = "Henrik"
    valid_last_name = "Henriksen"
    valid_address = "Randomgade nr. 10 4. tv."

    with pytest.raises(ValidationError):
        CustomerCreateResource(
            email=valid_email,
            phone_number=invalid_phone_number,
            first_name=valid_first_name,
            last_name=valid_last_name,
            address=valid_address
        ), f"Phone number: {invalid_phone_number} should not be valid"


@pytest.mark.parametrize("invalid_first_name", [
    None,
    "",
    "Henr1k",
    "H@nrik",
    "Hen rik",
    True,
    "H",
    "Maximilianaelizabethannamarialucreciavictorias"
])
def test_create_customer_resource_does_not_work_with_invalid_first_name(invalid_first_name):
    valid_email = "henrik@gmail.com"
    valid_phone_number = "10203040"
    valid_last_name = "Henriksen"
    valid_address = "Randomgade nr. 10 4. tv."

    with pytest.raises(ValidationError):
        CustomerCreateResource(
            email=valid_email,
            phone_number=valid_phone_number,
            first_name=invalid_first_name,
            last_name=valid_last_name,
            address=valid_address
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name", [
    None,
    "",
    "Henr1ksen",
    "H@nriksen",
    "Hen riksen",
    False,
    "H",
    "Featherstonehaughworthingtonsmythenbishopsonss"
])
def test_create_customer_resource_does_not_work_with_invalid_last_name(invalid_last_name):
    valid_email = "henrik@gmail.com"
    valid_phone_number = "10203040"
    valid_first_name = "Henrik"
    valid_address = "Randomgade nr. 10 4. tv."

    with pytest.raises(ValidationError):
        CustomerCreateResource(
            email=valid_email,
            phone_number=valid_phone_number,
            first_name=valid_first_name,
            last_name=invalid_last_name,
            address=valid_address
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_address", [
    "",
    " ",
    "Randomgade  nr. 10 4. tv.",
    "Randomgade   nr. 10 4. tv.",
    12345,
    "Rand",
    "123456789 Long Avenue Name That Extends For A Very Long Distance, "
    "Apartment 1010101, The Very Long City Name Which Seems Nearly Endless, "
    "Another Extended State Name, 678901-1234567, Country That Has An Extremely "
    "Lengthy Name That Goes On And On Without End"

])
def test_create_customer_resource_does_not_work_with_invalid_address(invalid_address):
    valid_email = "henrik@gmail.com"
    valid_phone_number = "10203040"
    valid_first_name = "Henrik"
    valid_last_name = "Henriksen"

    with pytest.raises(ValidationError):
        CustomerCreateResource(
            email=valid_email,
            phone_number=valid_phone_number,
            first_name=valid_first_name,
            last_name=valid_last_name,
            address=invalid_address
        ), f"Address: {invalid_address} should not be valid"

def test_update_customer_resource_works_without_setting_any_fields():
    customer_update_data = CustomerUpdateResource()
    updated_fields = customer_update_data.get_updated_fields()
    assert len(updated_fields) == 0, f"Updated fields should be empty, not {updated_fields}"


@pytest.mark.parametrize("email, expected_outcome", [
    ("henrik@gmail.com", "henrik@gmail.com"),
    ("henrik@gmail.co.uk", "henrik@gmail.co.uk"),
    ("123henrik@gmail.com", "123henrik@gmail.com"),
    (" henrik@gmail.com ", "henrik@gmail.com"),
    ("a@b.c", "a@b.c"),
    ("this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com",
     "this_is_a_valid_email_address_part@example-with-a-much-longer-subdomain-and-suffix.com"),
])
def test_update_customer_resource_works_with_valid_email_data(email, expected_outcome):
    customer_update_data = CustomerUpdateResource(
        email=email,
    )
    assert customer_update_data.email == expected_outcome \
        , f"Email: {customer_update_data.email} does not match expected email: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["email"] == customer_update_data.email \
        , f"Email: {updated_fields['email']} does not match updated customers email: {customer_update_data.email}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain email, not {updated_fields}"


@pytest.mark.parametrize("phone_number, expected_outcome", [
    ("10203040", "10203040"),
    (" 10203040 ", "10203040"),
    (None, None),
    ("01234567", "01234567"),
    ("1234", "1234"),
    ("123456789012345678901234567890", "123456789012345678901234567890"),
])
def test_update_customer_resource_works_with_valid_phone_number_data(phone_number, expected_outcome):
    customer_update_data = CustomerUpdateResource(
        phone_number=phone_number,
    )
    assert customer_update_data.phone_number == expected_outcome \
        , f"Phone number: {customer_update_data.phone_number} does not match expected phone number: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["phone_number"] == customer_update_data.phone_number \
        , f"Phone number: {updated_fields['phone_number']} does not match updated customers phone number: {customer_update_data.phone_number}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain phone number, not {updated_fields}"


@pytest.mark.parametrize("first_name, expected_outcome", [
    ("Henrik", "Henrik"),
    ("hEnRiK", "Henrik"),
    (" Henrik ", "Henrik"),
    ("henrik", "Henrik"),
    ("He", "He"),
    ("Maximilianaelizabethannamarialucreciavictoria", "Maximilianaelizabethannamarialucreciavictoria"),
])
def test_update_customer_resource_works_with_valid_first_name_data(first_name, expected_outcome):
    customer_update_data = CustomerUpdateResource(
        first_name=first_name,
    )
    assert customer_update_data.first_name == expected_outcome \
        , f"First name: {customer_update_data.first_name} does not match expected first name: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["first_name"] == customer_update_data.first_name \
        , f"First name: {updated_fields['first_name']} does not match updated customers first name: {customer_update_data.first_name}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain first name, not {updated_fields}"


@pytest.mark.parametrize("last_name, expected_outcome", [
    ("Henriksen", "Henriksen"),
    ("hEnRiKsEn", "Henriksen"),
    (" Henriksen ", "Henriksen"),
    ("henriksen", "Henriksen"),
    ("He", "He"),
    ("Featherstonehaughworthingtonsmythenbishopsons", "Featherstonehaughworthingtonsmythenbishopsons"),
])
def test_update_customer_resource_works_with_valid_last_name_data(last_name, expected_outcome):
    customer_update_data = CustomerUpdateResource(
        last_name=last_name,
    )
    assert customer_update_data.last_name == expected_outcome \
        , f"Last name: {customer_update_data.last_name} does not match expected last name: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["last_name"] == customer_update_data.last_name \
        , f"Last name: {updated_fields['last_name']} does not match updated customers last name: {customer_update_data.last_name}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain last name, not {updated_fields}"


@pytest.mark.parametrize("address, expected_outcome", [
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
])
def test_update_customer_resource_works_with_valid_address_data(address, expected_outcome):
    customer_update_data = CustomerUpdateResource(
        address=address,
    )
    assert customer_update_data.address == expected_outcome \
        , f"Address: {customer_update_data.address} does not match expected address: {expected_outcome}"
    updated_fields = customer_update_data.get_updated_fields()
    assert updated_fields["address"] == customer_update_data.address \
        , f"Address: {updated_fields['address']} does not match updated customers address: {customer_update_data.address}"
    assert len(updated_fields) == 1 \
        , f"Updated fields should only contain address, not {updated_fields}"


@pytest.mark.parametrize("invalid_email", [
    None,
    "henrikgmail.com",
    "henrik@",
    "",
    "henrik@g mail.com",
    "henrik.gmail@com",
    123,
    "12345678901234_this_is_an_invalid_email_address@example-with-a-much-too-long-subdomain-and-suffix.com"
])
def test_update_customer_resource_does_not_work_with_invalid_email(invalid_email):
    with pytest.raises(ValidationError):
        CustomerUpdateResource(
            email=invalid_email
        ), f"Email: {invalid_email} should not be valid"



@pytest.mark.parametrize("invalid_phone_number", [
    "",
    " ",
    "1A2B3C4D",
    "1@2+3.4?",
    "102 3040",
    "123",
    "1234567890123456789012345678901",
    10203040
])
def test_update_customer_resource_does_not_work_with_invalid_phone_number(invalid_phone_number):
    with pytest.raises(ValidationError):
        CustomerUpdateResource(
            phone_number=invalid_phone_number
        ), f"Phone number: {invalid_phone_number} should not be valid"


@pytest.mark.parametrize("invalid_first_name", [
    None,
    "",
    "Henr1k",
    "H@nrik",
    "Hen rik",
    True,
    "H",
    "Maximilianaelizabethannamarialucreciavictorias"
])
def test_update_customer_resource_does_not_work_with_invalid_first_name(invalid_first_name):
    with pytest.raises(ValidationError):
        CustomerUpdateResource(
            first_name=invalid_first_name,
        ), f"First name: {invalid_first_name} should not be valid"


@pytest.mark.parametrize("invalid_last_name", [
    None,
    "",
    "Henr1ksen",
    "H@nriksen",
    "Hen riksen",
    False,
    "H",
    "Featherstonehaughworthingtonsmythenbishopsonss"
])
def test_update_customer_resource_does_not_work_with_invalid_last_name(invalid_last_name):
    with pytest.raises(ValidationError):
        CustomerUpdateResource(
            last_name=invalid_last_name
        ), f"Last name: {invalid_last_name} should not be valid"


@pytest.mark.parametrize("invalid_address", [
    "",
    " ",
    "Randomgade  nr. 10 4. tv.",
    "Randomgade   nr. 10 4. tv.",
    12345,
    "Rand",
    "123456789 Long Avenue Name That Extends For A Very Long Distance, "
    "Apartment 1010101, The Very Long City Name Which Seems Nearly Endless, "
    "Another Extended State Name, 678901-1234567, Country That Has An Extremely "
    "Lengthy Name That Goes On And On Without End"

])
def test_update_customer_resource_does_not_work_with_invalid_address(invalid_address):
    with pytest.raises(ValidationError):
        CustomerCreateResource(
            address=invalid_address
        ), f"Address: {invalid_address} should not be valid"
