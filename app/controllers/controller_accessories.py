from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_accessories
from app.resources.accessory_resource import AccessoryCreateResource, AccessoryUpdateResource, AccessoryReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


accessories_router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@accessories_router.get("/accessories", response_model=list[AccessoryReturnResource])
async def get_accessories(session: Session = Depends(get_db)):
    error_message = "Failed to get accessories"
    try:
        raise NotImplementedError("Request GET '/accessories' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@accessories_router.get("/accessory/{accessory_id}", response_model=AccessoryReturnResource)
async def get_accessory(accessory_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get accessory"
    try:
        raise NotImplementedError("Request GET '/accessory/{accessory_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@accessories_router.post("/accessory", response_model=AccessoryReturnResource)
async def create_accessory(accessory_create_data: AccessoryCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create accessory"
    try:
        raise NotImplementedError("Request POST '/accessory' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@accessories_router.put("/accessory/{accessory_id}", response_model=AccessoryReturnResource)
async def update_accessory(accessory_id: int, accessory_update_data: AccessoryUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update accessory"
    try:
        raise NotImplementedError("Request PUT '/accessory/{accessory_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@accessories_router.delete("/accessory/{accessory_id}", response_model=AccessoryReturnResource)
async def delete_accessory(accessory_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete accessory"
    try:
        raise NotImplementedError("Request DELETE '/accessory/{accessory_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))