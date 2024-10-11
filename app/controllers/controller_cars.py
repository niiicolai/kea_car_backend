from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_cars
from app.resources.car_resource import CarCreateResource, CarUpdateResource, CarReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter(tags=["Cars"])

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/cars", response_model=list[CarReturnResource], description="Not been implemented yet.")
async def get_cars(session: Session = Depends(get_db)):
    error_message = "Failed to get cars"
    try:
        raise NotImplementedError("Request GET '/cars' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def get_car(car_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get car"
    try:
        raise NotImplementedError("Request GET '/car/{car_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/car", response_model=CarReturnResource, description="Not been implemented yet.")
async def create_car(car_create_data: CarCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create car"
    try:
        raise NotImplementedError("Request POST '/car' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def update_car(car_id: int, car_update_data: CarUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update car"
    try:
        raise NotImplementedError("Request PUT '/car/{car_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def delete_car(car_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete car"
    try:
        raise NotImplementedError("Request DELETE '/car/{car_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))