# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Body, status

# Internal library imports
from app.services import service_colors
from db import Session, get_db as get_db_session
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.color_repositories import MySQLColorRepository, ColorReturnResource, ColorCreateResource

# These imports should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.color_resource import ColorUpdateResource


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
async def get_colors(session: Session = Depends(get_db)):
    error_message = "Failed to get colors from the MySQL database"
    try:
        return service_colors.get_all(
            repository=MySQLColorRepository(session)
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
    response_description="Successfully retrieved a color, returns: ColorReturnResource",
    summary="Retrieve a Color by ID.",
    description="Fetches a Color by ID from the MySQL database and returns it as a 'ColorReturnResource'."
)
async def get_color(color_id: UUID = Path(..., description="The UUID of the color to retrieve."),
                    session: Session = Depends(get_db)):
    error_message = "Failed to get color from the MySQL database"
    try:
        return service_colors.get_by_id(
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


@router.post(
    path="/color",
    response_model=ColorReturnResource,
    response_description="Successfully created a color, returns: ColorReturnResource.",
    summary="Create a Color.",
    description="Creates a Color within the MySQL database by giving a request body 'ColorCreateResource' and returns it as a 'ColorReturnResource'."
)
async def create_color(color_create_data: ColorCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create color within the MySQL database"
    try:
        return service_colors.create(
            repository=MySQLColorRepository(session),
            color_create_data=color_create_data
        )
    except AlreadyTakenFieldValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
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

@router.put(
    path="/color/{color_id}",
    response_model=ColorReturnResource,
    response_description="Successfully updated a color, returns: ColorReturnResource.",
    summary="Update a Color - NOT BEEN IMPLEMENTED YET.",
    description="Updates a Color within the MySQL database by giving a UUID in the path for the color and by giving a request body 'ColorUpdateResource' and returns it as a 'ColorReturnResource'."
)
async def update_color(color_id: UUID = Path(..., description="The UUID of the color to update."),
                       color_update_data: ColorUpdateResource = Body(..., title="ColorUpdateResource"),
                       session: Session = Depends(get_db)):
    error_message = "Failed to update color within the MySQL database"
    try:
        raise NotImplementedError("Request PUT '/mysql/color/{color_id}' has not been implemented yet.")
    except AlreadyTakenFieldValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
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

@router.delete(
    path="/color/{color_id}",
    response_model=ColorReturnResource,
    response_description="Successfully deleted a color, returns: ColorReturnResource.",
    summary="Delete a Color - NOT BEEN IMPLEMENTED YET.",
    description="Deletes a Color within the MySQL database by giving a UUID in the path for the color and returns it as a 'ColorReturnResource'."
)
async def delete_color(color_id: UUID = Path(..., description="The UUID of the color to delete."),
                       session: Session = Depends(get_db)):
    error_message = "Failed to delete color within the MySQL database"
    try:
        raise NotImplementedError("Request DELETE '/mysql/color/{color_id}' has not been implemented yet.")
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