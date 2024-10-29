# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Body, Query, status

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

@router.get(
    path="/models",
    response_model=List[ModelReturnResource],
    response_description="Successfully retrieved list of models, returns: List[ModelReturnResource]",
    summary="Retrieve all Models.",
    description="Fetches all Models or all Models belonging to a brand from the MySQL database and returns a list of 'ModelReturnResource'."
)
async def get_models(brand_id: Optional[UUID] = Query(default=None, description="The UUID of the brand, to retrieve models belonging to that brand."),
                     session: Session = Depends(get_db)):
    error_message = "Failed to get models from the MySQL database"
    try:
        if brand_id is not None:
            brand_id = str(brand_id)
        return service_models.get_all(
            model_repository=MySQLModelRepository(session),
            brand_repository=MySQLBrandRepository(session),
            brand_id=brand_id
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

@router.get(
    path="/model/{model_id}",
    response_model=ModelReturnResource,
    response_description="Successfully retrieved a model, returns: ModelReturnResource",
    summary="Retrieve a Model by ID.",
    description="Fetches a Model by ID from the MySQL database by giving a UUID in the path for the model and returns it as a 'ModelReturnResource'."
)
async def get_model(model_id: UUID = Path(..., description="The UUID of the model to retrieve."),
                    session: Session = Depends(get_db)):
    error_message = "Failed to get model from the MySQL database"
    try:
        return service_models.get_by_id(
            repository=MySQLModelRepository(session),
            model_id=str(model_id)
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
    path="/model",
    response_model=ModelReturnResource,
    response_description="Successfully created a model, returns: ModelReturnResource.",
    summary="Create a Model.",
    description="Creates a Model within the MySQL database by giving a request body 'ModelCreateResource' and returns it as a 'ModelReturnResource'."
)
async def create_model(model_create_data: ModelCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create model within the MySQL database"
    try:
        raise NotImplementedError("Request POST '/mysql/model' has not been implemented yet.")
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
    path="/model/{model_id}",
    response_model=ModelReturnResource,
    response_description="Successfully updated a model, returns: ModelReturnResource.",
    summary="Update a Model - NOT BEEN IMPLEMENTED YET.",
    description="Updates a Model within the MySQL database by giving a UUID in the path for the model and by giving a request body 'ModelUpdateResource' and returns it as a 'ModelReturnResource'."
)
async def update_model(model_id: UUID = Path(..., description="The UUID of the model to update."),
                       model_update_data: ModelUpdateResource = Body(..., title="ModelUpdateResource"),
                       session: Session = Depends(get_db)):
    error_message = "Failed to update model within the MySQL database"
    try:
        raise NotImplementedError("Request PUT '/mysql/model/{model_id}' has not been implemented yet.")
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

@router.delete(
    path="/model/{model_id}",
    response_model=ModelReturnResource,
    response_description="Successfully deleted a model, returns: ModelReturnResource.",
    summary="Delete a Model - NOT BEEN IMPLEMENTED YET.",
    description="Deletes a Model within the MySQL database by giving a UUID in the path for the model and returns it as a 'ModelReturnResource'."
)
async def delete_model(model_id: UUID = Path(..., description="The UUID of the model to delete."),
                       session: Session = Depends(get_db)):
    error_message = "Failed to delete model within the MySQL database"
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