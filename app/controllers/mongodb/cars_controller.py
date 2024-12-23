# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query, status

# Internal library imports
from db import Database, get_mongodb
from app.services import cars_service as service
from app.controllers.error_handler import error_handler
from app.core.security import get_current_sales_person_token
from app.repositories.model_repositories import MongoDBModelRepository
from app.repositories.color_repositories import MongoDBColorRepository
from app.repositories.purchase_repositories import MongoDBPurchaseRepository
from app.repositories.insurance_repository import MongoDBInsuranceRepository
from app.repositories.customer_repositories import MongoDBCustomerRepository
from app.repositories.accessory_repositories import MongoDBAccessoryRepository
from app.repositories.sales_person_repositories import MongoDBSalesPersonRepository
from app.repositories.car_repositories import (
    MongoDBCarRepository,
    CarReturnResource,
    CarCreateResource
)


router: APIRouter = APIRouter()

def get_db():  # pragma: no cover
    with get_mongodb() as database:
        yield database

@router.get(
    path="/cars",
    response_model=List[CarReturnResource],
    response_description=
    """
    Successfully retrieved list a of cars. 
    Returns: List[CarReturnResource].
    """,
    summary="Retrieve Cars - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Cars from the MongoDB database,
    potentially filtered by cars belonging to a customer and/or sales person, 
    if the cars are purchased and/or is past their purchase deadline,
    and returns a list of 'CarReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_cars(
        customer_id: Optional[UUID] = Query(
            default=None,
            description=
            """
            The UUID of the customer, 
            to retrieve cars belonging to that customer.
            """
        ),
        sales_person_id: Optional[UUID] = Query(
            default=None,
            description=
            """
            The UUID of the sales person, 
            to retrieve cars belonging to that sales person.
            """
        ),
        is_purchased: Optional[bool] = Query(
            default=None,
            description=
            """
            Set to: 
            'true' to retrieve only purchased cars, 
            'false' to retrieve only cars that has not been purchased 
            and default retrieves both purchased and non-purchased cars.
            """
        ),
        is_past_purchase_deadline: Optional[bool] = Query(
            default=None,
            description=
            """
            Set to: 
            'true' to retrieve only cars past purchase deadline, 
            'false' to retrieve only cars that has not past the purchased deadline 
            and default retrieves cars that is past and not past purchase deadline.
            """
        ),
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of cars that is returned."""
        ),
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get cars from the MongoDB database",
        callback=lambda: service.get_all(
            car_repository=MongoDBCarRepository(database),
            customer_repository=MongoDBCustomerRepository(database),
            sales_person_repository=MongoDBSalesPersonRepository(database),
            customer_id=None if not customer_id else str(customer_id),
            sales_person_id=None if not sales_person_id else str(sales_person_id),
            is_purchased=is_purchased,
            is_past_purchase_deadline=is_past_purchase_deadline,
            cars_limit=limit
        )
    )


@router.get(
    path="/car/{car_id}",
    response_model=CarReturnResource,
    response_description=
    """
    Successfully retrieved a car. 
    Returns: CarReturnResource
    """,
    summary="Retrieve a Car by ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Car by ID from the MongoDB database by giving a UUID 
    in the path for the car and returns it as a 'CarReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_car(
        car_id: UUID = Path(
            default=...,
            description="""The UUID of the car to retrieve."""
        ),
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get car from the MongoDB database",
        callback=lambda: service.get_by_id(
            repository=MongoDBCarRepository(database),
            car_id=str(car_id)
        )
    )


@router.post(
    path="/car",
    response_model=CarReturnResource,
    response_description=
    """
    Successfully created a car. 
    Returns: CarReturnResource.
    """,
    summary="Create a Car - Requires authorization token in header.",
    description=
    """
    Creates a Car within the MongoDB database 
    by giving a request body 'CarCreateResource' 
    and returns it as a 'CarReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def create_car(
        car_data: CarCreateResource,
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to create car within the MongoDB database",
        callback=lambda: service.create(
            car_repository=MongoDBCarRepository(database),
            customer_repository=MongoDBCustomerRepository(database),
            sales_person_repository=MongoDBSalesPersonRepository(database),
            model_repository=MongoDBModelRepository(database),
            color_repository=MongoDBColorRepository(database),
            accessory_repository=MongoDBAccessoryRepository(database),
            insurance_repository=MongoDBInsuranceRepository(database),
            car_create_data=car_data
        )
    )


@router.delete(
    path="/car/{car_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description=
    """
    Successfully deleted a car.
    Returns: 204 No Content.
    """,
    summary="Delete a Car - Requires authorization token in header.",
    description=
    """
    Deletes a Car within the MongoDB database 
    by giving a UUID in the path for the car 
    and returns a 204 status code.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def delete_car(
        car_id: UUID = Path(
            default=...,
            description="""The UUID of the car to delete."""
        ),
        delete_purchase_too: bool = Query(
            default=False,
            description=
            """
            A boolean that is default False, 
            for if you are certain you want to delete 
            the car with its purchase if it has one.
            """
        ),
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to delete car within the MongoDB database",
        callback=lambda: service.delete(
            car_repository=MongoDBCarRepository(database),
            purchase_repository=MongoDBPurchaseRepository(database),
            car_id=str(car_id),
            delete_purchase_too=delete_purchase_too
        )
    )
