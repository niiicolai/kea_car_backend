from fastapi import APIRouter, Depends, HTTPException, status
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_brands
from app.repositories.brand_repositories import MySQLBrandRepository
from app.resources.brand_resource import BrandCreateResource, BrandUpdateResource, BrandReturnResource
from app.exceptions.database_errors import UnableToFindIdException
from typing import List
from uuid import UUID

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/brands", response_model=List[BrandReturnResource], description="Returns all brands.")
async def get_brands(session: Session = Depends(get_db)):
    error_message = "Failed to get brands"
    try:
        repository = MySQLBrandRepository(session)
        return service_brands.get_all(repository)
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

@router.get("/brand/{brand_id}", response_model=BrandReturnResource, description="Not been implemented yet.")
async def get_brand(brand_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get brand"
    try:
        raise NotImplementedError("Request GET '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdException as e:
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


@router.post("/brand", response_model=BrandReturnResource, description="Not been implemented yet.")
async def create_brand(brand_create_data: BrandCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create brand"
    try:
        raise NotImplementedError("Request POST '/brand' has not been implemented yet.")
    except UnableToFindIdException as e:
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

@router.put("/brand/{brand_id}", response_model=BrandReturnResource, description="Not been implemented yet.")
async def update_brand(brand_id: UUID, brand_update_data: BrandUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update brand"
    try:
        raise NotImplementedError("Request PUT '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdException as e:
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

@router.delete("/brand/{brand_id}", response_model=BrandReturnResource, description="Not been implemented yet.")
async def delete_brand(brand_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete brand"
    try:
        raise NotImplementedError("Request DELETE '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdException as e:
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