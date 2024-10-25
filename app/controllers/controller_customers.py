# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, status

# Internal library imports
from app.services import service_customers
from db import Session, get_db as get_db_session
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.customer_repositories import MySQLCustomerRepository, CustomerReturnResource, CustomerCreateResource

# These imports should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.customer_resource import CustomerUpdateResource


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/customers", response_model=List[CustomerReturnResource], description="Returns all customers.")
async def get_customers(session: Session = Depends(get_db)):
    error_message = "Failed to get customers"
    try:
        return service_customers.get_all(MySQLCustomerRepository(session))
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

@router.get("/customer/{customer_id}", response_model=CustomerReturnResource, description="Returns one customer by ID.")
async def get_customer(customer_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get customer"
    try:
        return service_customers.get_by_id(MySQLCustomerRepository(session), str(customer_id))
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


@router.post("/customer", response_model=CustomerReturnResource, description="Creates and returns a new customer.")
async def create_customer(customer_create_data: CustomerCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create customer"
    try:
        return service_customers.create(MySQLCustomerRepository(session), customer_create_data)
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

@router.put("/customer/{customer_id}", response_model=CustomerReturnResource, description="Not been implemented yet.")
async def update_customer(customer_id: UUID, customer_update_data: CustomerUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update customer"
    try:
        raise NotImplementedError("Request PUT '/customer/{customer_id}' has not been implemented yet.")
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

@router.delete("/customer/{customer_id}", response_model=CustomerReturnResource, description="Not been implemented yet.")
async def delete_customer(customer_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete customer"
    try:
        raise NotImplementedError("Request DELETE '/customer/{customer_id}' has not been implemented yet.")
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