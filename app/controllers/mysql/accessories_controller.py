# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import accessories_service as service
from app.controllers.error_handler import error_handler
from app.repositories.accessory_repositories import (
    AccessoryReturnResource,
    MySQLAccessoryRepository
)

router: APIRouter = APIRouter()


def get_db():  # pragma: no cover
    with get_db_session() as session:
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
    MySQL database and returns a list of 'AccessoryReturnResource'.
    """
)
async def get_accessories(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of accessories that is returned."""
        ),
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get accessories from the MySQL database",
        callback=lambda: service.get_all(
            repository=MySQLAccessoryRepository(session),
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
    Retrieves an Accessory by ID from the MySQL database 
    by giving a UUID in the path for the accessory and 
    returns it as an 'AccessoryReturnResource'.
    """
)
async def get_accessory(
        accessory_id: UUID = Path(
            default=...,
            description="""The UUID of the accessory to retrieve."""
        ),
        session: Session = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get accessory from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLAccessoryRepository(session),
            accessory_id=str(accessory_id)
        )
    )
