from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_insurance_types
from app.resources.insurance_type_resource import InsuranceTypeCreateResource, InsuranceTypeUpdateResource, InsuranceTypeReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/insurance-types", response_model=list[InsuranceTypeReturnResource])
async def get_inurance_types(session: Session = Depends(get_db)):
    error_message = "Failed to get insurance types"
    try:
        raise NotImplementedError("Request GET '/insurance-types' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/insurance-type/{insurance_type_id}", response_model=InsuranceTypeReturnResource)
async def get_insurance_type(insurance_type_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get insurance type"
    try:
        raise NotImplementedError("Request GET '/insurance-type/{insurance_type_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/insurance-type", response_model=InsuranceTypeReturnResource)
async def create_insurance_type(insurance_type_create_data: InsuranceTypeCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create insurance type"
    try:
        raise NotImplementedError("Request POST '/insurance-type' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/insurance-type", response_model=InsuranceTypeUpdateResource)
async def update_insurance_type(insurance_type_update_data: InsuranceTypeUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update insurance type"
    try:
        raise NotImplementedError("Request PUT '/insurance-type' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/insurance-type/{insurance_type_id}", response_model=InsuranceTypeCreateResource)
async def delete_insurance_type(insurance_type_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete insurance type"
    try:
        raise NotImplementedError("Request DELETE '/insurance-type/{insurance_type_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))