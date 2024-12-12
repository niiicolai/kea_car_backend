# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Neo4jSession, get_neo4j
from app.services import accessories_service as service
from app.controllers.error_handler import error_handler
from app.repositories.accessory_repositories import (
    Neo4jAccessoryRepository,
    AccessoryReturnResource
)

router: APIRouter = APIRouter()


def get_db():  # pragma: no cover
    with get_neo4j() as session:
        yield session


@router.get(
    path="/accessories",
    response_model=List[AccessoryReturnResource],
    response_description=
    """
    Successfully retrieved a list of accessories.
    Returns: List[AccessoryReturnResource].
    """,
    summary="Retrieve Accessories.",
    description=
    """
    Retrieves all or a limited amount of Accessories from the 
    Neo4j database and returns a list of 'AccessoryReturnResource'.
    """
)
async def get_accessories(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of accessories that is returned."""
        ),
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get accessories from the Neo4j database",
        callback=lambda: service.get_all(
            repository=Neo4jAccessoryRepository(session),
            accessory_limit=limit
        )
    )


@router.get(
    path="/accessory/{accessory_id}",
    response_model=AccessoryReturnResource,
    response_description=
    """
    Successfully retrieved an accessory.
    Returns: AccessoryReturnResource.
    """,
    summary="Retrieve an Accessory by ID.",
    description=
    """
    Retrieves an Accessory by ID from the Neo4j database 
    by giving a UUID in the path for the accessory and 
    returns it as an 'AccessoryReturnResource'.
    """
)
async def get_accessory(
        accessory_id: UUID = Path(
            default=...,
            description="""The UUID of the accessory to retrieve."""
        ),
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get accessory from the Neo4j database",
        callback=lambda: service.get_by_id(
            repository=Neo4jAccessoryRepository(session),
            accessory_id=str(accessory_id)
        )
    )
