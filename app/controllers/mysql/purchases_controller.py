# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import purchases_service as service
from app.controllers.error_handler import error_handler
from app.core.security import get_current_sales_person_token
from app.repositories.car_repositories import MySQLCarRepository
from app.repositories.purchase_repositories import (
    MySQLPurchaseRepository,
    PurchaseReturnResource,
    PurchaseCreateResource
)


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session
        session.commit()

@router.get(
    path="/purchases",
    response_model=List[PurchaseReturnResource],
    response_description=
    """
    Successfully retrieved a list of purchases.
    Returns: List[PurchaseReturnResource].
    """,
    summary="Retrieve Purchases - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Purchases from the MySQL 
    database and returns a list of 'PurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_purchases(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of purchases that is returned."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get purchases from the MySQL database",
        callback=lambda: service.get_all(
            repository=MySQLPurchaseRepository(session),
            purchases_limit=limit
        )
    )


@router.get(
    path="/purchase/{purchase_id}",
    response_model=PurchaseReturnResource,
    response_description=
    """
    Successfully retrieved a purchase.
    Returns: PurchaseReturnResource.
    """,
    summary="Retrieve a Purchase by ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Purchase by ID from the MySQL database 
    by giving a UUID in the path for the purchase and 
    returns it as a 'PurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_purchase(
        purchase_id: UUID = Path(
            default=...,
            description="""The UUID of the purchase to retrieve."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get purchase from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLPurchaseRepository(session),
            purchase_id=str(purchase_id)
        )
    )


@router.get(
    path="/purchase/car/{cars_id}",
    response_model=PurchaseReturnResource,
    response_description=
    """
    Successfully retrieved a purchase.
    Returns: PurchaseReturnResource.
    """,
    summary="Retrieve a Purchase by Car ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Purchase by Car ID from the MySQL database 
    by giving a UUID in the path for the car of the purchase 
    and returns it as a 'PurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_purchase_by_car_id(
        cars_id: UUID = Path(
            default=...,
            description="""The UUID of the purchase's car to retrieve."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get purchase by car id from the MySQL database",
        callback=lambda: service.get_by_car_id(
            purchase_repository=MySQLPurchaseRepository(session),
            car_repository=MySQLCarRepository(session),
            car_id=str(cars_id)
        )
    )


@router.post(
    path="/purchase",
    response_model=PurchaseReturnResource,
    response_description=
    """
    Successfully created a purchase.
    Returns: PurchaseReturnResource.
    """,
    summary="Create a Purchase - Requires authorization token in header.",
    description=
    """
    Creates a Purchase within the MySQL database 
    by giving a request body 'PurchaseCreateResource' 
    and returns it as a 'PurchaseReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def create_purchase(
        purchase_create_data: PurchaseCreateResource,
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to create purchase within the MySQL database",
        callback=lambda: service.create(
            purchase_repository=MySQLPurchaseRepository(session),
            car_repository=MySQLCarRepository(session),
            purchase_create_data=purchase_create_data
        )
    )
