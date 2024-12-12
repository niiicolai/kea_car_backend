# External Library imports
from fastapi import APIRouter, Depends, Path

# Internal library imports
from app.controllers.error_handler import error_handler
from app.core.security import get_current_sales_person_token
from app.services.weather_service import get_weather_by_country
from app.resources.weather_resource import WeatherReturnResource


router: APIRouter = APIRouter()

@router.get(
    path="/mysql/weather/{country}",
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
def get_weather(
        country: str = Path(
            default=...,
            title="Country",
            description="Country to get weather for")
):  # pragma: no cover
    return error_handler(
        error_message="Failed to get weather from the external API",
        callback=lambda: get_weather_by_country(country)
    )
