# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Database, get_mongodb
from app.services import colors_service as service
from app.controllers.error_handler import error_handler
from app.repositories.color_repositories import MongoDBColorRepository, ColorReturnResource


router: APIRouter = APIRouter()

def get_db():
    with get_mongodb() as database:
        yield database

@router.get(
    path="/colors",
    response_model=List[ColorReturnResource],
    response_description=
    """
    Successfully retrieved a list of colors.
    Returns: List[ColorReturnResource].
    """,
    summary="Retrieve Colors.",
    description=
    """
    Retrieves all or a limited amount of Colors from the MongoDB 
    database and returns a list of 'ColorReturnResource'.
    """
)
async def get_colors(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of colors that is returned."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get colors from the MongoDB database",
        callback=lambda: service.get_all(
            repository=MongoDBColorRepository(database),
            colors_limit=limit
        )
    )


@router.get(
    path="/color/{color_id}",
    response_model=ColorReturnResource,
    response_description=
    """
    Successfully retrieved a color.
    Returns: ColorReturnResource.
    """,
    summary="Retrieve a Color by ID.",
    description=
    """
    Retrieves a Color by ID from the MongoDB 
    database and returns it as a 'ColorReturnResource'.
    """
)
async def get_color(
        color_id: UUID = Path(
            default=...,
            description="""The UUID of the color to retrieve."""
        ),
        database: Database = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get color from the MongoDB database",
        callback=lambda: service.get_by_id(
            repository=MongoDBColorRepository(database),
            color_id=str(color_id)
        )
    )
