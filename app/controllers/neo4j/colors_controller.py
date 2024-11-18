# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Neo4jSession, get_neo4j
from app.services import colors_service as service
from app.controllers.error_handler import error_handler
from app.repositories.color_repositories import Neo4jColorRepository, ColorReturnResource


router: APIRouter = APIRouter()

def get_db():
    with get_neo4j() as session:
        yield session

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
    Retrieves all or a limited amount of Colors from the Neo4j 
    database and returns a list of 'ColorReturnResource'.
    """
)
async def get_colors(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of colors that is returned."""
        ),
        session: Neo4jSession = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get colors from the Neo4j database",
        callback=lambda: service.get_all(
            repository=Neo4jColorRepository(session),
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
    Retrieves a Color by ID from the Neo4j 
    database and returns it as a 'ColorReturnResource'.
    """
)
async def get_color(
        color_id: UUID = Path(
            default=...,
            description="""The UUID of the color to retrieve."""
        ),
        session: Neo4jSession = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get color from the Neo4j database",
        callback=lambda: service.get_by_id(
            repository=Neo4jColorRepository(session),
            color_id=str(color_id)
        )
    )
