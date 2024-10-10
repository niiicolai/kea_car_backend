from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_sales_people
from app.resources.sales_person_resource import SalesPersonCreateResource, SalesPersonUpdateResource, SalesPersonReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter(tags=['Sales People'])

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/sales-people", response_model=list[SalesPersonReturnResource])
async def get_sales_people(session: Session = Depends(get_db)):
    error_message = "Failed to get sales people"
    try:
        raise NotImplementedError("Request GET '/sales-people' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/sales-person/{sales_person_id}", response_model=SalesPersonReturnResource)
async def get_sales_person(sales_person_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get sales person"
    try:
        raise NotImplementedError("Request GET '/sales-person/{sales_person_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/sales-person", response_model=SalesPersonReturnResource)
async def create_sales_person(sales_person_create_data: SalesPersonCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create sales person"
    try:
        raise NotImplementedError("Request POST '/sales-person' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/sales-person/{sales_person_id}", response_model=SalesPersonReturnResource)
async def update_sales_person(sales_person_id: int, sales_person_update_data: SalesPersonUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update sales person"
    try:
        raise NotImplementedError("Request PUT '/sales-person/{sales_person_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/sales-person/{sales_person_id}", response_model=SalesPersonReturnResource)
async def delete_sales_person(sales_person_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete sales person"
    try:
        raise NotImplementedError("Request DELETE '/sales-person/{sales_person_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))