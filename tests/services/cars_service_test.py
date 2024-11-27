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
# Valid car data
expected_amount_of_cars = 4
valid_car_test_data = [
    {
        "id": "0be86135-c58f-43b6-a369-a3c5445b9948",
        "purchase_deadline": date(2024,12,7),
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
        "purchase_deadline": date(2024,12,4),
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
        "purchase_deadline": date(2024,12,4),
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
def test_get_all_cars_valid_customer_id(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, car_data):
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
def test_get_all_cars_valid_sales_person_id(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, car_data):
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
def test_get_all_cars_valid_is_purchased(mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository, car_data):
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
        
#TODO: Add test for is_past_purchase_deadline
        
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
        mySQLCarRepository, mySQLCustomerRepository, mySQLSalesPersonRepository,  valid_cars_limit, expecting_car_amount
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


# VALID TESTS FOR create_car

# INVALID TESTS FOR create_car

# VALID TESTS FOR delete_car

# INVALID TESTS FOR delete_car
