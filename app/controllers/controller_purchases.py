from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_purchases
from app.resources.purchase_resource import PurchaseCreateResource, PurchaseUpdateResource, PurchaseReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/purchases", response_model=list[PurchaseReturnResource], description="Returns all purchases.")
async def get_purchases(session: Session = Depends(get_db)):
    error_message = "Failed to get purchases"
    try:
        purchases = service_purchases.get_all(session)
        return [purchase.as_resource() for purchase in purchases]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/purchase/{purchase_id}", response_model=PurchaseReturnResource, description="Not been implemented yet.")
async def get_purchase(purchase_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get purchase"
    try:
        raise NotImplementedError("Request GET '/purchase/{purchase_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/purchase", response_model=PurchaseReturnResource, description="Not been implemented yet.")
async def create_purchase(purchase_create_data: PurchaseCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create purchase"
    try:
        raise NotImplementedError("Request POST '/purchase' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/purchase/{purchase_id}", response_model=PurchaseReturnResource, description="Not been implemented yet.")
async def update_purchase(purchase_id: int, purchase_update_data: PurchaseUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update purchase"
    try:
        raise NotImplementedError("Request PUT '/purchase/{purchase_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/purchase/{purchase_id}", response_model=PurchaseReturnResource, description="Not been implemented yet.")
async def delete_purchase(purchase_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete purchase"
    try:
        raise NotImplementedError("Request DELETE '/purchase/{purchase_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))