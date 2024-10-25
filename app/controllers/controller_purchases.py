from fastapi import APIRouter, Depends, HTTPException, status
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_purchases
from app.exceptions.database_errors import UnableToFindIdError, PurchaseDeadlineHasPastError, AlreadyTakenFieldValueError, UnableToFindEntityError
from app.repositories.purchase_repositories import MySQLPurchaseRepository, PurchaseReturnResource, PurchaseCreateResource
from app.repositories.car_repositories import MySQLCarRepository
from typing import List
from uuid import UUID

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/purchases", response_model=List[PurchaseReturnResource], description="Returns all purchases.")
async def get_purchases(session: Session = Depends(get_db)):
    error_message = "Failed to get purchases"
    try:
        return service_purchases.get_all(MySQLPurchaseRepository(session))
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
            detail=str(f"Unknown Error caught. {error_message}: {e}")
        )

@router.get("/purchase/{purchase_id}", response_model=PurchaseReturnResource, description="Returns one Model by ID.")
async def get_purchase(purchase_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get purchase"
    try:
        return service_purchases.get_by_id(MySQLPurchaseRepository(session), str(purchase_id))
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
            detail=str(f"Unknown Error caught. {error_message}: {e}")
        )

@router.get("/purchase/car/{cars_id}", response_model=PurchaseReturnResource, description="Returns a Purchase by a Car ID.")
async def get_purchase_by_car_id(cars_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get purchase by car id"
    try:
        return service_purchases.get_by_car_id(
            MySQLPurchaseRepository(session),
            MySQLCarRepository(session),
            str(cars_id))
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
            detail=str(f"Unknown Error caught. {error_message}: {e}")
        )


@router.post("/purchase", response_model=PurchaseReturnResource, description="Create a new Purchase.")
async def create_purchase(purchase_create_data: PurchaseCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create purchase"
    try:
        return service_purchases.create(
            MySQLPurchaseRepository(session),
            MySQLCarRepository(session),
            purchase_create_data)
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