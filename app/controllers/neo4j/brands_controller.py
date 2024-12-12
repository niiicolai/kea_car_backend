# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Neo4jSession, get_neo4j
from app.services import brands_service as service
from app.controllers.error_handler import error_handler
from app.repositories.brand_repositories import (
    Neo4jBrandRepository,
    BrandReturnResource
)


router: APIRouter = APIRouter()

def get_db():  # pragma: no cover
    with get_neo4j() as session:
        yield session

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
    Retrieves all or a limited amount of Brands from the Neo4j 
    database and returns a list of 'BrandReturnResource'.
    """
)
async def get_brands(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of brands that is returned."""
        ),
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get brands from the Neo4j database",
        callback=lambda: service.get_all(
            repository=Neo4jBrandRepository(session),
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
    Retrieves a Brand by ID from the Neo4j database by giving a UUID 
    in the path for the brand and returns it as a 'BrandReturnResource'.
    """
)
async def get_brand(
        brand_id: UUID = Path(
            default=...,
            description="""The UUID of the brand to retrieve."""
        ),
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get brand from the Neo4j database",
        callback=lambda: service.get_by_id(
            repository=Neo4jBrandRepository(session),
            brand_id=str(brand_id)
        )
    )
