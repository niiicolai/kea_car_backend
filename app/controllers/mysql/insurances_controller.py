# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import insurances_service as service
from app.controllers.error_handler import error_handler
from app.core.security import TokenPayload, get_current_mysql_sales_person_token
from app.repositories.insurance_repository import MySQLInsuranceRepository, InsuranceReturnResource



router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/insurances",
    response_model=List[InsuranceReturnResource],
    response_description=
    """
    Successfully retrieved a list of insurances.
    Returns: List[InsuranceReturnResource].
    """,
    summary="Retrieve Insurances - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Insurances from the 
    MySQL database and returns a list of 'InsuranceReturnResource'.
    """
)
async def get_insurances(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of insurances that is returned."""
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get insurances from the MySQL database",
        callback=lambda: service.get_all(
            repository=MySQLInsuranceRepository(session),
            insurances_limit=limit
        )
    )

@router.get(
    path="/insurance/{insurance_id}",
    response_model=InsuranceReturnResource,
    response_description=
    """
    Successfully retrieved an insurance.
    Returns: InsuranceReturnResource.
    """,
    summary="Retrieve an Insurance by ID - Requires authorization token in header.",
    description=
    """
    Retrieves an Insurance by ID from the MySQL database 
    by giving a UUID in the path for the insurance 
    and returns it as an 'InsuranceReturnResource'.
    """
)
async def get_insurance(
        insurance_id: UUID = Path(
            default=...,
            description="""The UUID of the insurance to retrieve."""
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get insurance from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLInsuranceRepository(session),
            insurance_id=str(insurance_id)
        )
    )
