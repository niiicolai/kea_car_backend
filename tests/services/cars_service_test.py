from typing import Optional

import pytest
from app.services import cars_service
from app.exceptions.database_errors import (
    UnableToFindIdError,
    TheColorIsNotAvailableInModelToGiveToCarError,
    UnableToDeleteCarWithoutDeletingPurchaseTooError
)
from datetime import date
from app.resources.car_resource import (
    CarCreateResource,
    CarReturnResource,
    ModelReturnResource,
    ColorReturnResource,
    AccessoryReturnResource,
    InsuranceReturnResource,
    CustomerReturnResource,
    SalesPersonReturnResource
)


def create_car_resource(
        invalid_model_id: Optional[str] = None,
        invalid_color_id: Optional[str] = None,
        invalid_customer_id: Optional[str] = None,
        invalid_sales_person_id: Optional[str] = None,
        invalid_accessory_ids: Optional[str] = None,
        invalid_insurance_ids: Optional[str] = None
) -> CarCreateResource:
    valid_car_data = valid_car_test_data[0]
    valid_model_id = valid_car_data.get("model").get("id")
    valid_color_id = valid_car_data.get("color").get("id")
    valid_customer_id = valid_car_data.get("customer").get("id")
    valid_sales_person_id = valid_car_data.get("sales_person").get("id")
    valid_accessory_ids = [accessory.get("id") for accessory in valid_car_data.get("accessories")]
    valid_insurance_ids = [insurance.get("id") for insurance in valid_car_data.get( "insurances")]

    return CarCreateResource(
        models_id=invalid_model_id if invalid_model_id else valid_model_id,
        colors_id=invalid_color_id if invalid_color_id else valid_color_id,
        customers_id=invalid_customer_id if invalid_customer_id else valid_customer_id,
        sales_people_id=invalid_sales_person_id if invalid_sales_person_id else valid_sales_person_id,
        accessory_ids=[invalid_accessory_ids] if invalid_accessory_ids else valid_accessory_ids,
        insurance_ids=[invalid_insurance_ids] if invalid_insurance_ids else valid_insurance_ids
    )


# Valid car data

expected_amount_of_cars = 4
invalid_customer_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"
invalid_sales_person_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"
invalid_model_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"
invalid_color_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"
invalid_color_model_id = "14382aba-6fe6-405d-a5e2-0b8cfd1f9582"
invalid_accessory_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"
invalid_insurance_id_data = "0be86135-c58f-43b6-a369-a3c5445b9948"

valid_car_test_data = [
    {
        "id": "0be86135-c58f-43b6-a369-a3c5445b9948",
        "purchase_deadline": date(2024, 12, 7),
        "total_price": 10530.8,
        "model": {
            "id": "d4bd413c-00d8-45ce-be0e-1d1333ac5e75"
        },
        "color": {
            "id": "7bb35b1d-37ff-43c2-988a-cf85c5b6d690"
        },
        "accessories": [
            {
                "id": "e7858d25-49e7-4ad5-821c-100de2b18918"
            }
        ],
        "insurances": [
            {
                "id": "37074fac-26da-4e38-9ae6-acbe755359e5"
            }
        ],
        "customer": {
            "id": "f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc"
        },
        "sales_person": {
            "id": "f9097a97-eca4-49b6-85a0-08423789c320"
        },
        "is_purchased": False
    },
    {
        "id": "d4c7f1f8-4451-43bc-a827-63216a2ddece",
        "purchase_deadline": date(2024, 12, 4),
        "total_price": 10530.8,
        "model": {
            "id": "d4bd413c-00d8-45ce-be0e-1d1333ac5e75"
        },
        "color": {
            "id": "7bb35b1d-37ff-43c2-988a-cf85c5b6d690"
        },
        "accessories": [
            {
                "id": "e7858d25-49e7-4ad5-821c-100de2b18918"
            }
        ],
        "insurances": [
            {
                "id": "37074fac-26da-4e38-9ae6-acbe755359e5"
            }
        ],
        "customer": {
            "id": "0ac1d668-55aa-46a1-898a-8fa61457facb"
        },
        "sales_person": {
            "id": "f9097a97-eca4-49b6-85a0-08423789c320"
        },
        "is_purchased": True
    },
    {
        "id": "a1b1e305-1a89-4b06-86d1-21ac1fa3c8a6",
        "purchase_deadline": date(2024, 12, 4),
        "total_price": 10530.8,
        "model": {
            "id": "d4bd413c-00d8-45ce-be0e-1d1333ac5e75"
        },
        "color": {
            "id": "7bb35b1d-37ff-43c2-988a-cf85c5b6d690"
        },
        "accessories": [
            {
                "id": "e7858d25-49e7-4ad5-821c-100de2b18918"
            }
        ],
        "insurances": [
            {
                "id": "37074fac-26da-4e38-9ae6-acbe755359e5"
            }
        ],
        "customer": {
            "id": "f159bdaf-bc83-46c3-8a3f-f6b5c93ebbdc"
        },
        "sales_person": {
            "id": "d096d2e1-f06a-4555-9cd1-afa9f930f10c"
        },
        "is_purchased": False
    },
]


# VALID TESTS FOR get_car_by_id
@pytest.mark.parametrize("car_data", valid_car_test_data)
def test_get_car_by_id_valid(mySQLCarRepository, car_data):
    valid_car_id = car_data.get("id")
    car = cars_service.get_by_id(repository=mySQLCarRepository, car_id=valid_car_id)
    assert isinstance(car, CarReturnResource), "The car is not a CarReturnResource instance"

    assert car.id == valid_car_id, (
        f"The car id {car.id} is not the same as the expected id {valid_car_id}"
    )

    assert car.purchase_deadline == car_data.get("purchase_deadline"), (
        f"The car purchase_deadline {car.purchase_deadline} is not the same as the expected "
        f"purchase_deadline {car_data.get('purchase_deadline')}"
    )

    assert car.total_price == car_data.get("total_price"), (
        f"The car total_price {car.total_price} is not the same as the expected total_price "
        f"{car_data.get('total_price')}"
    )

    assert isinstance(car.model, ModelReturnResource), (
        f"The car model is not a ModelReturnResource instance, but a {type(car.model).__name__}"
    )

    assert car.model.id == car_data.get("model").get("id"), (
        f"The car model id {car.model.id} is not the same as the expected model id "
        f"{car_data.get('model').get('id')}"
    )

    assert isinstance(car.color, ColorReturnResource), (
        f"The car color is not a ColorReturnResource instance, but a {type(car.color).__name__}"
    )

    assert car.color.id == car_data.get("color").get("id"), (
        f"The car color id {car.color.id} is not the same as the expected color id "
        f"{car_data.get('color').get('id')}"
    )

    assert (
            isinstance(car.accessories, list) and
            all(isinstance(accessory, AccessoryReturnResource) for accessory in car.accessories)
    ), (
        f"The car accessories are not a list of AccessoryReturnResource instances"
    )

    assert all(
        accessory.id in [accessory.get("id") for accessory in car_data.get("accessories")]
        for accessory in car.accessories
    ), (
        f"The car accessories ids {', '.join([accessory.id for accessory in car.accessories])} "
        f"are not the same as the expected accessories ids "
        f"{', '.join([accessory.get('id') for accessory in car_data.get('accessories')])}"
    )

    assert (
            isinstance(car.insurances, list) and
            all(isinstance(insurance, InsuranceReturnResource) for insurance in car.insurances)
    ), (
        f"The car insurances are not a list of InsuranceReturnResource instances"
    )

    assert all(
        insurance.id in [insurance.get("id") for insurance in car_data.get("insurances")]
        for insurance in car.insurances
    ), (
        f"The car insurances ids {', '.join([insurance.id for insurance in car.insurances])} "
        f"are not the same as the expected insurances ids "
        f"{', '.join([insurance.get('id') for insurance in car_data.get('insurances')])}"
    )

    assert isinstance(car.customer, CustomerReturnResource), (
        f"The customer is not a CustomerReturnResource instance, but a {type(car.customer).__name__}"
    )

    assert car.customer.id == car_data.get("customer").get("id"), (
        f"The customer id {car.customer.id} is not the same as the expected customer id "
        f"{car_data.get('customer').get('id')}"
    )

    assert isinstance(car.sales_person, SalesPersonReturnResource), (
        f"The sales_person is not a SalesPersonReturnResource instance, but a {type(car.sales_person).__name__}"
    )

    assert car.sales_person.id == car_data.get("sales_person").get("id"), (
        f"The sales_person id {car.sales_person.id} is not the same as the expected sales_person id "
        f"{car_data.get('sales_person').get('id')}"
    )

    assert car.is_purchased == car_data.get("is_purchased"), (
        f"The car is_purchased {car.is_purchased} is not the same as the expected is_purchased "
        f"{car_data.get('is_purchased')}"
    )


# INVALID TESTS FOR get_car_by_id
@pytest.mark.parametrize("invalid_car_id, expected_error, expecting_error_message", [
    (None, TypeError, "car_id must be of type str, not NoneType."),
    (True, TypeError, "car_id must be of type str, not bool."),
    (1, TypeError, "car_id must be of type str, not int."),
    ("unknown-id", UnableToFindIdError, "Car with ID: unknown-id does not exist."),
])
def test_get_car_by_id_with_invalid_car_id_partitions(
        mySQLCarRepository, invalid_car_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        cars_service.get_by_id(
            repository=mySQLCarRepository,
            car_id=invalid_car_id
        )


@pytest.mark.parametrize("invalid_car_repository, expecting_error_message", [
    (None, "repository must be of type CarRepository, not NoneType."),
    (1, "repository must be of type CarRepository, not int."),
    (True, "repository must be of type CarRepository, not bool."),
    ("repository", "repository must be of type CarRepository, not str."),
])
def test_get_car_by_id_with_invalid_repository_type_partitions(invalid_car_repository, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_by_id(
            repository=invalid_car_repository,
            car_id="d4c7f1f8-4451-43bc-a827-63216a2ddece"
        )


def test_get_car_by_id_with_invalid_repository_types_partitions(
        mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type CarRepository, not {type(mySQLAccessoryRepository).__name__}."):
        cars_service.get_by_id(
            repository=mySQLAccessoryRepository,
            car_id="d4c7f1f8-4451-43bc-a827-63216a2ddece"
        )
    with pytest.raises(TypeError,
                       match=f"repository must be of type CarRepository, not {type(mySQLBrandRepository).__name__}."):
        cars_service.get_by_id(
            repository=mySQLBrandRepository,
            car_id="d4c7f1f8-4451-43bc-a827-63216a2ddece"
        )
    with pytest.raises(TypeError,
                       match=f"repository must be of type CarRepository, not {type(mySQLInsuranceRepository).__name__}."):
        cars_service.get_by_id(
            repository=mySQLInsuranceRepository,
            car_id="d4c7f1f8-4451-43bc-a827-63216a2ddece"
        )


# VALID TESTS FOR get_all_cars
def test_get_all_cars_valid(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository):
    cars = cars_service.get_all(car_repository=mySQLCarRepository,
                                customer_repository=mySQLCustomerRepository,
                                sales_person_repository=mySQLSalesPersonRepository)
    assert isinstance(cars, list), "The cars are not a list"
    for car in cars:
        assert isinstance(car, CarReturnResource), "The car is not a CarReturnResource instance"
    assert len(cars) == expected_amount_of_cars, (
        f"The amount of cars {len(cars)} is not the same as the expected amount of cars {expected_amount_of_cars}"
    )


@pytest.mark.parametrize("car_data", valid_car_test_data)
def test_get_all_cars_valid_customer_id(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository,
                                        car_data):
    valid_customer_id = car_data.get("customer").get("id")
    cars = cars_service.get_all(car_repository=mySQLCarRepository,
                                customer_repository=mySQLCustomerRepository,
                                sales_person_repository=mySQLSalesPersonRepository,
                                customer_id=valid_customer_id)
    assert isinstance(cars, list), "The cars are not a list"
    for car in cars:
        assert isinstance(car, CarReturnResource), "The car is not a CarReturnResource instance"
        assert isinstance(car.customer, CustomerReturnResource), (
            f"The customer is not a CustomerReturnResource instance, but a {type(car.customer).__name__}"
        )
        assert car.customer.id == valid_customer_id, (
            f"The customer id {car.customer.id} is not the same as the expected customer id {valid_customer_id}"
        )


@pytest.mark.parametrize("car_data", valid_car_test_data)
def test_get_all_cars_valid_sales_person_id(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository,
                                            car_data):
    valid_sales_person_id = car_data.get("sales_person").get("id")
    cars = cars_service.get_all(car_repository=mySQLCarRepository,
                                customer_repository=mySQLCustomerRepository,
                                sales_person_repository=mySQLSalesPersonRepository,
                                sales_person_id=valid_sales_person_id)
    assert isinstance(cars, list), "The cars are not a list"
    for car in cars:
        assert isinstance(car, CarReturnResource), "The car is not a CarReturnResource instance"
        assert isinstance(car.sales_person, SalesPersonReturnResource), (
            f"The sales_person is not a SalesPersonReturnResource instance, but a {type(car.sales_person).__name__}"
        )
        assert car.sales_person.id == valid_sales_person_id, (
            f"The sales_person id {car.sales_person.id} is not the same as the expected sales_person id {valid_sales_person_id}"
        )


@pytest.mark.parametrize("car_data", valid_car_test_data)
def test_get_all_cars_valid_is_purchased(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository,
                                         car_data):
    valid_is_purchased = car_data.get("is_purchased")
    cars = cars_service.get_all(car_repository=mySQLCarRepository,
                                customer_repository=mySQLCustomerRepository,
                                sales_person_repository=mySQLSalesPersonRepository,
                                is_purchased=valid_is_purchased)
    assert isinstance(cars, list), "The cars are not a list"
    for car in cars:
        assert isinstance(car, CarReturnResource), "The car is not a CarReturnResource instance"
        assert car.is_purchased == valid_is_purchased, (
            f"The car is_purchased {car.is_purchased} is not the same as the expected is_purchased {valid_is_purchased}"
        )


@pytest.mark.parametrize("valid_cars_limit, expecting_car_amount", [
    (-1, 4),
    (None, 4),
    (0, 4),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 4)
])
def test_get_all_cars_with_valid_cars_limit_values_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, valid_cars_limit, expecting_car_amount
):
    cars = cars_service.get_all(
        car_repository=mySQLCarRepository,
        customer_repository=mySQLCustomerRepository,
        sales_person_repository=mySQLSalesPersonRepository,
        cars_limit=valid_cars_limit
    )

    assert isinstance(cars, list) and all(isinstance(car, CarReturnResource) for car in cars) \
        , f"Cars are not a list of CarReturnResource objects, but {type(cars).__name__}"

    assert len(cars) == expecting_car_amount \
        , f"There should be {expecting_car_amount} cars, not '{len(cars)}'"


# INVALID TESTS FOR get_all_cars

@pytest.mark.parametrize("invalid_cars_limit, expecting_error_message", [
    ("1", "cars_limit must be of type int or None, not str."),
    (1.0, "cars_limit must be of type int or None, not float."),
    (True, "cars_limit must be of type int or None, not bool."),
])
def test_get_all_cars_with_invalid_cars_limit_values_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, invalid_cars_limit,
        expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            cars_limit=invalid_cars_limit
        )


@pytest.mark.parametrize("invalid_is_purchased, expecting_error_message", [
    ("1", "is_purchased must be of type bool or None, not str."),
    (1, "is_purchased must be of type bool or None, not int."),
    (1.0, "is_purchased must be of type bool or None, not float."),
    ("True", "is_purchased must be of type bool or None, not str.")
])
def test_get_all_cars_with_invalid_is_purchased_values_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, invalid_is_purchased,
        expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            is_purchased=invalid_is_purchased
        )


@pytest.mark.parametrize("invalid_customer_id, expected_error, expecting_error_message", [
    (1, TypeError, "customer_id must be of type str or None, not int."),
    (True, TypeError, "customer_id must be of type str or None, not bool."),
    ("unknown-id", UnableToFindIdError, "Customer with ID: unknown-id does not exist."),
])
def test_get_all_cars_with_invalid_customer_id_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, invalid_customer_id, expected_error,
        expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            customer_id=invalid_customer_id
        )


@pytest.mark.parametrize("invalid_sales_person_id, expected_error, expecting_error_message", [
    (1, TypeError, "sales_person_id must be of type str or None, not int."),
    (True, TypeError, "sales_person_id must be of type str or None, not bool."),
    ("unknown-id", UnableToFindIdError, "Sales Person with ID: unknown-id does not exist."),
])
def test_get_all_cars_with_invalid_sales_person_id_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, invalid_sales_person_id,
        expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            sales_person_id=invalid_sales_person_id
        )


@pytest.mark.parametrize("invalid_car_repository, expecting_error_message", [
    (None, "car_repository must be of type CarRepository, not NoneType."),
    (1, "car_repository must be of type CarRepository, not int."),
    (True, "car_repository must be of type CarRepository, not bool."),
    ("repository", "car_repository must be of type CarRepository, not str."),
])
def test_get_all_cars_with_invalid_car_repository_type_partitions(
        mySQLCustomerRepository, mySQLSalesPersonRepository, invalid_car_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_all(
            car_repository=invalid_car_repository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository
        )


@pytest.mark.parametrize("invalid_customer_repository, expecting_error_message", [
    (None, "customer_repository must be of type CustomerRepository, not NoneType."),
    (1, "customer_repository must be of type CustomerRepository, not int."),
    (True, "customer_repository must be of type CustomerRepository, not bool."),
    ("repository", "customer_repository must be of type CustomerRepository, not str."),
])
def test_get_all_cars_with_invalid_customer_repository_type_partitions(
        mySQLCarRepository, mySQLSalesPersonRepository, invalid_customer_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=invalid_customer_repository,
            sales_person_repository=mySQLSalesPersonRepository
        )


@pytest.mark.parametrize("invalid_sales_person_repository, expecting_error_message", [
    (None, "sales_person_repository must be of type SalesPersonRepository, not NoneType."),
    (1, "sales_person_repository must be of type SalesPersonRepository, not int."),
    (True, "sales_person_repository must be of type SalesPersonRepository, not bool."),
    ("repository", "sales_person_repository must be of type SalesPersonRepository, not str."),
])
def test_get_all_cars_with_invalid_sales_person_repository_type_partitions(
        mySQLCarRepository, mySQLCustomerRepository, invalid_sales_person_repository, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=invalid_sales_person_repository
        )


def test_get_all_cars_with_invalid_repository_types_partitions(
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository
):
    with pytest.raises(TypeError,
                       match=f"car_repository must be of type CarRepository, "
                             f"not {type(mySQLCustomerRepository).__name__}."):
        cars_service.get_all(
            car_repository=mySQLCustomerRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository
        )
    with pytest.raises(TypeError,
                       match=f"customer_repository must be of type CustomerRepository, "
                             f"not {type(mySQLSalesPersonRepository).__name__}."):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLSalesPersonRepository,
            sales_person_repository=mySQLSalesPersonRepository
        )
    with pytest.raises(TypeError,
                       match=f"sales_person_repository must be of type SalesPersonRepository, "
                             f"not {type(mySQLCarRepository).__name__}."):
        cars_service.get_all(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLCarRepository
        )


# VALID TESTS FOR create_car

@pytest.mark.parametrize("valid_car_data", valid_car_test_data)
def test_create_car_with_valid_partitions(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLModelRepository,
        mySQLColorRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        valid_car_data
):
    amount_of_cars_before_creation = expected_amount_of_cars
    expected_amount_of_cars_after_creation = amount_of_cars_before_creation + 1

    valid_car_create_resource = create_car_resource()

    created_car = cars_service.create(
        car_repository=mySQLCarRepository,
        customer_repository=mySQLCustomerRepository,
        sales_person_repository=mySQLSalesPersonRepository,
        model_repository=mySQLModelRepository,
        color_repository=mySQLColorRepository,
        accessory_repository=mySQLAccessoryRepository,
        insurance_repository=mySQLInsuranceRepository,
        car_create_data=valid_car_create_resource
    )

    assert isinstance(created_car, CarReturnResource), \
        (f"Car is not of type CarReturnResource, "
         f"but {type(created_car).__name__}")

    expected_car_id = created_car.id
    assert mySQLCarRepository.get_by_id(expected_car_id) is not None, \
        f"Car with ID {expected_car_id} was not created."

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars_after_creation, \
        (f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
         f"the expected amount of cars after creation {expected_amount_of_cars_after_creation}")

    assert created_car.total_price == valid_car_data.get("total_price"), \
        (f"Created car's total price {created_car.total_price} does not match the expected total price "
         f"{valid_car_data.get('total_price')}")


# INVALID TESTS FOR create_car
@pytest.mark.parametrize("invalid_car_repository, expecting_error_message", [
    (None, "car_repository must be of type CarRepository, not NoneType."),
    (1, "car_repository must be of type CarRepository, not int."),
    (True, "car_repository must be of type CarRepository, not bool."),
    ("car_repository", "car_repository must be of type CarRepository, not str."),
])
def test_create_car_with_invalid_car_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLModelRepository,
        mySQLColorRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_car_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=invalid_car_repository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_customer_repository, expecting_error_message", [
    (None, "customer_repository must be of type CustomerRepository, not NoneType."),
    (1, "customer_repository must be of type CustomerRepository, not int."),
    (True, "customer_repository must be of type CustomerRepository, not bool."),
    ("customer_repository", "customer_repository must be of type CustomerRepository, not str."),
])
def test_create_car_with_invalid_customer_repository(
        mySQLCarRepository,
        mySQLSalesPersonRepository,
        mySQLModelRepository,
        mySQLColorRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_customer_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=invalid_customer_repository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_sales_person_repository, expecting_error_message", [
    (None, "sales_person_repository must be of type SalesPersonRepository, not NoneType."),
    (1, "sales_person_repository must be of type SalesPersonRepository, not int."),
    (True, "sales_person_repository must be of type SalesPersonRepository, not bool."),
    ("sales_person_repository", "sales_person_repository must be of type SalesPersonRepository, not str."),
])
def test_create_car_with_invalid_sales_person_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLModelRepository,
        mySQLColorRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_sales_person_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=invalid_sales_person_repository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_model_repository, expecting_error_message", [
    (None, "model_repository must be of type ModelRepository, not NoneType."),
    (1, "model_repository must be of type ModelRepository, not int."),
    (True, "model_repository must be of type ModelRepository, not bool."),
    ("model_repository", "model_repository must be of type ModelRepository, not str."),
])
def test_create_car_with_invalid_model_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLColorRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_model_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=invalid_model_repository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_color_repository, expecting_error_message", [
    (None, "color_repository must be of type ColorRepository, not NoneType."),
    (1, "color_repository must be of type ColorRepository, not int."),
    (True, "color_repository must be of type ColorRepository, not bool."),
    ("color_repository", "color_repository must be of type ColorRepository, not str."),
])
def test_create_car_with_invalid_color_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLModelRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_color_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=invalid_color_repository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_accessory_repository, expecting_error_message", [
    (None, "accessory_repository must be of type AccessoryRepository, not NoneType."),
    (1, "accessory_repository must be of type AccessoryRepository, not int."),
    (True, "accessory_repository must be of type AccessoryRepository, not bool."),
    ("accessory_repository", "accessory_repository must be of type AccessoryRepository, not str."),
])
def test_create_car_with_invalid_accessory_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLColorRepository,
        mySQLModelRepository,
        mySQLInsuranceRepository,
        invalid_accessory_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=invalid_accessory_repository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=valid_car_create_resource
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_insurance_repository, expecting_error_message", [
    (None, "insurance_repository must be of type InsuranceRepository, not NoneType."),
    (1, "insurance_repository must be of type InsuranceRepository, not int."),
    (True, "insurance_repository must be of type InsuranceRepository, not bool."),
    ("insurance_repository", "insurance_repository must be of type InsuranceRepository, not str."),
])
def test_create_car_with_invalid_insurance_repository(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLColorRepository,
        mySQLModelRepository,
        mySQLAccessoryRepository,
        invalid_insurance_repository,
        expecting_error_message
):
    valid_car_create_resource = create_car_resource()

    with pytest.raises(TypeError, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=invalid_insurance_repository,
            car_create_data=valid_car_create_resource
        )
    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")


@pytest.mark.parametrize("invalid_car_create_data, expecting_error, expecting_error_message", [
    (None, TypeError, "car_create_data must be of type CarCreateResource, not NoneType."),
    (1, TypeError, "car_create_data must be of type CarCreateResource, not int."),
    (True, TypeError, "car_create_data must be of type CarCreateResource, not bool."),
    ("car_create_data", TypeError, "car_create_data must be of type CarCreateResource, not str."),
    (create_car_resource(invalid_model_id=invalid_model_id_data), UnableToFindIdError,
     f"Model with ID: {invalid_model_id_data} does not exist."),
    (create_car_resource(invalid_color_id=invalid_color_id_data), UnableToFindIdError,
     f"Color with ID: {invalid_color_id_data} does not exist."),
    (create_car_resource(invalid_customer_id=invalid_customer_id_data), UnableToFindIdError,
     f"Customer with ID: {invalid_customer_id_data} does not exist."),
    (create_car_resource(invalid_sales_person_id=invalid_sales_person_id_data), UnableToFindIdError,
     f"Sales Person with ID: {invalid_sales_person_id_data} does not exist."),
    (create_car_resource(invalid_accessory_ids=invalid_accessory_id_data), UnableToFindIdError,
     f"Accessory with ID: {invalid_accessory_id_data} does not exist."),
    (create_car_resource(invalid_insurance_ids=invalid_insurance_id_data), UnableToFindIdError,
     f"Insurance with ID: {invalid_insurance_id_data} does not exist."),
    (create_car_resource(invalid_color_id=invalid_color_model_id),
     TheColorIsNotAvailableInModelToGiveToCarError, "does not have the color: silver")

])
def test_create_car_with_invalid_car_create_data_partitions(
        mySQLCarRepository,
        mySQLCustomerRepository,
        mySQLSalesPersonRepository,
        mySQLColorRepository,
        mySQLModelRepository,
        mySQLAccessoryRepository,
        mySQLInsuranceRepository,
        invalid_car_create_data,
        expecting_error,
        expecting_error_message
):
    with pytest.raises(expecting_error, match=expecting_error_message):
        cars_service.create(
            car_repository=mySQLCarRepository,
            customer_repository=mySQLCustomerRepository,
            sales_person_repository=mySQLSalesPersonRepository,
            model_repository=mySQLModelRepository,
            color_repository=mySQLColorRepository,
            accessory_repository=mySQLAccessoryRepository,
            insurance_repository=mySQLInsuranceRepository,
            car_create_data=invalid_car_create_data
        )

    actual_amount_of_cars_after_creation = len(mySQLCarRepository.get_all())
    assert actual_amount_of_cars_after_creation == expected_amount_of_cars, (
            f"Amount of cars after creation {actual_amount_of_cars_after_creation} does not match "
            f"the expected amount of cars after creation {expected_amount_of_cars}")

# VALID TESTS FOR delete_car

@pytest.mark.parametrize("valid_car", valid_car_test_data)
def test_delete_car_with_valid_partitions(
    mySQLCarRepository, mySQLPurchaseRepository, valid_car
):
    valid_car_id = valid_car.get("id")
    delete_purchase_too = valid_car.get("is_purchased", False)


    amount_of_expected_cars = len(mySQLCarRepository.get_all())
    amount_of_expected_purchases = len(mySQLPurchaseRepository.get_all())


    cars_service.delete(
        car_repository=mySQLCarRepository,
        purchase_repository=mySQLPurchaseRepository,
        car_id=valid_car_id,
        delete_purchase_too=delete_purchase_too
    )


    expected_amount_of_cars_after_deletion = amount_of_expected_cars - 1
    actual_amount_of_cars_after_deletion = len(mySQLCarRepository.get_all())

    assert actual_amount_of_cars_after_deletion == expected_amount_of_cars_after_deletion, \
        (f"Amount of cars after deletion {actual_amount_of_cars_after_deletion} does not match "
         f"the expected amount of cars after deletion {expected_amount_of_cars_after_deletion}")

    assert mySQLCarRepository.get_by_id(valid_car_id) is None, \
        f"Car with ID {valid_car_id} was not deleted."

    if delete_purchase_too:
        expected_amount_of_purchases_after_deletion = amount_of_expected_purchases - 1
        actual_amount_of_purchases_after_deletion = len(mySQLPurchaseRepository.get_all())

        assert actual_amount_of_purchases_after_deletion == expected_amount_of_purchases_after_deletion, \
            (f"Amount of purchases after deletion {actual_amount_of_purchases_after_deletion} does not match "
             f"the expected amount of purchases after deletion {expected_amount_of_purchases_after_deletion}")


# INVALID TESTS FOR delete_car

@pytest.mark.parametrize("invalid_car_id, expected_error, expected_error_message", [
    (None, TypeError, "car_id must be of type str, not NoneType."),
    (1, TypeError, "car_id must be of type str, not int."),
    (True, TypeError, "car_id must be of type str, not bool."),
    ("unknown-id", UnableToFindIdError, "Car with ID: unknown-id does not exist."),
])
def test_delete_car_with_invalid_car_id(
    mySQLCarRepository, mySQLPurchaseRepository, invalid_car_id, expected_error, expected_error_message
):
    with pytest.raises(expected_error, match=expected_error_message):
        cars_service.delete(
            car_repository=mySQLCarRepository,
            purchase_repository=mySQLPurchaseRepository,
            car_id=invalid_car_id,
            delete_purchase_too=False
        )

@pytest.mark.parametrize("invalid_delete_purchase_too, expected_error_message", [
    (None, "delete_purchase_too must be of type bool, not NoneType."),
    (1, "delete_purchase_too must be of type bool, not int."),
    ("True", "delete_purchase_too must be of type bool, not str."),
])
def test_delete_car_with_invalid_delete_purchase_too(
    mySQLCarRepository, mySQLPurchaseRepository, invalid_delete_purchase_too, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        cars_service.delete(
            car_repository=mySQLCarRepository,
            purchase_repository=mySQLPurchaseRepository,
            car_id=valid_car_test_data[0]["id"],
            delete_purchase_too=invalid_delete_purchase_too
        )

@pytest.mark.parametrize("invalid_car_repository, expected_error_message", [
    (None, "car_repository must be of type CarRepository, not NoneType."),
    (1, "car_repository must be of type CarRepository, not int."),
    (True, "car_repository must be of type CarRepository, not bool."),
    ("repo", "car_repository must be of type CarRepository, not str."),
])
def test_delete_car_with_invalid_car_repository(
    mySQLPurchaseRepository, invalid_car_repository, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        cars_service.delete(
            car_repository=invalid_car_repository,
            purchase_repository=mySQLPurchaseRepository,
            car_id=valid_car_test_data[0]["id"],
            delete_purchase_too=False
        )

@pytest.mark.parametrize("invalid_purchase_repository, expected_error_message", [
    (None, "purchase_repository must be of type PurchaseRepository, not NoneType."),
    (1, "purchase_repository must be of type PurchaseRepository, not int."),
    (True, "purchase_repository must be of type PurchaseRepository, not bool."),
    ("repo", "purchase_repository must be of type PurchaseRepository, not str."),
])
def test_delete_car_with_invalid_purchase_repository(
    mySQLCarRepository, invalid_purchase_repository, expected_error_message
):
    with pytest.raises(TypeError, match=expected_error_message):
        cars_service.delete(
            car_repository=mySQLCarRepository,
            purchase_repository=invalid_purchase_repository,
            car_id=valid_car_test_data[0]["id"],
            delete_purchase_too=False
        )

def test_delete_car_without_deleting_purchase(
    mySQLCarRepository, mySQLPurchaseRepository
):
    
    car_id_with_purchase = valid_car_test_data[1]["id"]
    delete_purchase_too = False
    expected_error = UnableToDeleteCarWithoutDeletingPurchaseTooError
    expected_error_message = f"The car with ID: '{car_id_with_purchase}' must delete its purchase too."

    amount_of_expected_cars = len(mySQLCarRepository.get_all())
    amount_of_expected_purchases = len(mySQLPurchaseRepository.get_all())

    with pytest.raises(expected_error, match=expected_error_message):
        cars_service.delete(
            car_repository=mySQLCarRepository,
            purchase_repository=mySQLPurchaseRepository,
            car_id=car_id_with_purchase,
            delete_purchase_too=delete_purchase_too
        )

    assert len(mySQLCarRepository.get_all()) == amount_of_expected_cars, (
        "The number of cars changed despite an exception being raised."
    )
    assert len(mySQLPurchaseRepository.get_all()) == amount_of_expected_purchases, (
        "The number of purchases changed despite an exception being raised."
    )

