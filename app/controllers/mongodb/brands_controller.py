# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Database, get_mongodb
from app.services import brands_service as service
from app.controllers.error_handler import error_handler
from app.repositories.brand_repositories import (
    MongoDBBrandRepository,
    BrandReturnResource
)


router: APIRouter = APIRouter()

def get_db():
    with get_mongodb() as database:
        yield database

@router.get(
    path="/brands",
    response_model=List[BrandReturnResource],
    response_description=
    """
    Successfully retrieved a list of brands.
    Returns: List[BrandReturnResource].
    """,
    summary="Retrieve Brands.",
    description=
    """
    Retrieves all or a limited amount of Brands from the MongoDB 
    database and returns a list of 'BrandReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_brands(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of brands that is returned."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get brands from the MongoDB database",
        callback=lambda: service.get_all(
            repository=MongoDBBrandRepository(database),
            brands_limit=limit
        )
    )


@router.get(
    path="/brand/{brand_id}",
    response_model=BrandReturnResource,
    response_description=
    """
    Successfully retrieved a brand. 
    Returns: BrandReturnResource.
    """,
    summary="Retrieve a Brand by ID.",
    description=
    """
    Retrieves a Brand by ID from the MongoDB database by giving a UUID 
    in the path for the brand and returns it as a 'BrandReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_brand(
        brand_id: UUID = Path(
            default=...,
            description="""The UUID of the brand to retrieve."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get brand from the MongoDB database",
        callback=lambda: service.get_by_id(
            repository=MongoDBBrandRepository(database),
            brand_id=str(brand_id)
        )
    )
