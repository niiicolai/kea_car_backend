# External Library imports
from uuid import UUID
from typing import List
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, Form, HTTPException, Path, Body, status

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

@router.post(
    path="/token",
    response_model=service_sales_people.Token,
    response_description="Successfully created a token, returns: Token.",
    summary="Create an Access Token for a Sales Person.",
    description="Works the same as the '/mysql/login' endpoint, but requires forms in stead of a request body, this endpoint is needed for the Swagger UI can authorize access to endpoints that needs authorization. Creates an Access Token from a sales person within the MySQL database by giving Forms for the email and password of that sales person and returns a 'Token'."
)
async def login_for_access_token(
        username: str = Form(..., description="The email of the sales person."),
        password: str = Form(..., description="The password of the sales person."),
        session: Session = Depends(get_db)
):
    error_message = "Failed to create an access token from a Sales Person in the MySQL database"
    try:
        return service_sales_people.login(
            repository=MySQLSalesPersonRepository(session),
            sales_person_login_data=SalesPersonLoginResource(email=username, password=password)
        )
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

@router.post(
    path="/login",
    response_model=service_sales_people.Token,
    response_description="Successfully logged in, returns: Token.",
    summary="Logs in as a Sales Person.",
    description="Works the same as the '/mysql/token' endpoint, but requires a request body in stead of forms, this endpoint is to make it easier for the frontend to log in and access endpoints that needs authorization. Logs in as a sales person within the MySQL database by giving a request body 'SalesPersonLoginResource' of that sales person and returns a 'Token'."
)
async def login(sales_person_login_data: SalesPersonLoginResource, session: Session = Depends(get_db)):
    error_message = "Failed to login from a Sales Person in the MySQL database"
    try:
        return service_sales_people.login(
            repository=MySQLSalesPersonRepository(session),
            sales_person_login_data=sales_person_login_data
        )
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


@router.get(
    path="/sales_people",
    response_model=List[SalesPersonReturnResource],
    response_description="Successfully retrieved list of sales people, returns: List[SalesPersonReturnResource]",
    summary="Retrieve all Sales People.",
    description="Fetches all Sales People from the MySQL database and returns a list of 'SalesPersonReturnResource'."
)
async def get_sales_people(session: Session = Depends(get_db)):
    error_message = "Failed to get sales people from the MySQL database"
    try:
        return service_sales_people.get_all(
            repository=MySQLSalesPersonRepository(session)
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

@router.get(
    path="/sales_person/{sales_person_id}",
    response_model=SalesPersonReturnResource,
    response_description="Successfully retrieved a sales person, returns: SalesPersonReturnResource",
    summary="Retrieve a Sales Person by ID.",
    description="Fetches a Sales Person by ID from the MySQL database by giving a UUID in the path for the sales person and returns it as a 'SalesPersonReturnResource'."
)
async def get_sales_person(sales_person_id: UUID = Path(..., description="The UUID of the sales person to retrieve."),
                           session: Session = Depends(get_db)):
    error_message = "Failed to get sales person from the MySQL database"
    try:
        return service_sales_people.get_by_id(
            repository=MySQLSalesPersonRepository(session),
            sales_person_id=str(sales_person_id)
        )
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


@router.post(
    path="/sales_person",
    response_model=SalesPersonReturnResource,
    response_description="Successfully created a sales person, returns: SalesPersonReturnResource.",
    summary="Create a Sales Person.",
    description="Creates a Sales Person within the MySQL database by giving a request body 'SalesPersonCreateResource' and returns it as a 'SalesPersonReturnResource'."
)
async def create_sales_person(sales_person_create_data: SalesPersonCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create sales person within the MySQL database"
    try:
        return service_sales_people.create(
            repository=MySQLSalesPersonRepository(session),
            sales_person_create_data=sales_person_create_data
        )
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

@router.put(
    path="/sales_person/{sales_person_id}",
    response_model=SalesPersonReturnResource,
    response_description="Successfully updated a sales person, returns: SalesPersonReturnResource.",
    summary="Update a Sales Person - NOT BEEN IMPLEMENTED YET.",
    description="Updates a Sales Person within the MySQL database by giving a UUID in the path for the sales person and by giving a request body 'SalesPersonUpdateResource' and returns it as a 'SalesPersonReturnResource'."
)
async def update_sales_person(sales_person_id: UUID = Path(..., description="The UUID of the sales person to update."),
                              sales_person_update_data: SalesPersonUpdateResource = Body(..., title="SalesPersonUpdateResource"),
                              session: Session = Depends(get_db)):
    error_message = "Failed to update sales person within the MySQL database"
    try:
        raise NotImplementedError("Request PUT '/mysql/sales-person/{sales_person_id}' has not been implemented yet.")
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

@router.delete(
    path="/sales_person/{sales_person_id}",
    response_model=SalesPersonReturnResource,
    response_description="Successfully deleted a sales person, returns: SalesPersonReturnResource.",
    summary="Delete a Sales Person - NOT BEEN IMPLEMENTED YET.",
    description="Deletes a Sales Person within the MySQL database by giving a UUID in the path for the sales person and returns it as a 'SalesPersonReturnResource'."
)
async def delete_sales_person(sales_person_id: UUID = Path(..., description="The UUID of the sales person to delete."),
                              session: Session = Depends(get_db)):
    error_message = "Failed to delete sales person within the MySQL database"
    try:
        raise NotImplementedError("Request DELETE '/mysql/sales_person/{sales_person_id}' has not been implemented yet.")
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