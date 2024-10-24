from fastapi import APIRouter, Depends, HTTPException, status
from db import Session, get_db as get_db_session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions.database_errors import UnableToFindIdError
from app.services import service_cars
from app.resources.car_resource import CarCreateResource, CarUpdateResource, CarReturnResource
from app.repositories.car_repositories import MySQLCarRepository
from app.repositories.customer_repositories import MySQLCustomerRepository
from app.repositories.sales_person_repositories import MySQLSalesPersonRepository
from app.repositories.model_repositories import MySQLModelRepository
from app.repositories.color_repositories import MySQLColorRepository
from app.repositories.accessory_repositories import MySQLAccessoryRepository
from app.repositories.insurance_repository import MySQLInsuranceRepository

from typing import Optional, List
from uuid import UUID


router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/cars", response_model=List[CarReturnResource], description="Returns all cars there are or from a given customer and/or sales person id.")
async def get_cars(customer_id: Optional[UUID] = None, sales_person_id: Optional[UUID] = None, session: Session = Depends(get_db)):
    error_message = "Failed to get cars"
    try:
        car_repository = MySQLCarRepository(session)
        customer_repository = MySQLCustomerRepository(session)
        sales_person_repository = MySQLSalesPersonRepository(session)
        if customer_id is not None:
            customer_id = str(customer_id)
        if sales_person_id is not None:
            sales_person_id = str(sales_person_id)
        return service_cars.get_all(
            car_repository,
            customer_repository,
            sales_person_repository,
            customer_id,
            sales_person_id)

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

@router.get("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def get_car(car_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to get car"
    try:
        return service_cars.get_by_id(MySQLCarRepository(session), str(car_id))
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


@router.post("/car", response_model=CarReturnResource, description="Creates a car in the database.")
async def create_car(car_create_data: CarCreateResource, session: Session = Depends(get_db)):
    error_message = "Failed to create car"
    try:
        return service_cars.create(
            car_repository=MySQLCarRepository(session),
            customer_repository=MySQLCustomerRepository(session),
            sales_person_repository=MySQLSalesPersonRepository(session),
            model_repository=MySQLModelRepository(session),
            color_repository=MySQLColorRepository(session),
            accessory_repository=MySQLAccessoryRepository(session),
            insurance_repository=MySQLInsuranceRepository(session),
            car_create_data=car_create_data)
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

@router.put("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def update_car(car_id: UUID, car_update_data: CarUpdateResource, session: Session = Depends(get_db)):
    error_message = "Failed to update car"
    try:
        raise NotImplementedError("Request PUT '/car/{car_id}' has not been implemented yet.")
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

@router.delete("/car/{car_id}", response_model=CarReturnResource, description="Not been implemented yet.")
async def delete_car(car_id: UUID, session: Session = Depends(get_db)):
    error_message = "Failed to delete car"
    try:
        raise NotImplementedError("Request DELETE '/car/{car_id}' has not been implemented yet.")
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