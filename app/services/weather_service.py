import os
import requests
from app.resources.weather_resource import WeatherReturnResource
from app.exceptions.weather_errors import UnsupportedCountryError, WeatherAPIError

# Base URL for the Weather API
baseUrl = "https://api.weatherapi.com/v1/"

# Get the API key from the environment variables
key = os.getenv("WEATHER_API_KEY")

# List of supported countries
# Find the supported countries here: https://www.weatherapi.com/docs/conditions.json
supported_countries = ["denmark", "sweden"]

def get_weather_by_country(country: str) -> WeatherReturnResource:
    if isinstance(country, str) == False:
        raise TypeError(f'country must be of type string, but was {type(country)}')
    if country.lower() not in supported_countries:
        raise UnsupportedCountryError(country, supported_countries)
    
    # Combine the base url with the endpoint and the key
    # Example= https://api.weatherapi.com/v1/current.json?q=Denmark&key=somekey    
    url = baseUrl + "current.json?q=" + country + "&key=" + key
    print(url)
    # Make an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the response status code is 200 (OK)
    if response.status_code != 200:
        raise WeatherAPIError(api_url=url)
    
    # Parse the JSON response
    data = response.json()
    
    # Return the DTO object with the temperature
    return WeatherReturnResource(
        temp_c = data['current']['temp_c'],
    )