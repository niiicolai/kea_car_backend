from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_models
from app.resources.model_resource import ModelCreateResource, ModelUpdateResource, ModelReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter(tags=['Models'])

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/models", response_model=list[ModelReturnResource], description="Returns all models or all models from a given brand ID.")
async def get_models(brand_id: Optional[int] = None, session: Session = Depends(get_db)):
    error_message = "Failed to get models"
    try:
        models = service_models.get_all(brand_id, session)
        return [model.as_resource() for model in models]
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/model/{model_id}", response_model=ModelReturnResource, description="Not been implemented yet.")
async def get_model(model_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get model"
    try:
        raise NotImplementedError("Request GET '/model/{model_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/model", response_model=ModelReturnResource, description="Not been implemented yet.")
async def create_model(model_create_data: ModelCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create model"
    try:
        raise NotImplementedError("Request POST '/model' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/model/{model_id}", response_model=ModelReturnResource, description="Not been implemented yet.")
async def update_model(model_id: int, model_update_data: ModelUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update model"
    try:
        raise NotImplementedError("Request PUT '/model/{model_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/model/{model_id}", response_model=ModelReturnResource, description="Not been implemented yet.")
async def delete_model(model_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete model"
    try:
        raise NotImplementedError("Request DELETE '/model/{model_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))