# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Database, get_mongodb
from app.services import accessories_service as service
from app.controllers.error_handler import error_handler
from app.repositories.accessory_repositories import (
    AccessoryReturnResource,
    MongoDBAccessoryRepository
)

router: APIRouter = APIRouter()


def get_db():
    with get_mongodb() as database:
        yield database


@router.get(
    path="/accessories",
    response_model=List[AccessoryReturnResource],
    response_description=
    """
    Successfully retrieved a list of accessories.
    Returns: List[AccessoryReturnResource].
    """,
    summary="Retrieve Accessories - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Accessories from the 
    MongoDB database and returns a list of 'AccessoryReturnResource'.
    """
)
async def get_accessories(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of accessories that is returned."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get accessories from the MongoDB database",
        callback=lambda: service.get_all(
            repository=MongoDBAccessoryRepository(database),
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
    Retrieves an Accessory by ID from the MongoDB database 
    by giving a UUID in the path for the accessory and 
    returns it as an 'AccessoryReturnResource'.
    """
)
async def get_accessory(
        accessory_id: UUID = Path(
            default=...,
            description="""The UUID of the accessory to retrieve."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get accessory from the MongoDB database",
        callback=lambda: service.get_by_id(
            repository=MongoDBAccessoryRepository(database),
            accessory_id=str(accessory_id)
        )
    )
