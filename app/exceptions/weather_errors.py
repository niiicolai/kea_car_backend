class UnsupportedCountryError(Exception):
    def __init__(self, country: str, countries: list):
        self.message = f'The country "{country}" is incorrect. The following countries are supported: {countries}'
        super().__init__(self.message)

    def __str__(self):
        return f"UnsupportedCountryError: {self.message}"
    
class WeatherAPIError(Exception):
    def __init__(self):
        self.message = f'Something went wrong when contacting the external API'
        super().__init__(self.message)

    def __str__(self):
        return f"WeatherAPIError: {self.message}"
