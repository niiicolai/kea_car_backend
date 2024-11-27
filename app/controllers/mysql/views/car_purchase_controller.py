# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query


# Internal library imports
from db import Session, get_db as get_db_session
from app.controllers.error_handler import error_handler
from app.core.security import get_current_sales_person_token
from app.services.view_services import car_purchase_service as service
from app.repositories.customer_repositories import MySQLCustomerRepository
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository

from app.repositories.view_repositories.car_purchase_repositories import (
    MySQLCarPurchaseRepository,
    CarPurchaseReturnResource,
    CustomerWithCarsReturnResource,
    SalesPersonWithCarsReturnResource
)

router: APIRouter = APIRouter()


def get_db():
    with get_db_session() as session:
        yield session


@router.get(
    path="/car_purchase/sales_person/{sales_person_id}",
    response_model=SalesPersonWithCarsReturnResource,
    response_description=
    """
    Successfully retrieved a sales person with cars.
    Returns: SalesPersonWithCarsReturnResource.
    """,
    summary="Retrieve sales person with cars - Requires authorization token in header.",
    description=
    """
    Retrieves a Sales Person with cars from the MySQL database by giving a UUID in the 
    path for the sales person and returns it as a 'SalesPersonWithCarsReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_sales_person_with_car_purchases(
        sales_person_id: UUID = Path(
            default=...,
            description="""The UUID of the sales person to retrieve with cars."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get sales person with car purchases from the MySQL database",
        callback=
        lambda: service.get_sales_person_with_cars(
            car_purchase_repository=MySQLCarPurchaseRepository(session),
            sales_person_repository=MySQLSalesPersonRepository(session),
            sales_person_id=str(sales_person_id)
        )
    )


@router.get(
    path="/car_purchase/customer/{customer_id}",
    response_model=CustomerWithCarsReturnResource,
    response_description=
    """
    Successfully retrieved a customer with cars.
    Returns: CustomerWithCarsReturnResource.
    """,
    summary="Retrieve customer with cars - Requires authorization token in header.",
    description=
    """
    Retrieves a Customer with cars from the MySQL database by giving a UUID in the 
    path for the customer and returns it as a 'CustomerWithCarsReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_customer_with_car_purchases(
        customer_id: UUID = Path(
            default=...,
            description="""The UUID of the customer to retrieve with cars."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get customer with car purchases from the MySQL database",
        callback=
        lambda: service.get_customer_with_cars(
            car_purchase_repository=MySQLCarPurchaseRepository(session),
            customer_repository=MySQLCustomerRepository(session),
            customer_id=str(customer_id)
        )
    )

@router.get(
    path="/cars_with_purchase",
    response_model=List[CarPurchaseReturnResource],
    response_description=
    """
    Successfully retrieved a list of cars with purchases.
    Returns: List[CarPurchaseReturnResource].
    """,
    summary="Retrieve Cars with Purchase - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Cars with Purchase from the MySQL 
    database and returns a list of 'CarPurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_cars_with_purchase(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of cars with purchase that is returned."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get cars with purchase from the MySQL database",
        callback=
        lambda: service.get_cars_with_purchase(
            repository=MySQLCarPurchaseRepository(session),
            cars_purchase_limit=limit
        )
    )

@router.get(
    path="/car_with_purchase/{car_id}",
    response_model=CarPurchaseReturnResource,
    response_description=
    """
    Successfully retrieved a car with purchase.
    Returns: CarPurchaseReturnResource.
    """,
    summary="Retrieve a Car with Purchase by car ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Car with Purchase by ID from the MySQL database 
    by giving a UUID in the path for the car 
    and returns it as a 'CarPurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_sales_person(
        car_id: UUID = Path(
            default=...,
            description="""The UUID of the car to retrieve."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get car with purchase from the MySQL database",
        callback=lambda: service.get_car_with_purchase_by_id(
            repository=MySQLCarPurchaseRepository(session),
            car_id=str(car_id)
        )
    )
