from typing import Optional
import pytest
from app.services import customers_service
from app.exceptions.database_errors import (
    UnableToFindIdError,
    AlreadyTakenFieldValueError
)
from app.resources.customer_resource import (
    CustomerCreateResource,
    CustomerUpdateResource,
    CustomerReturnResource
)

amount_of_expected_customers = 5
amount_of_expected_cars = 4
amount_of_expected_purchases = 1


def prepare_customer_data(
        customer_data: dict,
        customer_resource: Optional[CustomerReturnResource] = None
) -> tuple[dict, list, str]:
    customer_data = customer_data.copy()
    customer_keys = customer_data.keys()
    if 'amount_of_cars' in customer_keys:
        customer_data.pop('amount_of_cars')
    if 'amount_of_purchased_cars' in customer_keys:
        customer_data.pop('amount_of_purchased_cars')
    if 'car_ids' in customer_keys:
        customer_data.pop('car_ids')
    customer_id = ""
    if 'id' in customer_keys:
        customer_id = customer_data.pop('id')
    if isinstance(customer_resource, CustomerReturnResource) and customer_resource is not None:
        customer_id = customer_resource.id
    customer_fields = list(customer_data.keys())

    return customer_data, customer_fields, customer_id


customer_henrik = {
    "id": "0ac1d668-55aa-46a1-898a-8fa61457facb",
    "email": "henrik@gmail.com",
    "phone_number": "10203040",
    "first_name": "Henrik",
    "last_name": "Henriksen",
    "address": "Randomgade nr. 10 4. tv.",
    "amount_of_cars": 1,
    "amount_of_purchased_cars": 1,
    "car_ids": ["bdfca7c4-e0ad-4618-8766-9bb355371c81"]
}

customer_oliver = {
    "id": "bbbb06bc-268d-4f88-8b8e-3da4df118328",
    "email": "oli@oli.dk",
    "phone_number": "12345678",
    "first_name": "Oliver",
    "last_name": "Jorgensen",
    "address": "asdasd123",
    "amount_of_cars": 0,
    "amount_of_purchased_cars": 0
}

customer_tom = {
    "id": "daf830ad-be98-4f95-8fa8-3dc7efa540fe",
    "email": "tom@gmail.com",
    "phone_number": "12345678",
    "first_name": "Tom",
    "last_name": "Tomsen",
    "address": "Test 21",
    "amount_of_cars": 0,
    "amount_of_purchased_cars": 0
}

customer_james = {
    "id": "f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc",
    "email": "james@gmail.com",
    "phone_number": "12345678",
    "first_name": "James",
    "last_name": "Jamesen",
    "address": "Test 21",
    "amount_of_cars": 3,
    "amount_of_purchased_cars": 0,
    "car_ids":
        ["0be86135-c58f-43b6-a369-a3c5445b9948",
         "a1b1e305-1a89-4b06-86d1-21ac1fa3c8a6",
         "a5503fbb-c388-4789-a10c-d7ae7bdf7408"]
}

customer_test = {
    "id": "fc40f99e-13f0-460d-b79d-f75206acdd07",
    "email": "test@test.dk",
    "phone_number": "12345678",
    "first_name": "Test",
    "last_name": "Teste",
    "address": "Test 21",
    "amount_of_cars": 0,
    "amount_of_purchased_cars": 0
}


# VALID TESTS FOR get_customer_by_id

@pytest.mark.parametrize("expected_customer", [
    customer_henrik,
    customer_oliver,
    customer_tom,
    customer_james,
    customer_test,
])
def test_get_customer_by_id_with_valid_partitions(
        mySQLCustomerRepository, expected_customer
):
    expected_customer_data, customer_fields, expected_customer_id = prepare_customer_data(expected_customer)

    customer = customers_service.get_by_id(
        repository=mySQLCustomerRepository,
        customer_id=expected_customer_id
    )
    assert isinstance(customer, CustomerReturnResource), \
        (f"Customer is not of type CustomerReturnResource, "
         f"but {type(customer).__name__}")

    assert customer.id == expected_customer_id, \
        (f"Customer ID {customer.id} does not match "
         f"expected customer ID {expected_customer_id}")

    for field in customer_fields:
        assert getattr(customer, field) == expected_customer_data.get(field), \
            (f"Customer {field}: {getattr(customer, field)} does not match "
             f"the expected data: {expected_customer_data.get(field)}")


# INVALID TESTS FOR get_customer_by_id

@pytest.mark.parametrize("invalid_customer_id, expected_error, expecting_error_message", [
    (None, TypeError, "customer_id must be of type str, not NoneType."),
    (True, TypeError, "customer_id must be of type str, not bool."),
    (1, TypeError, "customer_id must be of type str, not int."),
    ("unknown-id", UnableToFindIdError, "Customer with ID: unknown-id does not exist."),
])
def test_get_customer_by_id_with_invalid_customer_id_partitions(
        mySQLCustomerRepository, invalid_customer_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        customers_service.get_by_id(
            repository=mySQLCustomerRepository,
            customer_id=invalid_customer_id
        )


@pytest.mark.parametrize("invalid_customer_repository, expecting_error_message", [
    (None, "repository must be of type CustomerRepository, not NoneType."),
    (1, "repository must be of type CustomerRepository, not int."),
    ("repository", "repository must be of type CustomerRepository, not str."),
])
def test_get_customer_by_id_with_invalid_repository_type_partitions(invalid_customer_repository,
                                                                    expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.get_by_id(
            repository=invalid_customer_repository,
            customer_id=customer_test.get('id')
        )


def test_get_customer_by_id_with_invalid_repository_types_partitions(
        mySQLColorRepository, mySQLCarRepository, mySQLPurchaseRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLColorRepository).__name__}."
                       ):
        customers_service.get_by_id(
            repository=mySQLColorRepository,
            customer_id=customer_test.get('id')
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLCarRepository).__name__}."
                       ):
        customers_service.get_by_id(
            repository=mySQLCarRepository,
            customer_id=customer_test.get('id')
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLPurchaseRepository).__name__}."
                       ):
        customers_service.get_by_id(
            repository=mySQLPurchaseRepository,
            customer_id=customer_test.get('id')
        )


# VALID TESTS FOR get_all_customers


def test_get_all_customers_with_valid_partitions(mySQLCustomerRepository):
    expected_customers = [
        customer_henrik,
        customer_oliver,
        customer_tom,
        customer_james,
        customer_test,
    ]

    customers = customers_service.get_all(repository=mySQLCustomerRepository)

    assert isinstance(customers, list) and all(isinstance(customer, CustomerReturnResource) for customer in customers) \
        , (f"Customers are not a list of CustomerReturnResource objects, "
           f"but {type(customers).__name__}")

    assert len(customers) == amount_of_expected_customers, \
        (f"Amount of customers {len(customers)} does not match "
         f"{amount_of_expected_customers}")

    for customer in customers:
        assert isinstance(customer, CustomerReturnResource), \
            (f"Customer is not of type CustomerReturnResource, "
             f"but {type(customer).__name__}")

        assert customer.id in [expected_customer.get('id') for expected_customer in expected_customers], \
            f"Customer ID {customer.id} does not match any of the expected IDs."


@pytest.mark.parametrize("valid_customers_limit, expecting_customer_amount", [
    (-1, amount_of_expected_customers),
    (None, amount_of_expected_customers),
    (0, amount_of_expected_customers),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, amount_of_expected_customers),
])
def test_get_all_customers_with_valid_customers_limit_values_partitions(
        mySQLCustomerRepository, valid_customers_limit, expecting_customer_amount
):
    customers = customers_service.get_all(
        repository=mySQLCustomerRepository,
        customers_limit=valid_customers_limit
    )

    assert isinstance(customers, list) and all(isinstance(customer, CustomerReturnResource) for customer in customers) \
        , f"Customers are not a list of CustomerReturnResource objects, but {type(customers).__name__}"

    assert len(customers) == expecting_customer_amount \
        , (f"There should be {expecting_customer_amount} customers, "
           f"not '{len(customers)}'")


@pytest.mark.parametrize("valid_email_filter, expecting_customers", [
    (None, [customer_henrik,
            customer_oliver,
            customer_tom,
            customer_james,
            customer_test]),
    ("", [customer_henrik,
          customer_oliver,
          customer_tom,
          customer_james,
          customer_test]),
    ("@", [customer_henrik,
           customer_oliver,
           customer_tom,
           customer_james,
           customer_test]),
    ("henrik", [customer_henrik]),
    ("gmail", [customer_henrik,
               customer_tom,
               customer_james]),
    (".dk", [customer_oliver,
             customer_test]),
    (" ", []),
    ("unknown-email", []),
])
def test_get_all_customers_with_valid_email_filter_values_partitions(
        mySQLCustomerRepository, valid_email_filter, expecting_customers
):
    customers = customers_service.get_all(
        repository=mySQLCustomerRepository,
        filter_customer_by_email=valid_email_filter
    )

    assert isinstance(customers, list) and all(isinstance(customer, CustomerReturnResource) for customer in customers) \
        , f"Customers are not a list of CustomerReturnResource objects, but {type(customers).__name__}"

    assert len(customers) == len(expecting_customers) \
        , (f"There should be {len(expecting_customers)} customers, "
           f"not '{len(customers)}'")

    for customer in customers:
        assert customer.id in [expected_customer.get('id') for expected_customer in expecting_customers], \
            f"Customer ID {customer.id} does not match any of the expected IDs."

        if valid_email_filter is not None:
            assert valid_email_filter in customer.email, \
                f"Email filter '{valid_email_filter}' is not in customer email '{customer.email}'."


@pytest.mark.parametrize("valid_email_filter, valid_customers_limit, expecting_customer_amount", [
    (None, -1, amount_of_expected_customers),
    (None, None, amount_of_expected_customers),
    (None, 0, amount_of_expected_customers),
    (None, 1, 1),
    (None, 3, 3),
    (None, 5, amount_of_expected_customers),
    (None, 6, amount_of_expected_customers),
    ("", -1, amount_of_expected_customers),
    ("", None, amount_of_expected_customers),
    ("", 0, amount_of_expected_customers),
    ("", 1, 1),
    ("", 3, 3),
    ("", 5, amount_of_expected_customers),
    ("", 6, amount_of_expected_customers),
    ("@", -1, amount_of_expected_customers),
    ("@", None, amount_of_expected_customers),
    ("@", 0, amount_of_expected_customers),
    ("@", 1, 1),
    ("@", 3, 3),
    ("@", 5, amount_of_expected_customers),
    ("@", 6, amount_of_expected_customers),
    ("henrik", -1, 1),
    ("henrik", None, 1),
    ("henrik", 0, 1),
    ("henrik", 1, 1),
    ("henrik", 3, 1),
    ("henrik", 5, 1),
    ("henrik", 6, 1),
    ("gmail", -1, 3),
    ("gmail", None, 3),
    ("gmail", 0, 3),
    ("gmail", 1, 1),
    ("gmail", 3, 3),
    ("gmail", 5, 3),
    ("gmail", 6, 3),
    (".dk", -1, 2),
    (".dk", None, 2),
    (".dk", 0, 2),
    (".dk", 1, 1),
    (".dk", 3, 2),
    (".dk", 5, 2),
    (".dk", 6, 2),
    (" ", -1, 0),
    (" ", None, 0),
    (" ", 0, 0),
    (" ", 1, 0),
    (" ", 3, 0),
    (" ", 5, 0),
    (" ", 6, 0),
    ("unknown-email", -1, 0),
    ("unknown-email", None, 0),
    ("unknown-email", 0, 0),
    ("unknown-email", 1, 0),
    ("unknown-email", 3, 0),
    ("unknown-email", 5, 0),
    ("unknown-email", 6, 0),
])
def test_get_all_customers_with_valid_email_filter_and_customers_limit_values_partitions(
        mySQLCustomerRepository, valid_email_filter, valid_customers_limit, expecting_customer_amount
):
    customers = customers_service.get_all(
        repository=mySQLCustomerRepository,
        filter_customer_by_email=valid_email_filter,
        customers_limit=valid_customers_limit
    )

    assert isinstance(customers, list) and all(isinstance(customer, CustomerReturnResource) for customer in customers) \
        , f"Customers are not a list of CustomerReturnResource objects, but {type(customers).__name__}"

    assert len(customers) == expecting_customer_amount \
        , (f"There should be {expecting_customer_amount} customers, "
           f"not '{len(customers)}'")

    for customer in customers:
        if valid_email_filter is not None:
            assert valid_email_filter in customer.email, \
                f"Email filter '{valid_email_filter}' is not in customer email '{customer.email}'."


# INVALID TESTS FOR get_all_customers

@pytest.mark.parametrize("invalid_customers_limit, expecting_error_message", [
    ("1", "customers_limit must be of type int or None, not str."),
    (True, "customers_limit must be of type int or None, not bool."),
    (1.5, "customers_limit must be of type int or None, not float."),
])
def test_get_all_customers_with_invalid_customers_limit_values_partitions(
        mySQLCustomerRepository, invalid_customers_limit, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.get_all(
            repository=mySQLCustomerRepository,
            customers_limit=invalid_customers_limit
        )


@pytest.mark.parametrize("invalid_email_filter, expecting_error_message", [
    (1, "filter_customer_by_email must be of type str or None, not int."),
    (True, "filter_customer_by_email must be of type str or None, not bool."),
    (1.5, "filter_customer_by_email must be of type str or None, not float."),
])
def test_get_all_customers_with_invalid_email_filter_values_partitions(
        mySQLCustomerRepository, invalid_email_filter, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.get_all(
            repository=mySQLCustomerRepository,
            filter_customer_by_email=invalid_email_filter
        )


@pytest.mark.parametrize("invalid_repository, expecting_error_message", [
    (None, "repository must be of type CustomerRepository, not NoneType."),
    (1, "repository must be of type CustomerRepository, not int."),
    (True, "repository must be of type CustomerRepository, not bool."),
    ("customer_repository", "repository must be of type CustomerRepository, not str."),
])
def test_get_all_customers_with_invalid_repository_type_partitions(
        invalid_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.get_all(
            repository=invalid_repository
        )


def test_get_all_customers_with_invalid_repository_types_partitions(
        mySQLColorRepository, mySQLCarRepository, mySQLPurchaseRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLColorRepository).__name__}."
                       ):
        customers_service.get_all(
            repository=mySQLColorRepository
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLCarRepository).__name__}."
                       ):
        customers_service.get_all(
            repository=mySQLCarRepository
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLPurchaseRepository).__name__}."
                       ):
        customers_service.get_all(
            repository=mySQLPurchaseRepository
        )


# VALID TESTS FOR create_customer

def test_create_customer_with_valid_partitions(mySQLCustomerRepository, valid_customer_data):
    amount_of_customers_before_creation = len(mySQLCustomerRepository.get_all())

    created_customer = customers_service.create(
        repository=mySQLCustomerRepository,
        customer_create_data=CustomerCreateResource(**valid_customer_data)
    )

    expected_amount_of_customers_after_creation = amount_of_customers_before_creation + 1
    actual_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())

    assert isinstance(created_customer, CustomerReturnResource), \
        (f"Customer is not of type CustomerReturnResource, "
         f"but {type(created_customer).__name__}")

    expected_customer_data, customer_fields, expected_customer_id = prepare_customer_data(
        valid_customer_data, created_customer
    )

    assert mySQLCustomerRepository.get_by_id(expected_customer_id) is not None, \
        f"Customer with ID {expected_customer_id} was not created."

    assert actual_amount_of_customers_after_creation == expected_amount_of_customers_after_creation, \
        (f"Amount of customers after creation {actual_amount_of_customers_after_creation} does not match "
         f"the expected amount of customers after creation {expected_amount_of_customers_after_creation}")

    for customer_field in customer_fields:
        assert getattr(created_customer, customer_field) == expected_customer_data.get(customer_field), \
            (f"Customer {customer_field}: {getattr(created_customer, customer_field)} does not match "
             f"the expected data: {expected_customer_data.get(customer_field)}")


# INVALID TESTS FOR create_customer

@pytest.mark.parametrize("invalid_customer_create_data, expected_error, expecting_error_message", [
    (None, TypeError, "customer_create_data must be of type CustomerCreateResource, not NoneType."),
    (1, TypeError, "customer_create_data must be of type CustomerCreateResource, not int."),
    (True, TypeError, "customer_create_data must be of type CustomerCreateResource, not bool."),
    ("customer_data", TypeError, "customer_create_data must be of type CustomerCreateResource, not str."),
    (CustomerUpdateResource(), TypeError, f"customer_create_data must be of type CustomerCreateResource, "
                                          f"not {type(CustomerUpdateResource()).__name__}."),
    ({}, TypeError, "customer_create_data must be of type CustomerCreateResource, not dict."),
    ({"email": customer_test.get('email')}, AlreadyTakenFieldValueError,
     f"email: {customer_test.get('email')} is already taken."),
    ({"email": customer_henrik.get('email')}, AlreadyTakenFieldValueError,
     f"email: {customer_henrik.get('email')} is already taken."),
])
def test_create_customer_with_invalid_customer_create_data_partitions(
        mySQLCustomerRepository, valid_customer_data, invalid_customer_create_data, expected_error,
        expecting_error_message
):
    expected_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    if isinstance(invalid_customer_create_data, dict) and invalid_customer_create_data.get('email') is not None:
        valid_customer_data['email'] = invalid_customer_create_data.get('email')
        invalid_customer_create_data = CustomerCreateResource(**valid_customer_data)

    with pytest.raises(expected_error, match=expecting_error_message):
        customers_service.create(
            repository=mySQLCustomerRepository,
            customer_create_data=invalid_customer_create_data
        )

    actual_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_creation == expected_amount_of_customers_after_creation, \
        (f"Amount of customers after creation {actual_amount_of_customers_after_creation} does not match "
         f"the expected amount of customers after creation {expected_amount_of_customers_after_creation}")


@pytest.mark.parametrize("invalid_repository, expecting_error_message", [
    (None, "repository must be of type CustomerRepository, not NoneType."),
    (1, "repository must be of type CustomerRepository, not int."),
    (True, "repository must be of type CustomerRepository, not bool."),
    ("customer_repository", "repository must be of type CustomerRepository, not str."),
])
def test_create_customer_with_invalid_repository_type_partitions(
        mySQLCustomerRepository, valid_customer_data, invalid_repository, expecting_error_message
):
    expected_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.create(
            repository=invalid_repository,
            customer_create_data=CustomerCreateResource(**valid_customer_data)
        )

    actual_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_creation == expected_amount_of_customers_after_creation, \
        (f"Amount of customers after creation {actual_amount_of_customers_after_creation} does not match "
         f"the expected amount of customers after creation {expected_amount_of_customers_after_creation}")


def test_create_customer_with_invalid_repository_types_partitions(
        mySQLCustomerRepository, mySQLColorRepository, mySQLCarRepository, mySQLPurchaseRepository, valid_customer_data
):
    expected_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLColorRepository).__name__}."
                       ):
        customers_service.create(
            repository=mySQLColorRepository,
            customer_create_data=CustomerCreateResource(**valid_customer_data)
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLCarRepository).__name__}."
                       ):
        customers_service.create(
            repository=mySQLCarRepository,
            customer_create_data=CustomerCreateResource(**valid_customer_data)
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLPurchaseRepository).__name__}."
                       ):
        customers_service.create(
            repository=mySQLPurchaseRepository,
            customer_create_data=CustomerCreateResource(**valid_customer_data)
        )

    actual_amount_of_customers_after_creation = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_creation == expected_amount_of_customers_after_creation, \
        (f"Amount of customers after creation {actual_amount_of_customers_after_creation} does not match "
         f"the expected amount of customers after creation {expected_amount_of_customers_after_creation}")


# VALID TESTS FOR update_customer

@pytest.mark.parametrize("customer_to_update", [
    customer_henrik,
    customer_oliver,
    customer_tom,
    customer_james,
    customer_test,
])
def test_update_customer_with_valid_partitions(
        mySQLCustomerRepository, valid_customer_data, customer_to_update
):
    customer_to_update, updated_customer_fields, customer_to_update_id = (
        prepare_customer_data(customer_to_update)
    )

    valid_customer_update_create_data = CustomerUpdateResource(**customer_to_update)
    updated_customer = customers_service.update(
        repository=mySQLCustomerRepository,
        customer_id=customer_to_update_id,
        customer_update_data=valid_customer_update_create_data
    )

    assert isinstance(updated_customer, CustomerReturnResource), \
        (f"Customer is not of type CustomerReturnResource, "
         f"but {type(updated_customer).__name__}")

    assert updated_customer.id == customer_to_update_id, \
        (f"Updated customer ID {updated_customer.id} does not match "
         f"the expected ID {customer_to_update_id}")

    for updated_customer_field in updated_customer_fields:
        actual_updated_customer_field_data = getattr(updated_customer, updated_customer_field)
        expected_updated_customer_field_data = customer_to_update.get(updated_customer_field)
        not_expected_updated_customer_field_data = valid_customer_data.get(updated_customer_field)
        assert actual_updated_customer_field_data != not_expected_updated_customer_field_data, \
            (f"Updated customer {updated_customer_field}: {actual_updated_customer_field_data} "
             f"is still the same as before update {not_expected_updated_customer_field_data}")
        assert actual_updated_customer_field_data == expected_updated_customer_field_data, \
            (f"Updated customer {updated_customer_field}: {actual_updated_customer_field_data} does not match "
             f"the expected update data {expected_updated_customer_field_data}")


@pytest.mark.parametrize("customer_to_update", [
    customer_henrik,
    customer_oliver,
    customer_tom,
    customer_james,
    customer_test,
])
def test_update_customer_email_to_their_own_email_with_valid_partitions(
        mySQLCustomerRepository, customer_to_update
):
    customer_to_update, updated_customer_fields, customer_to_update_id = (
        prepare_customer_data(customer_to_update)
    )

    valid_customer_update_create_data = CustomerUpdateResource(email=customer_to_update.get('email'))
    updated_customer = customers_service.update(
        repository=mySQLCustomerRepository,
        customer_id=customer_to_update_id,
        customer_update_data=valid_customer_update_create_data
    )

    assert isinstance(updated_customer, CustomerReturnResource), \
        (f"Customer is not of type CustomerReturnResource, "
         f"but {type(updated_customer).__name__}")

    assert updated_customer.id == customer_to_update_id, \
        (f"Updated customer ID {updated_customer.id} does not match "
         f"the expected ID {customer_to_update_id}")

    assert updated_customer.email == customer_to_update.get('email'), \
        (f"Updated customer email {updated_customer.email} does not match "
         f"the expected email {customer_to_update.get('email')}")


# INVALID TESTS FOR update_customer

@pytest.mark.parametrize("invalid_customer_update_data, expected_error, expecting_error_message", [
    (None, TypeError, "customer_update_data must be of type CustomerUpdateResource, not NoneType."),
    (1, TypeError, "customer_update_data must be of type CustomerUpdateResource, not int."),
    (True, TypeError, "customer_update_data must be of type CustomerUpdateResource, not bool."),
    ("customer_data", TypeError, "customer_update_data must be of type CustomerUpdateResource, not str."),
    ({}, TypeError, "customer_update_data must be of type CustomerUpdateResource, not dict."),
    (CustomerUpdateResource(email=customer_test.get('email')), AlreadyTakenFieldValueError,
     f"email: {customer_test.get('email')} is already taken."),
])
def test_update_customer_with_invalid_customer_update_data_partitions(
        mySQLCustomerRepository,
        invalid_customer_update_data,
        expected_error,
        expecting_error_message,
):
    valid_customer_id = customer_oliver.get('id')
    with pytest.raises(expected_error, match=expecting_error_message):
        customers_service.update(
            repository=mySQLCustomerRepository,
            customer_id=valid_customer_id,
            customer_update_data=invalid_customer_update_data
        )


@pytest.mark.parametrize("invalid_customer_id, expected_error, expecting_error_message", [
    (None, TypeError, "customer_id must be of type str, not NoneType."),
    (1, TypeError, "customer_id must be of type str, not int."),
    (True, TypeError, "customer_id must be of type str, not bool."),
    ("unknown-id", UnableToFindIdError, "Customer with ID: unknown-id does not exist."),
])
def test_update_customer_with_invalid_customer_id_partitions(
        mySQLCustomerRepository, valid_customer_data, invalid_customer_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        customers_service.update(
            repository=mySQLCustomerRepository,
            customer_id=invalid_customer_id,
            customer_update_data=CustomerUpdateResource(**valid_customer_data)
        )


@pytest.mark.parametrize("invalid_customer_repository, expecting_error_message", [
    (None, "repository must be of type CustomerRepository, not NoneType."),
    (1, "repository must be of type CustomerRepository, not int."),
    (True, "repository must be of type CustomerRepository, not bool."),
    ("customer_repository", "repository must be of type CustomerRepository, not str."),
])
def test_update_customer_with_invalid_repository_type_partitions(
        mySQLCustomerRepository, valid_customer_data, invalid_customer_repository, expecting_error_message
):
    valid_customer_id = customer_oliver.get('id')
    valid_customer_update_data = CustomerUpdateResource(**valid_customer_data)
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.update(
            repository=invalid_customer_repository,
            customer_id=valid_customer_id,
            customer_update_data=valid_customer_update_data
        )


def test_update_customer_with_invalid_repository_types_partitions(
        mySQLColorRepository, mySQLCarRepository, mySQLPurchaseRepository, valid_customer_data
):
    valid_customer_id = customer_oliver.get('id')
    valid_customer_update_data = CustomerUpdateResource(**valid_customer_data)
    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLColorRepository).__name__}."
                       ):
        customers_service.update(
            repository=mySQLColorRepository,
            customer_id=valid_customer_id,
            customer_update_data=valid_customer_update_data
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLCarRepository).__name__}."
                       ):
        customers_service.update(
            repository=mySQLCarRepository,
            customer_id=valid_customer_id,
            customer_update_data=valid_customer_update_data
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLPurchaseRepository).__name__}."
                       ):
        customers_service.update(
            repository=mySQLPurchaseRepository,
            customer_id=valid_customer_id,
            customer_update_data=valid_customer_update_data
        )


# VALID TESTS FOR delete_customer

@pytest.mark.parametrize("valid_customer",
                         [customer_henrik, customer_oliver, customer_tom, customer_james, customer_test])
def test_delete_customer_with_valid_partitions(
        mySQLCustomerRepository, mySQLCarRepository, mySQLPurchaseRepository, valid_customer
):
    valid_customer_id = valid_customer.get('id')

    customers_service.delete(
        repository=mySQLCustomerRepository,
        customer_id=valid_customer_id
    )

    expected_amount_of_customers_after_deletion = amount_of_expected_customers - 1
    actual_amount_of_customers_after_deletion = len(mySQLCustomerRepository.get_all())

    assert actual_amount_of_customers_after_deletion == expected_amount_of_customers_after_deletion, \
        (f"Amount of customers after deletion {actual_amount_of_customers_after_deletion} does not match "
         f"the expected amount of customers after deletion {expected_amount_of_customers_after_deletion}")

    assert mySQLCustomerRepository.get_by_id(valid_customer_id) is None, \
        f"Customer with ID {valid_customer_id} was not deleted."

    expected_amount_of_cars_after_deletion = amount_of_expected_cars - valid_customer.get('amount_of_cars')
    actual_amount_of_cars_after_deletion = len(mySQLCarRepository.get_all())

    assert actual_amount_of_cars_after_deletion == expected_amount_of_cars_after_deletion, \
        (f"Amount of cars after deletion {actual_amount_of_cars_after_deletion} does not match "
         f"the expected amount of cars after deletion {expected_amount_of_cars_after_deletion}")

    expected_amount_of_purchases_after_deletion = amount_of_expected_purchases - valid_customer.get(
        'amount_of_purchased_cars')
    actual_amount_of_purchases_after_deletion = len(mySQLPurchaseRepository.get_all())

    assert actual_amount_of_purchases_after_deletion == expected_amount_of_purchases_after_deletion, \
        (f"Amount of purchases after deletion {actual_amount_of_purchases_after_deletion} does not match "
         f"the expected amount of purchases after deletion {expected_amount_of_purchases_after_deletion}")

    deleted_customers_car_ids = valid_customer.get('car_ids', [])

    for car_id in deleted_customers_car_ids:
        assert mySQLCarRepository.get_by_id(car_id) is None, \
            f"Car with ID {car_id} was not deleted."


# INVALID TESTS FOR delete_customer

@pytest.mark.parametrize("invalid_customer_id, expected_error, expecting_error_message", [
    (None, TypeError, "customer_id must be of type str, not NoneType."),
    (1, TypeError, "customer_id must be of type str, not int."),
    (True, TypeError, "customer_id must be of type str, not bool."),
    ("unknown-id", UnableToFindIdError, "Customer with ID: unknown-id does not exist."),
])
def test_delete_customer_with_invalid_customer_id_partitions(
        mySQLCustomerRepository, invalid_customer_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        customers_service.delete(
            repository=mySQLCustomerRepository,
            customer_id=invalid_customer_id
        )

    actual_amount_of_customers_after_deletion = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_deletion == amount_of_expected_customers, \
        (f"Amount of customers after deletion {actual_amount_of_customers_after_deletion} does not match "
         f"the expected amount of customers after deletion {amount_of_expected_customers}")


@pytest.mark.parametrize("invalid_customer_repository, expecting_error_message", [
    (None, "repository must be of type CustomerRepository, not NoneType."),
    (1, "repository must be of type CustomerRepository, not int."),
    (True, "repository must be of type CustomerRepository, not bool."),
    ("repository", "repository must be of type CustomerRepository, not str."),
])
def test_delete_customer_with_invalid_customer_repository_type_partitions(
        mySQLCustomerRepository, invalid_customer_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        customers_service.delete(
            repository=invalid_customer_repository,
            customer_id=customer_test.get('id')
        )

    actual_amount_of_customers_after_deletion = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_deletion == amount_of_expected_customers, \
        (f"Amount of customers after deletion {actual_amount_of_customers_after_deletion} does not match "
         f"the expected amount of customers after deletion {amount_of_expected_customers}")


def test_delete_customer_with_invalid_customer_repository_types_partitions(
        mySQLCustomerRepository, mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLAccessoryRepository).__name__}."
                       ):
        customers_service.delete(
            repository=mySQLAccessoryRepository,
            customer_id=customer_test.get('id')
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."
                       ):
        customers_service.delete(
            repository=mySQLBrandRepository,
            customer_id=customer_test.get('id')
        )

    with pytest.raises(TypeError,
                       match=f"repository must be of type CustomerRepository, "
                             f"not {type(mySQLInsuranceRepository).__name__}."
                       ):
        customers_service.delete(
            repository=mySQLInsuranceRepository,
            customer_id=customer_test.get('id')
        )

    actual_amount_of_customers_after_deletion = len(mySQLCustomerRepository.get_all())
    assert actual_amount_of_customers_after_deletion == amount_of_expected_customers, \
        (f"Amount of customers after deletion {actual_amount_of_customers_after_deletion} does not match "
         f"the expected amount of customers after deletion {amount_of_expected_customers}")
