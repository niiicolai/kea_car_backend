import pytest
from unittest.mock import patch
from app.services.weather_service import get_weather_by_country
from app.resources.weather_resource import WeatherReturnResource
from app.exceptions.weather_errors import UnsupportedCountryError, WeatherAPIError


@pytest.mark.parametrize("valid_country, mock_response, expected_temp", [
    ('denmark', {'current': {'temp_c': 20.0}}, 20.0),
    ('Denmark', {'current': {'temp_c': 20.0}}, 20.0),
    ('sweden', {'current': {'temp_c': 15.0}}, 15.0)
])
@patch('app.services.weather_service.requests.get')
def test_get_weather_by_valid_country_partitions(mock_get, valid_country, mock_response, expected_temp):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Call the function
    result = get_weather_by_country('denmark')

    # Assert the result
    assert isinstance(result, WeatherReturnResource)
    assert result.temp_c == expected_temp


@pytest.mark.parametrize("invalid_country, expected_error, expected_error_message", [
    ('finland', UnsupportedCountryError, "The country 'finland' is incorrect."),
    ('Norway', UnsupportedCountryError, "The country 'Norway' is incorrect."),
    (True, TypeError, "country must be of type string"),
    (123, TypeError, "country must be of type string")
])
@patch('app.services.weather_service.requests.get')
def test_get_weather_by_invalid_country_partitions(
        mock_get, invalid_country, expected_error, expected_error_message
):
    mock_response = {'current': {'temp_c': 20.0}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    with pytest.raises(expected_error, match=expected_error_message):
        get_weather_by_country(invalid_country)


@patch('app.services.weather_service.requests.get')
def test_get_weather_by_country_api_error(mock_get):
    mock_get.return_value.status_code = 500

    with pytest.raises(WeatherAPIError, match="Something went wrong when contacting the external API"):
        get_weather_by_country('denmark')
