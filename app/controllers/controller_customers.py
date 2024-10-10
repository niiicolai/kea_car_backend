from fastapi import APIRouter, Depends, HTTPException
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_customers
from app.resources.customer_resource import CustomerCreateResource, CustomerUpdateResource, CustomerReturnResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError


router: APIRouter = APIRouter(tags=["Customers"])

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/customers", response_model=list[CustomerReturnResource])
async def get_customers(session: Session = Depends(get_db)):
    error_message = "Failed to get customers"
    try:
        customers = service_customers.get_all(session)
        return [customer.as_resource() for customer in customers]
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/customer/{customer_id}", response_model=CustomerReturnResource)
async def get_customer(customer_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to get customer"
    try:
        return service_customers.get_by_id(session, customer_id).as_resource()
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.post("/customer", response_model=CustomerReturnResource)
async def create_customer(customer_create_data: CustomerCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create customer"
    try:
        return service_customers.create(session, customer_create_data).as_resource()
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/customer/{customer_id}", response_model=CustomerReturnResource)
async def update_customer(customer_id: int, customer_update_data: CustomerUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update customer"
    try:
        raise NotImplementedError("Request PUT '/customer/{customer_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.delete("/customer/{customer_id}", response_model=CustomerReturnResource)
async def delete_customer(customer_id: int, session: Session = Depends(get_db)):
    error_message = "Failed to delete customer"
    try:
        raise NotImplementedError("Request DELETE '/customer/{customer_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))