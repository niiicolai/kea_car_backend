# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import insurances_service as service
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.insurance_repository import MySQLInsuranceRepository, InsuranceReturnResource



router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/insurances",
    response_model=List[InsuranceReturnResource],
    response_description="Successfully retrieved list of insurances, returns: List[InsuranceReturnResource]",
    summary="Retrieve all Insurances.",
    description="Fetches all Insurances from the MySQL database and returns a list of 'InsuranceReturnResource'."
)
async def get_insurances(session: Session = Depends(get_db)):
    error_message = "Failed to get insurances from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLInsuranceRepository(session)
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
    path="/insurance/{insurance_id}",
    response_model=InsuranceReturnResource,
    response_description="Successfully retrieved an insurance, returns: InsuranceReturnResource",
    summary="Retrieve a Insurance by ID.",
    description="Fetches an Insurance by ID from the MySQL database by giving a UUID in the path for the insurance and returns it as an 'InsuranceReturnResource'."
)
async def get_insurance(insurance_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get insurance from the MySQL database"
    try:
        return service.get_by_id(
            repository=MySQLInsuranceRepository(session),
            insurance_id=str(insurance_id)
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