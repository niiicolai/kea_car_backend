
from typing import Callable
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError

def error_handler(callback: Callable) -> Callable:
    try:
        return callback()
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"SQL Error caught: {e}")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(f"Validation Error caught: {e}")
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught.")
        )
        