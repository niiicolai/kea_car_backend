# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, status

# Internal library imports
from app.services import service_models
from db import Session, get_db as get_db_session
from app.repositories.brand_repositories import MySQLBrandRepository
from app.repositories.model_repositories import MySQLModelRepository, ModelReturnResource
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError

# These imports should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.model_resource import ModelCreateResource, ModelUpdateResource

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/models", response_model=List[ModelReturnResource], description="Returns all models or all models from a given brand ID.")
async def get_models(brand_id: Optional[UUID] = None, session: Session = Depends(get_db)):
    error_message = "Failed to get models"
    try:
        if brand_id is not None:
            brand_id = str(brand_id)
        return service_models.get_all(MySQLModelRepository(session), MySQLBrandRepository(session), brand_id)
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
            detail=str(f"Unknown Error caught. {error_message}: {e}")
        )

@router.get("/model/{model_id}", response_model=ModelReturnResource, description="Returns one model by ID.")
async def get_model(model_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get model"
    try:
        return service_models.get_by_id(MySQLModelRepository(session), str(model_id))
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
            detail=str(f"Unknown Error caught. {error_message}: {e}")
        )


@router.post("/model", response_model=ModelReturnResource, description="Not been implemented yet.")
async def create_model(model_create_data: ModelCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create model"
    try:
        raise NotImplementedError("Request POST '/model' has not been implemented yet.")
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

@router.put("/model/{model_id}", response_model=ModelReturnResource, description="Not been implemented yet.")
async def update_model(model_id: UUID, model_update_data: ModelUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update model"
    try:
        raise NotImplementedError("Request PUT '/model/{model_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
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

@router.delete("/model/{model_id}", response_model=ModelReturnResource, description="Not been implemented yet.")
async def delete_model(model_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete model"
    try:
        raise NotImplementedError("Request DELETE '/model/{model_id}' has not been implemented yet.")
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