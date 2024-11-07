# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Query, Body, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import customers_service as service
from app.core.security import TokenPayload, get_current_mysql_sales_person_token
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.customer_repositories import (
    MySQLCustomerRepository,
    CustomerReturnResource,
    CustomerCreateResource,
    CustomerUpdateResource
)

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/customers",
    response_model=List[CustomerReturnResource],
    response_description=
    """
    Successfully retrieved a list of customers. 
    Returns: List[CustomerReturnResource].
    """,
    summary="Retrieve Customers - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Customers from the 
    MySQL database and returns a list of 'CustomerReturnResource'.
    """
)
async def get_customers(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description=
            """
            Set a limit for the amount of customers that is returned.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get customers from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLCustomerRepository(session),
            customers_limit=limit
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
    path="/customer/{customer_id}",
    response_model=CustomerReturnResource,
    response_description=
    """
    Successfully retrieved a customer.
    Returns: CustomerReturnResource.
    """,
    summary="Retrieve a Customer by ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Customer by ID from the MySQL database 
    and returns it as a 'CustomerReturnResource'.
    """
)
async def get_customer(
        customer_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the customer to retrieve.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get customer from the MySQL database"
    try:
        return service.get_by_id(
            repository=MySQLCustomerRepository(session),
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


@router.post(
    path="/customer",
    response_model=CustomerReturnResource,
    response_description=
    """
    Successfully created a customer.
    Returns: CustomerReturnResource.
    """,
    summary="Create a Customer - Requires authorization token in header.",
    description=
    """
    Creates a Customer within the MySQL database 
    by giving a request body 'CustomerCreateResource' 
    and returns it as a 'CustomerReturnResource'.
    """
)
async def create_customer(
        customer_create_data: CustomerCreateResource,
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to create customer within the MySQL database"
    try:
        return service.create(
            repository=MySQLCustomerRepository(session),
            customer_create_data=customer_create_data
        )
    except AlreadyTakenFieldValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
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


@router.put(
    path="/customer/{customer_id}",
    response_model=CustomerReturnResource,
    response_description=
    """
    Successfully updated a customer.
    Returns: CustomerReturnResource.
    """,
    summary="Update a Customer - Requires authorization token in header.",
    description=
    """
    Updates a Customer within the MySQL database 
    by giving a UUID in the path for the customer 
    and by giving a request body 'CustomerUpdateResource' 
    and returns it as a 'CustomerReturnResource'.
    """
)
async def update_customer(
        customer_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the customer to update.
            """
        ),
        customer_update_data: CustomerUpdateResource = Body(
            default=...,
            title="CustomerUpdateResource"
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to update customer within the MySQL database"
    try:
        return service.update(
            repository=MySQLCustomerRepository(session),
            customer_id=str(customer_id),
            customer_update_data=customer_update_data
        )
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except AlreadyTakenFieldValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
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


@router.delete(
    path="/customer/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description=
    """
    Successfully deleted a customer.
    Returns: 204 No Content.
    """,
    summary="Delete a Customer - Requires authorization token in header.",
    description=
    """
    Deletes a Customer within the MySQL database 
    by giving a UUID in the path for the customer 
    and returns a 204 status code.
    """
)
async def delete_customer(
        customer_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the customer to delete.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to delete customer within the MySQL database"
    try:
        service.delete(
            repository=MySQLCustomerRepository(session),
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
