# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import colors_service as service
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.color_repositories import MySQLColorRepository, ColorReturnResource
from app.controllers.mysql_error_handler import mysql_error_handler

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session


@router.get(
    path="/colors",
    response_model=List[ColorReturnResource],
    response_description="Successfully retrieved list of colors, returns: List[ColorReturnResource]",
    summary="Retrieve all Colors.",
    description="Fetches all Colors from the MySQL database by giving a UUID in the path for the color and returns a list of 'ColorReturnResource'."
)
async def get_colors(
        limit: Optional[int] = Query(default=None, ge=1, description="Set a limit of the amount of colors that is returned."),
        session: Session = Depends(get_db)):
    return mysql_error_handler(lambda: service.get_all(MySQLColorRepository(session), limit))


@router.get(
    path="/color/{color_id}",
    response_model=ColorReturnResource,
    response_description="Successfully retrieved a color, returns: ColorReturnResource",
    summary="Retrieve a Color by ID.",
    description="Fetches a Color by ID from the MySQL database and returns it as a 'ColorReturnResource'."
)
async def get_color(
        color_id: str = Path(..., description="The UUID of the color to retrieve."),
        session: Session = Depends(get_db)):
    return mysql_error_handler(lambda: service.get_by_id(MySQLColorRepository(session), color_id), {
        UnableToFindIdError: { "status_code": status.HTTP_404_NOT_FOUND }
    })
