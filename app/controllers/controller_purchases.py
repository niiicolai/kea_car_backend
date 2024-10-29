# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, status

# Internal library imports
from app.services import service_purchases
from db import Session, get_db as get_db_session
from app.repositories.car_repositories import MySQLCarRepository
from app.repositories.purchase_repositories import MySQLPurchaseRepository, PurchaseReturnResource, PurchaseCreateResource
from app.exceptions.database_errors import (
    UnableToFindIdError,
    PurchaseDeadlineHasPastError,
    AlreadyTakenFieldValueError,
    UnableToFindEntityError
)

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/purchases",
    response_model=List[PurchaseReturnResource],
    response_description="Successfully retrieved list of purchases, returns: List[PurchaseReturnResource]",
    summary="Retrieve all Purchases.",
    description="Fetches all Purchases from the MySQL database and returns a list of 'PurchaseReturnResource'."
)
async def get_purchases(session: Session = Depends(get_db)):
    error_message = "Failed to get purchases from the MySQL database"
    try:
        return service_purchases.get_all(
            repository=MySQLPurchaseRepository(session)
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
    path="/purchase/{purchase_id}",
    response_model=PurchaseReturnResource,
    response_description="Successfully retrieved a purchase, returns: PurchaseReturnResource",
    summary="Retrieve a Purchase by ID.",
    description="Fetches a Purchase by ID from the MySQL database by giving a UUID in the path for the purchase and returns it as a 'PurchaseReturnResource'."
)
async def get_purchase(purchase_id: UUID = Path(..., description="The UUID of the purchase to retrieve."),
                       session: Session = Depends(get_db)):
    error_message = "Failed to get purchase from the MySQL database"
    try:
        return service_purchases.get_by_id(
            repository=MySQLPurchaseRepository(session),
            purchase_id=str(purchase_id)
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
    path="/purchase/car/{cars_id}",
    response_model=PurchaseReturnResource,
    response_description="Successfully retrieved a purchase, returns: PurchaseReturnResource",
    summary="Retrieve a Purchase by Car ID.",
    description="Fetches a Purchase by Car ID from the MySQL database by giving a UUID in the path for the car of the purchase and returns it as a 'PurchaseReturnResource'."
)
async def get_purchase_by_car_id(cars_id: UUID = Path(..., description="The UUID of the purchase's car to retrieve."),
                                 session: Session = Depends(get_db)):
    error_message = "Failed to get purchase by car id from the MySQL database"
    try:
        return service_purchases.get_by_car_id(
            purchase_repository=MySQLPurchaseRepository(session),
            car_repository=MySQLCarRepository(session),
            car_id=str(cars_id)
        )
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except UnableToFindEntityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"Unable To Find Entity Error caught. {error_message}: {e}")
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
    path="/purchase",
    response_model=PurchaseReturnResource,
    response_description="Successfully created a purchase, returns: PurchaseReturnResource.",
    summary="Create a Purchase.",
    description="Creates a Purchase within the MySQL database by giving a request body 'PurchaseCreateResource' and returns it as a 'PurchaseReturnResource'."
)
async def create_purchase(purchase_create_data: PurchaseCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create purchase within the MySQL database"
    try:
        return service_purchases.create(
            purchase_repository=MySQLPurchaseRepository(session),
            car_repository=MySQLCarRepository(session),
            purchase_create_data=purchase_create_data
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
    except PurchaseDeadlineHasPastError as e:
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