# External Library imports
from uuid import UUID
from typing import List, Optional
from fastapi import APIRouter, Depends, Form, Path, Query

# Internal library imports
from db import Session, get_db as get_db_session
from app.controllers.error_handler import error_handler
from app.services import sales_people_service as service
from app.core.security import get_current_sales_person_token
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
            description="""The email of the sales person."""
        ),
        password: str = Form(
            default=...,
            description="""The password of the sales person."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to create an access token for a Sales Person in the MySQL database",
        callback=lambda: service.login(
            repository=MySQLSalesPersonRepository(session),
            sales_person_login_data=SalesPersonLoginResource(
                email=username,
                password=password
            )
        )
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
    return error_handler(
        error_message="Failed to login for a Sales Person in the MySQL database",
        callback=lambda: service.login(
            repository=MySQLSalesPersonRepository(session),
            sales_person_login_data=sales_person_login_data
        )
    )


@router.get(
    path="/sales_people",
    response_model=List[SalesPersonReturnResource],
    response_description=
    """
    Successfully retrieved a list of sales people.
    Returns: List[SalesPersonReturnResource].
    """,
    summary="Retrieve Sales People - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Sales People from the MySQL 
    database and returns a list of 'SalesPersonReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_sales_people(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description="""Set a limit for the amount of sales people that is returned."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get sales people from the MySQL database",
        callback=lambda: service.get_all(
            repository=MySQLSalesPersonRepository(session),
            sales_people_limit=limit
        )
    )


@router.get(
    path="/sales_person/{sales_person_id}",
    response_model=SalesPersonReturnResource,
    response_description=
    """
    Successfully retrieved a sales person.
    Returns: SalesPersonReturnResource.
    """,
    summary="Retrieve a Sales Person by ID - Requires authorization token in header.",
    description=
    """
    Retrieves a Sales Person by ID from the MySQL database 
    by giving a UUID in the path for the sales person 
    and returns it as a 'SalesPersonReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def get_sales_person(
        sales_person_id: UUID = Path(
            default=...,
            description="""The UUID of the sales person to retrieve."""
        ),
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to get sales person from the MySQL database",
        callback=lambda: service.get_by_id(
            repository=MySQLSalesPersonRepository(session),
            sales_person_id=str(sales_person_id)
        )
    )


@router.post(
    path="/sales_person",
    response_model=SalesPersonReturnResource,
    response_description=
    """
    Successfully created a sales person.
    Returns: SalesPersonReturnResource.
    """,
    summary="Create a Sales Person - Requires authorization token in header.",
    description=
    """
    Creates a Sales Person within the MySQL database 
    by giving a request body 'SalesPersonCreateResource' 
    and returns it as a 'SalesPersonReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
async def create_sales_person(
        sales_person_create_data: SalesPersonCreateResource,
        session: Session = Depends(get_db)
):
    return error_handler(
        error_message="Failed to create sales person within the MySQL database",
        callback=lambda: service.create(
            repository=MySQLSalesPersonRepository(session),
            sales_person_create_data=sales_person_create_data
        )
    )
