# External Library imports
from uuid import UUID
from typing import List, Optional
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status

# Internal library imports
from db import Session, get_db as get_db_session
from app.services import accessories_service as service
from app.exceptions.database_errors import UnableToFindIdError
from app.core.security import TokenPayload, get_current_mysql_sales_person_token
from app.repositories.accessory_repositories import (
    AccessoryReturnResource,
    MySQLAccessoryRepository
)

router: APIRouter = APIRouter()


def get_db():
    with get_db_session() as session:
        yield session


@router.get(
    path="/accessories",
    response_model=List[AccessoryReturnResource],
    response_description=
    """
    Successfully retrieved a list of accessories.
    Returns: List[AccessoryReturnResource].
    """,
    summary="Retrieve Accessories - Requires authorization token in header.",
    description=
    """
    Retrieves all or a limited amount of Accessories from the 
    MySQL database and returns a list of 'AccessoryReturnResource'.
    """
)
async def get_accessories(
        limit: Optional[int] = Query(
            default=None, ge=1,
            description=
            """
            Set a limit for the amount of accessories that is returned.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get accessories from the MySQL database"
    try:
        return service.get_all(
            repository=MySQLAccessoryRepository(session),
            accessory_limit=limit
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
    path="/accessory/{accessory_id}",
    response_model=AccessoryReturnResource,
    response_description=
    """
    Successfully retrieved an accessory.
    Returns: AccessoryReturnResource.
    """,
    summary="Retrieve an Accessory by ID - Requires authorization token in header.",
    description=
    """
    Retrieves an Accessory by ID from the MySQL database 
    by giving a UUID in the path for the accessory and 
    returns it as an 'AccessoryReturnResource'.
    """
)
async def get_accessory(
        accessory_id: UUID = Path(
            default=...,
            description=
            """
            The UUID of the accessory to retrieve.
            """
        ),
        current_token: TokenPayload = Depends(get_current_mysql_sales_person_token),
        session: Session = Depends(get_db)
):
    error_message = "Failed to get accessory from the MySQL database"
    try:
        return service.get_by_id(
            repository=MySQLAccessoryRepository(session),
            accessory_id=str(accessory_id)
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
