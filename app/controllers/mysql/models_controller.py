# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import models_service as service
from app.controllers.error_handler import error_handler
from app.repositories.brand_repositories import MySQLBrandRepository
from app.repositories.model_repositories import (
    MySQLModelRepository,
    ModelReturnResource
)

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session
        session.commit()

@router.get(
    path="/models",
    response_model=List[ModelReturnResource],
    response_description=
    """
    Successfully retrieved a list of models.
    Returns: List[ModelReturnResource].
    """,
    summary="Retrieve Models.",
    description=
    """
    Retrieves all or a limited amount of Models from the MySQL database 
    potentially filtered by models belonging to a brand 
    and returns a list of 'ModelReturnResource'.
    """
)
async def get_models(
        brand_id: Optional[UUID] = Query(
            default=None,
            description="""The UUID of the brand, to retrieve models belonging to that brand."""
        ),
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of models that is returned."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get models from the MySQL database",
        callback=lambda: service.get_all(
            model_repository=MySQLModelRepository(session),
            brand_repository=MySQLBrandRepository(session),
            brand_id=None if not brand_id else str(brand_id),
            models_limit=limit
        )
    )


@router.get(
    path="/model/{model_id}",
    response_model=ModelReturnResource,
    response_description=
    """
    Successfully retrieved a model.
    Returns: ModelReturnResource.
    """,
    summary="Retrieve a Model by ID.",
    description=
    """
    Retrieves a Model by ID from the MySQL database 
    by giving a UUID in the path for the model 
    and returns it as a 'ModelReturnResource'.
    """
)
async def get_model(
        model_id: UUID = Path(
            default=...,
            description="""The UUID of the model to retrieve."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get model from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLModelRepository(session),
            model_id=str(model_id)
        )
    )
