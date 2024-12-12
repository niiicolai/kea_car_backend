# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import cars_service as service
from app.controllers.error_handler import error_handler
from app.core.security import get_current_sales_person_token
from app.repositories.model_repositories import MySQLModelRepository
from app.repositories.color_repositories import MySQLColorRepository
from app.repositories.purchase_repositories import MySQLPurchaseRepository
from app.repositories.insurance_repository import MySQLInsuranceRepository
from app.repositories.customer_repositories import MySQLCustomerRepository
from app.repositories.accessory_repositories import MySQLAccessoryRepository
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository
from app.repositories.car_repositories import (
    MySQLCarRepository,
    CarReturnResource,
    CarCreateResource
)


router: APIRouter = APIRouter()

def get_db():  # pragma: no cover
    with get_db_session() as session:
        yield session


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
    Retrieves all or a limited amount of Cars from the MySQL database,
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
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get cars from the MySQL database",
        callback=lambda: service.get_all(
            car_repository=MySQLCarRepository(session),
            customer_repository=MySQLCustomerRepository(session),
            sales_person_repository=MySQLSalesPersonRepository(session),
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
    Retrieves a Car by ID from the MySQL database by giving a UUID 
    in the path for the car and returns it as a 'CarReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_car(
        car_id: UUID = Path(
            default=...,
            description="""The UUID of the car to retrieve."""
        ),
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get car from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLCarRepository(session),
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
    Creates a Car within the MySQL database 
    by giving a request body 'CarCreateResource' 
    and returns it as a 'CarReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def create_car(
        car_data: CarCreateResource,
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to create car within the MySQL database",
        callback=lambda: service.create(
            car_repository=MySQLCarRepository(session),
            customer_repository=MySQLCustomerRepository(session),
            sales_person_repository=MySQLSalesPersonRepository(session),
            model_repository=MySQLModelRepository(session),
            color_repository=MySQLColorRepository(session),
            accessory_repository=MySQLAccessoryRepository(session),
            insurance_repository=MySQLInsuranceRepository(session),
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
    Deletes a Car within the MySQL database 
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
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to delete car within the MySQL database",
        callback=lambda: service.delete(
            car_repository=MySQLCarRepository(session),
            purchase_repository=MySQLPurchaseRepository(session),
            car_id=str(car_id),
            delete_purchase_too=delete_purchase_too
        )
    )
