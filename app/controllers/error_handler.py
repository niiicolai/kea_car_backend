
from typing import Callable
from fastapi import HTTPException, status
import logging

"""
# Description:
The error handler will catch exceptions and return a HTTPException 
with the appropriate status code and message.


# Usage with default configuration:
```
return error_handler(lambda: service.get_all(repository=MySQLColorRepository(session), colors_limit=limit))
```


# Usage with custom exceptions:
```
return error_handler(lambda: service.get_by_id(repository=MySQLColorRepository(session), color_id=color_id), {
    UnableToFindIdError: { "status_code": status.HTTP_404_NOT_FOUND }
})
```


# Usage with custom exceptions and override default exceptions:
```
return error_handler(lambda: service.get_by_id(repository=MySQLColorRepository(session), color_id=color_id), {
    UnableToFindIdError: { "status_code": status.HTTP_404_NOT_FOUND }
}, {
    SQLAlchemyError: { "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR }
})

```
"""
def error_handler(callback: Callable, custom_exceptions: dict = {}, default_exceptions: dict = {}):
    try:
        return callback()
    except Exception as e:
        # Check if the caught exception is in the custom exceptions dictionary
        for exception in custom_exceptions:
            if isinstance(e, exception):
                raise HTTPException(
                    status_code=custom_exceptions[exception]["status_code"],
                    detail=str(e)
                )
                
        # Check if the caught exception is in the default exceptions dictionary
        for exception in default_exceptions:
            if isinstance(e, exception):
                raise HTTPException(
                    status_code=default_exceptions[exception]["status_code"],
                    detail=str(e)
                )
              
        # Log internal server errors for debugging
        logging.error(f"Internal Server Error Caught: {e}")
        
        # Raise a generic internal server error for the client
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(f"Internal Server Error Caught.")
        )
