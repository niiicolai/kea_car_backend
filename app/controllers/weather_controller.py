from app.core.security import get_current_sales_person_token
from app.services.weather_service import get_weather_by_country
from app.resources.weather_resource import WeatherReturnResource
from fastapi import APIRouter, Depends, Path, HTTPException, status
from app.exceptions.weather_errors import UnsupportedCountryError, WeatherAPIError

router: APIRouter = APIRouter()

@router.get(
    path="/weather/{country}",
    response_model=WeatherReturnResource,
    response_description=
    """
    Successfully retrieved a purchase.
    Returns: WeatherReturnResource.
    """,
    summary="Retrieve a Weather by country - Requires authorization token in header.",
    description=
    """
    Retrieves a Weather by country from an external API
    returns it as a 'WeatherReturnResource'.
    """,
    dependencies=[Depends(get_current_sales_person_token)]
)
def get_weather(country: str = Path(..., title="Country", description="Country to get weather for")):
    try:
        return get_weather_by_country(country)
    except Exception as e:
        if isinstance(e, UnsupportedCountryError):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail=str(e.message)
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='internal server error'
            )