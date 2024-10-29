# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Body, status

# Internal library imports
from app.services import service_brands
from db import Session, get_db as get_db_session
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.brand_repositories import MySQLBrandRepository, BrandReturnResource

# These imports should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.brand_resource import BrandCreateResource, BrandUpdateResource

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/brands",
    response_model=List[BrandReturnResource],
    response_description="Successfully retrieved list of brands, returns: List[BrandReturnResource]",
    summary="Retrieve all Brands.",
    description="Fetches all Brands from the MySQL database and returns a list of 'BrandReturnResource'."
)
async def get_brands(session: Session = Depends(get_db)):
    error_message = "Failed to get brands from the MySQL database"
    try:
        return service_brands.get_all(
            repository=MySQLBrandRepository(session)
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

@router.get(
    path="/brand/{brand_id}",
    response_model=BrandReturnResource,
    response_description="Successfully retrieved a brand, returns: BrandReturnResource",
    summary="Retrieve a Brand by ID.",
    description="Fetches a Brand by ID from the MySQL database by giving a UUID in the path for the brand and returns it as a 'BrandReturnResource'."
)
async def get_brand(brand_id: UUID = Path(..., description="The UUID of the brand to retrieve."),
                    session: Session = Depends(get_db)):
    error_message = "Failed to get brand from the MySQL database"
    try:
        return service_brands.get_by_id(
            repository=MySQLBrandRepository(session),
            brand_id=str(brand_id)
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
    path="/brand",
    response_model=BrandReturnResource,
    response_description="Successfully created a brand, returns: AccessoryReturnResource.",
    summary="Create a Brand - NOT BEEN IMPLEMENTED YET.",
    description="Creates a Brand within the MySQL database by giving a request body 'BrandCreateResource' and returns it as a 'BrandReturnResource'."
)
async def create_brand(brand_create_data: BrandCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create brand within the MySQL database"
    try:
        raise NotImplementedError("Request POST '/mysql/brand' has not been implemented yet.")
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

@router.put(
    path="/brand/{brand_id}",
    response_model=BrandReturnResource,
    response_description="Successfully updated a brand, returns: BrandReturnResource.",
    summary="Update a Brand - NOT BEEN IMPLEMENTED YET.",
    description="Updates a Brand within the MySQL database by giving a UUID in the path for the brand and by giving a request body 'BrandUpdateResource' and returns it as a 'BrandReturnResource'."
)
async def update_brand(brand_id: UUID = Path(..., description="The UUID of the brand to update."),
                       brand_update_data: BrandUpdateResource = Body(..., title="BrandUpdateResource"),
                       session: Session = Depends(get_db)):
    error_message = "Failed to update brand within the MySQL database"
    try:
        raise NotImplementedError("Request PUT '/mysql/brand/{brand_id}' has not been implemented yet.")
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
    path="/brand/{brand_id}",
    response_model=BrandReturnResource,
    response_description="Successfully deleted a brand, returns: BrandReturnResource.",
    summary="Delete a Brand - NOT BEEN IMPLEMENTED YET.",
    description="Deletes a Brand within the MySQL database by giving a UUID in the path for the brand and returns it as a 'BrandReturnResource'."
)
async def delete_brand(brand_id: UUID = Path(..., description="The UUID of the brand to delete."),
                       session: Session = Depends(get_db)):
    error_message = "Failed to delete brand within the MySQL database"
    try:
        raise NotImplementedError("Request DELETE '/mysql/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )