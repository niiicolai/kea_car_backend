# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

# Internal library imports
from db import Neo4jSession, get_neo4j
from app.services import models_service as service
from app.controllers.error_handler import error_handler
from app.repositories.brand_repositories import Neo4jBrandRepository
from app.repositories.model_repositories import (
    Neo4jModelRepository,
    ModelReturnResource
)

router: APIRouter = APIRouter()

def get_db():  # pragma: no cover
    with get_neo4j() as session:
        yield session

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
    Retrieves all or a limited amount of Models from the Neo4j database 
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
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get models from the Neo4j database",
        callback=lambda: service.get_all(
            model_repository=Neo4jModelRepository(session),
            brand_repository=Neo4jBrandRepository(session),
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
    Retrieves a Model by ID from the Neo4j database 
    by giving a UUID in the path for the model 
    and returns it as a 'ModelReturnResource'.
    """
)
async def get_model(
        model_id: UUID = Path(
            default=...,
            description="""The UUID of the model to retrieve."""
        ),
        session: Neo4jSession = Depends(get_db)
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get model from the Neo4j database",
        callback=lambda: service.get_by_id(
            repository=Neo4jModelRepository(session),
            model_id=str(model_id)
        )
    )
