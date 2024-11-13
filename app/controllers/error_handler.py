# External Library imports
from typing import Callable
import logging
import os
from dotenv import load_dotenv

from fastapi import HTTPException, status

# Internal library imports
from app.exceptions.invalid_credentials_errors import IncorrectCredentialError
from app.exceptions.database_errors import (
    UnableToFindIdError,
    UnableToFindEntityError,
    AlreadyTakenFieldValueError,
    PurchaseDeadlineHasPastError,
    TheColorIsNotAvailableInModelToGiveToCarError,
    UnableToDeleteCarWithoutDeletingPurchaseTooError,
)


"""
# Description:
The error handler will catch exceptions and raise an HTTPException 
with the appropriate status code and message.


# Usage example:
```
return error_handler(error_message: str, lambda: service.get_all(repository=MySQLColorRepository(session), colors_limit=limit))
```
"""
def error_handler(error_message: str, callback: Callable):
    try:
        return callback()

    except UnableToFindIdError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(f"{error_message}: {e}")
        )

    except UnableToFindEntityError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except AlreadyTakenFieldValueError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except IncorrectCredentialError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except TheColorIsNotAvailableInModelToGiveToCarError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except UnableToDeleteCarWithoutDeletingPurchaseTooError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except PurchaseDeadlineHasPastError as e:
        log_error(error_message, e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(f"{error_message}: {e}")
        )

    except Exception as e:
        log_error(error_message, e)
        load_dotenv()
        # Raise a generic internal server error for the client
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught: {error_message}. {e}. {os.getenv('SECRET_KEY')}")
        )

def log_error(error_message: str, error: Exception):
    # Log internal server errors for debugging
    logging.error(f"{error.__class__.__name__} Was Caught.\n{error_message}:\n{error}", exc_info=True)
