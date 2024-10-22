from fastapi import APIRouter, Depends, Form, HTTPException, status
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.services import service_sales_people
from app.repositories.sales_person_repositories import SalesPersonRepository, MySQLSalesPersonRepository
from app.resources.sales_person_resource import SalesPersonCreateResource, SalesPersonUpdateResource, SalesPersonReturnResource, SalesPersonLoginResource
from app.exceptions.unable_to_find_id_error import UnableToFindIdError
from app.core.security import Token, verify_sales_person_email, verify_password, create_access_token
from typing import List
from uuid import UUID

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.post("/token", response_model=Token, description="Create a Token for a Sales Person.")
async def login_for_access_token(
        username: str = Form(..., examples=["hans@gmail.com"], description="The email of the sales person."),
        password: str = Form(..., examples=["hans123"], description="The password of the sales person."),
        session: Session = Depends(get_db)
):
    error_message = "Failed to create access token"
    repository: SalesPersonRepository = MySQLSalesPersonRepository(session)

    verified_email = verify_sales_person_email(username, repository)
    if verified_email is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}. Incorrect email: {username}"),
        )
    sales_person_resource, hashed_password = verified_email
    verified_password = verify_password(password, hashed_password)
    if not verified_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}. Incorrect password: {password}"),
        )

    return create_access_token(sales_person_resource)

@router.post("/login", response_model=SalesPersonReturnResource, description="Logs in as a Sales Person.")
async def login(sales_person_login_data: SalesPersonLoginResource, session: Session = Depends(get_db)):
    error_message = "Failed to login"
    try:
        sales_person = service_sales_people.login(sales_person_login_data, session)
        return sales_person.as_resource()
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))


@router.get("/sales_people", response_model=List[SalesPersonReturnResource], description="Returns all Sales People.")
async def get_sales_people(session: Session = Depends(get_db)):
    error_message = "Failed to get sales people"
    try:
        sales_people = service_sales_people.get_all(session)
        return [sales_person.as_resource() for sales_person in sales_people]
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.get("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Not been implemented yet.")
async def get_sales_person(sales_person_id: UUID, session: Session = Depends(get_db)):
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


@router.post("/sales_person", response_model=SalesPersonReturnResource, description="Create a new sales person.")
async def create_sales_person(sales_person_create_data: SalesPersonCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create sales person"
    try:
        new_sales_person = service_sales_people.create(sales_person_create_data, session)
        return new_sales_person.as_resource()
    except UnableToFindIdError as e:
        raise HTTPException(status_code=404, detail=str(f"Unable To Find Id Error caught. {error_message}: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=422, detail=str(f"SQL Error caught. {error_message}: {e}"))
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(f"Validation Error caught. {error_message}: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Unknown Error caught. {error_message}: {e}"))

@router.put("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Not been implemented yet.")
async def update_sales_person(sales_person_id: UUID, sales_person_update_data: SalesPersonUpdateResource, session: Session = Depends(get_db)):
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

@router.delete("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Not been implemented yet.")
async def delete_sales_person(sales_person_id: UUID, session: Session = Depends(get_db)):
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