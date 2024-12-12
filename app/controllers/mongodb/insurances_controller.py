# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Database, get_mongodb
from app.services import insurances_service as service
from app.controllers.error_handler import error_handler
from app.repositories.insurance_repository import (
    MongoDBInsuranceRepository,
    InsuranceReturnResource
)

router: APIRouter = APIRouter()

def get_db():  # pragma: no cover
    with get_mongodb() as database:
        yield database


@router.get(
    path="/insurances",
    response_model=List[InsuranceReturnResource],
    response_description=
    """
    Successfully retrieved a list of insurances.
    Returns: List[InsuranceReturnResource].
    """,
    summary="Retrieve Insurances.",
    description=
    """
    Retrieves all or a limited amount of Insurances from the 
    MongoDB database and returns a list of 'InsuranceReturnResource'.
    """
)
async def get_insurances(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of insurances that is returned."""
        ),
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get insurances from the MongoDB database",
        callback=lambda: service.get_all(
            repository=MongoDBInsuranceRepository(database),
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
    summary="Retrieve an Insurance by ID.",
    description=
    """
    Retrieves an Insurance by ID from the MongoDB database 
    by giving a UUID in the path for the insurance 
    and returns it as an 'InsuranceReturnResource'.
    """
)
async def get_insurance(
        insurance_id: UUID = Path(
            default=...,
            description="""The UUID of the insurance to retrieve."""
        ),
        database: Database = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get insurance from the MongoDB database",
        callback=lambda: service.get_by_id(
            repository=MongoDBInsuranceRepository(database),
            insurance_id=str(insurance_id)
        )
    )
