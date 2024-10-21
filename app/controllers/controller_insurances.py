from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_insurances
from app.resources.insurance_resource import InsuranceCreateResource, InsuranceUpdateResource, InsuranceReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from typing import List
from uuid import UUID


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/insurances", response_model=List[InsuranceReturnResource], description="Returns all insurances.")
async def get_insurances(session: Session = Depends(get_db)):
    error_message = "Failed to get insurances"
    try:
        insurances = service_insurances.get_all(session)
        return [insurance.as_resource() for insurance in insurances]
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/insurance/{insurance_id}", response_model=InsuranceReturnResource, description="Not been implemented yet.")
async def get_insurance(insurance_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get insurance"
    try:
        raise NotImplementedError("Request GET '/insurance/{insurance_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/insurance", response_model=InsuranceReturnResource, description="Not been implemented yet.")
async def create_insurance(insurance_create_data: InsuranceCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create insurance"
    try:
        raise NotImplementedError("Request POST '/insurance' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/insurance/{insurance_id}", response_model=InsuranceUpdateResource, description="Not been implemented yet.")
async def update_insurance(insurance_id: UUID, insurance_update_data: InsuranceUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update insurance"
    try:
        raise NotImplementedError("Request PUT '/insurance/{insurance_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/insurance/{insurance_id}", response_model=InsuranceCreateResource, description="Not been implemented yet.")
async def delete_insurance(insurance_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete insurance"
    try:
        raise NotImplementedError("Request DELETE '/insurance/{insurance_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))