from app.core.security import get_current_sales_person_token
from app.services.weather_service import get_weather
from app.resources.weather_resource import WeatherReturnResource
from fastapi import APIRouter, Depends, Path, HTTPException, status

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
    return get_weather(country)