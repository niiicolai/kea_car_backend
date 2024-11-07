# External Library imports
from uuid import UUID
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.exceptions.database_errors import UnableToFindIdError
from app.services.view_services import car_purchase_service as service
from app.repositories.customer_repositories import MySQLCustomerRepository
from app.core.security import TokenPayload, get_current_mysql_sales_person_token
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository

from app.repositories.view_repositories.car_purchase_repositories import (
    MySQLCarPurchaseRepository,
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
    """
)
async def get_sales_person_with_car_purchases(
        sales_person_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the sales person to retrieve with cars.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get sales person with car purchases from the MySQL database"

    try:
        return service.get_sales_person_with_cars(
            car_purchase_repository=MySQLCarPurchaseRepository(session),
            sales_person_repository=MySQLSalesPersonRepository(session),
            sales_person_id=str(sales_person_id)
        )
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
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
    """
)
async def get_customer_with_car_purchases(
        customer_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the customer to retrieve with cars.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get customer with car purchases from the MySQL database"
    try:
        return service.get_customer_with_cars(
            car_purchase_repository=MySQLCarPurchaseRepository(session),
            customer_repository=MySQLCustomerRepository(session),
            customer_id=str(customer_id)
        )
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )
