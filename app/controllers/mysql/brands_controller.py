# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import brands_service as service
from app.exceptions.database_errors import UnableToFindIdError
from app.repositories.brand_repositories import MySQLBrandRepository, BrandReturnResource


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get(
    path="/brands",
    response_model=List[BrandReturnResource],
    response_description=
    """
    Successfully retrieved a list of brands.
    Returns: List[BrandReturnResource].
    """,
    summary="Retrieve Brands.",
    description=
    """
    Retrieves all or a limited amount of Brands from the MySQL 
    database and returns a list of 'BrandReturnResource'.
    """
)
async def get_brands(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description=
            """
            Set a limit for the amount of brands that is returned.
            """
        ),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get brands from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLBrandRepository(session),
            brands_limit=limit
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
    response_description=
    """
    Successfully retrieved a brand. 
    Returns: BrandReturnResource.
    """,
    summary="Retrieve a Brand by ID.",
    description=
    """
    Retrieves a Brand by ID from the MySQL database by giving a UUID 
    in the path for the brand and returns it as a 'BrandReturnResource'.
    """
)
async def get_brand(
        brand_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the brand to retrieve.
            """
        ),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get brand from the MySQL database"
    try:
        return service.get_by_id(
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
