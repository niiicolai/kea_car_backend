# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Query, Body, status, Request


# Internal library imports
from app.services import service_accessories
from db import Session, get_db as get_db_session
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.accessory_repositories import MySQLAccessoryRepository, AccessoryReturnResource

# These imports should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.accessory_resource import AccessoryCreateResource, AccessoryUpdateResource


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    "/accessories",
    response_model=List[AccessoryReturnResource],
    response_description="Successfully retrieved list of accessories from the MySQL database: List[AccessoryReturnResource]",
    summary="Retrieve All Accessories.",
    description="Fetches all accessories from the database and returns a list of 'AccessoryReturnResource'."
)
async def get_accessories(session: Session = Depends(get_db)):
    error_message = "Failed to get accessories"
    try:
        return service_accessories.get_all(MySQLAccessoryRepository(session))
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

@router.get(
    "/accessory/{accessory_id}",
    response_model=AccessoryReturnResource,
    response_description="Successfully retrieved an accessory from the MySQL database: AccessoryReturnResource",
    summary="Retrieve an Accessory by ID.",
    description="Fetches an 'AccessoryReturnResource' by ID from the MySQL database.")
async def get_accessory(accessory_id: UUID = Path(..., description="The UUID of the accessory to retrieve"),
                        session: Session = Depends(get_db)):
    error_message = "Failed to get accessory"
    try:
        return service_accessories.get_by_id(MySQLAccessoryRepository(session), str(accessory_id))
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
    "/accessory",
    response_model=AccessoryReturnResource,
    response_description="Successfully created an accessory from the MySQL database: AccessoryReturnResource.",
    summary="Creates an Accessory - NOT BEEN IMPLEMENTED YET.",
    description="Creates an Accessory within the MySQL database by giving a request body 'AccessoryCreateResource' and returns it as an 'AccessoryReturnResource'.")
async def create_accessory(accessory_create_data: AccessoryCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create accessory"
    try:
        raise NotImplementedError("Request POST '/accessory' has not been implemented yet.")
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )

@router.put("/accessory/{accessory_id}",
            response_model=AccessoryReturnResource,
            response_description="Successfully updated an accessory from the MySQL database: AccessoryReturnResource.",
            description="Updated an Accessory within the MySQL database by giving a request body 'AccessoryUpdateResource' and returns it as an 'AccessoryReturnResource'.",
            summary="Updates an Accessory - NOT BEEN IMPLEMENTED YET.")
async def update_accessory(accessory_id: UUID = Path(..., description="The UUID of the accessory to update."),
                           accessory_update_data: AccessoryUpdateResource = Body(..., title="AccessoryUpdateResource"),
                           session: Session = Depends(get_db)):
    error_message = "Failed to update accessory"
    try:
        raise NotImplementedError("Request PUT '/accessory/{accessory_id}' has not been implemented yet.")
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
    "/accessory/{accessory_id}",
    response_model=AccessoryReturnResource,
    response_description="Successfully deleted an accessory from the MySQL database: AccessoryReturnResource.",
    description="Deleted an Accessory within the MySQL database by giving a UUID in the path for the accessory and returns it as an 'AccessoryReturnResource'.",
    summary="Deletes an Accessory - NOT BEEN IMPLEMENTED YET.")
async def delete_accessory(accessory_id: UUID = Path(..., description="The UUID of the accessory to delete."),
                           session: Session = Depends(get_db)):
    error_message = "Failed to delete accessory"
    try:
        raise NotImplementedError("Request DELETE '/accessory/{accessory_id}' has not been implemented yet.")
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