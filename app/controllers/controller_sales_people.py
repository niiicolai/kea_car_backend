# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, Form, HTTPException, status

# Internal library imports
from app.services import service_sales_people
from db import Session, get_db as get_db_session
from app.exceptions.invalid_credentials_errors import IncorrectCredentialError
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository, SalesPersonReturnResource, SalesPersonCreateResource

# These imports, except SalesPersonLoginResource, should come from repository, but the repo is not made for these resources,
# but to let swagger give examples of what the endpoints should do, we import them here
from app.resources.sales_person_resource import SalesPersonUpdateResource, SalesPersonLoginResource

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.post("/token", response_model=service_sales_people.Token, description="Create a Token for a Sales Person.")
async def login_for_access_token(
        username: str = Form(..., description="The email of the sales person."),
        password: str = Form(..., description="The password of the sales person."),
        session: Session = Depends(get_db)
):
    error_message = "Failed to create access token"
    try:
        repository = MySQLSalesPersonRepository(session)
        return service_sales_people.login(repository, SalesPersonLoginResource(email=username, password=password))
    except IncorrectCredentialError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}"),
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )

@router.post("/login", response_model=service_sales_people.Token, description="Logs in as a Sales Person.")
async def login(sales_person_login_data: SalesPersonLoginResource, session: Session = Depends(get_db)):
    error_message = "Failed to login"
    try:
        repository = MySQLSalesPersonRepository(session)
        return service_sales_people.login(repository, sales_person_login_data)
    except IncorrectCredentialError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}"),
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )


@router.get("/sales_people", response_model=List[SalesPersonReturnResource], description="Returns all Sales People.")
async def get_sales_people(session: Session = Depends(get_db)):
    error_message = "Failed to get sales people"
    try:
        repository = MySQLSalesPersonRepository(session)
        return service_sales_people.get_all(repository)
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )

@router.get("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Returns a Sales Person by id.")
async def get_sales_person(sales_person_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get sales person"
    try:
        repository = MySQLSalesPersonRepository(session)
        return service_sales_people.get_by_id(repository, str(sales_person_id))
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )


@router.post("/sales_person", response_model=SalesPersonReturnResource, description="Create a new sales person.")
async def create_sales_person(sales_person_create_data: SalesPersonCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create sales person"
    try:
        repository = MySQLSalesPersonRepository(session)
        return service_sales_people.create(repository, sales_person_create_data)
    except AlreadyTakenFieldValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}"),
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )

@router.put("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Not been implemented yet.")
async def update_sales_person(sales_person_id: UUID, sales_person_update_data: SalesPersonUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update sales person"
    try:
        raise NotImplementedError("Request PUT '/sales-person/{sales_person_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )

@router.delete("/sales_person/{sales_person_id}", response_model=SalesPersonReturnResource, description="Not been implemented yet.")
async def delete_sales_person(sales_person_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete sales person"
    try:
        raise NotImplementedError("Request DELETE '/sales-person/{sales_person_id}' has not been implemented yet.")
    except UnableToFindIdError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"Unable To Find Id Error caught. {error_message}: {e}")
        )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught. {error_message}: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught. {error_message}: {e}")
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught. {error_message}: {e}")
        )