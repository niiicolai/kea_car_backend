# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Body, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import customers_service as service
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
    response_description="Successfully retrieved list of customers, returns: List[CustomerReturnResource]",
    summary="Retrieve all Customers.",
    description="Fetches all Customers from the MySQL database and returns a list of 'CustomerReturnResource'."
)
async def get_customers(session: Session = Depends(get_db)):
    error_message = "Failed to get customers from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLCustomerRepository(session)
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
    response_description="Successfully retrieved a customer, returns: CustomerReturnResource",
    summary="Retrieve a Customer by ID.",
    description="Fetches a Customer by ID from the MySQL database and returns it as a 'CustomerReturnResource'."
)
async def get_customer(customer_id: UUID = Path(..., description="The UUID of the customer to retrieve."),
                       session: Session = Depends(get_db)):
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
    response_description="Successfully created a customer, returns: CustomerReturnResource.",
    summary="Create a Customer.",
    description="Creates a Customer within the MySQL database by giving a request body 'CustomerCreateResource' and returns it as a 'CustomerReturnResource'."
)
async def create_customer(customer_create_data: CustomerCreateResource, session: Session = Depends(get_db)):
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
    response_description="Successfully updated a customer, returns: CustomerReturnResource.",
    summary="Update a Customer.",
    description="Updates a Customer within the MySQL database by giving a UUID in the path for the customer and by giving a request body 'CustomerUpdateResource' and returns it as a 'CustomerReturnResource'."
)
async def update_customer(customer_id: UUID = Path(..., description="The UUID of the customer to update."),
                          customer_update_data: CustomerUpdateResource = Body(..., title="CustomerUpdateResource"),
                          session: Session = Depends(get_db)):
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
    response_model=CustomerReturnResource,
    response_description="Successfully deleted a customer, returns: CustomerReturnResource.",
    summary="Delete a Customer.",
    description="Deletes a Customer within the MySQL database by giving a UUID in the path for the customer and returns it as a 'CustomerReturnResource'."
)
async def delete_customer(customer_id: UUID = Path(..., description="The UUID of the customer to delete."),
                          session: Session = Depends(get_db)):
    error_message = "Failed to delete customer within the MySQL database"
    try:
        return service.delete(
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