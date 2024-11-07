# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, Form, HTTPException, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import sales_people_service as service
from app.exceptions.invalid_credentials_errors import IncorrectCredentialError
from app.exceptions.database_errors import UnableToFindIdError, AlreadyTakenFieldValueError
from app.repositories.sales_person_repositories import (
    MySQLSalesPersonRepository,
    SalesPersonReturnResource,
    SalesPersonCreateResource,
    SalesPersonLoginResource
)


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.post(
    path="/token",
    response_model=service.Token,
    response_description=
    """
    Successfully created a token.
    Returns: Token.
    """,
    summary="Create an Access Token for a Sales Person.",
    description=
    """
    Works the same as the '/mysql/login' endpoint, 
    but requires forms instead of a request body, 
    this endpoint is needed for the Swagger UI 
    can authorize access to endpoints 
    that needs authorization. Creates an Access Token 
    from a sales person within the MySQL database by 
    giving Forms for the email and password of that 
    sales person and returns a 'Token'.
    """
)
async def login_for_access_token(
        username: str = Form(
            default=...,
            description=
            """
            The email of the sales person.
            """
        ),
        password: str = Form(
            default=...,
            description=
            """
            The password of the sales person.
            """
        ),
        session: Session = Depends(get_db)
):
    error_message = "Failed to create an access token from a Sales Person in the MySQL database"
    try:
        return service.login(
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
    response_model=service.Token,
    response_description=
    """
    Successfully logged in.
    Returns: Token.
    """,
    summary="Logs in as a Sales Person.",
    description=
    """
    Works the same as the '/mysql/token' endpoint, 
    but requires a request body instead of forms, 
    this endpoint is to make it easier for the frontend 
    to log in and access endpoints that needs authorization. 
    Logs in as a sales person within the MySQL database by 
    giving a request body 'SalesPersonLoginResource' 
    of that sales person and returns a 'Token'.
    """
)
async def login(
        sales_person_login_data: SalesPersonLoginResource,
        session: Session = Depends(get_db)
):
    error_message = "Failed to login from a Sales Person in the MySQL database"
    try:
        return service.login(
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
    response_description=
    """
    Successfully retrieved a list of sales people.
    Returns: List[SalesPersonReturnResource].
    """,
    summary="Retrieve Sales People.",
    description=
    """
    Retrieves all or a limited amount of Sales People from the MySQL 
    database and returns a list of 'SalesPersonReturnResource'.
    """
)
async def get_sales_people(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description=
            """
            Set a limit for the amount of sales people that is returned.
            """
        ),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get sales people from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLSalesPersonRepository(session),
            sales_people_limit=limit
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
    response_description=
    """
    Successfully retrieved a sales person.
    Returns: SalesPersonReturnResource.
    """,
    summary="Retrieve a Sales Person by ID.",
    description=
    """
    Retrieves a Sales Person by ID from the MySQL database 
    by giving a UUID in the path for the sales person 
    and returns it as a 'SalesPersonReturnResource'.
    """
)
async def get_sales_person(
        sales_person_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the sales person to retrieve.
            """
        ),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get sales person from the MySQL database"
    try:
        return service.get_by_id(
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
    response_description=
    """
    Successfully created a sales person.
    Returns: SalesPersonReturnResource.
    """,
    summary="Create a Sales Person.",
    description=
    """
    Creates a Sales Person within the MySQL database 
    by giving a request body 'SalesPersonCreateResource' 
    and returns it as a 'SalesPersonReturnResource'.
    """
)
async def create_sales_person(
        sales_person_create_data: SalesPersonCreateResource,
        session: Session = Depends(get_db)
):
    error_message = "Failed to create sales person within the MySQL database"
    try:
        return service.create(
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
