# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import colors_service as service
from app.exceptions.database_errors import UnableToFindIdError
from app.core.security import TokenPayload, get_current_mysql_sales_person_token
from app.repositories.color_repositories import MySQLColorRepository, ColorReturnResource


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/colors",
    response_model=List[ColorReturnResource],
    response_description=
    """
    Successfully retrieved a list of colors.
    Returns: List[ColorReturnResource].
    """,
    summary="Retrieve Colors - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Colors from the MySQL 
    database and returns a list of 'ColorReturnResource'.
    """
)
async def get_colors(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description=
            """
            Set a limit for the amount of colors that is returned.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get colors from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLColorRepository(session),
            colors_limit=limit
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}"))

@router.get(
    path="/color/{color_id}",
    response_model=ColorReturnResource,
    response_description=
    """
    Successfully retrieved a color.
    Returns: ColorReturnResource.
    """,
    summary="Retrieve a Color by ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Color by ID from the MySQL 
    database and returns it as a 'ColorReturnResource'.
    """
)
async def get_color(
        color_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the color to retrieve.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get color from the MySQL database"
    try:
        return service.get_by_id(
            repository=MySQLColorRepository(session),
            color_id=str(color_id)
        )
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )
