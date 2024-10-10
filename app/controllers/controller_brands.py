from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_brands
from app.resources.brand_resource import BrandCreateResource, BrandUpdateResource, BrandReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter(tags=['Brands'])

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/brands", response_model=list[BrandReturnResource])
async def get_brands(session: Session = Depends(get_db)):
    error_message = "Failed to get brands"
    try:
        brands = service_brands.get_all(session)
        return [brand.as_resource() for brand in brands]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/brand/{brand_id}", response_model=BrandReturnResource)
async def get_brand(brand_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get brand"
    try:
        raise NotImplementedError("Request GET '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/brand", response_model=BrandReturnResource)
async def create_brand(brand_create_data: BrandCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create brand"
    try:
        raise NotImplementedError("Request POST '/brand' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/brand/{brand_id}", response_model=BrandReturnResource)
async def update_brand(brand_id: int, brand_update_data: BrandUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update brand"
    try:
        raise NotImplementedError("Request PUT '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/brand/{brand_id}", response_model=BrandReturnResource)
async def delete_brand(brand_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete brand"
    try:
        raise NotImplementedError("Request DELETE '/brand/{brand_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))