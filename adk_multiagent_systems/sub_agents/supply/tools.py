import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

import smtplib
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import google.auth
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64


load_dotenv()
api_key = os.getenv("API_KEY")

def get_weather(lat: float = 27.6648, lon: float = 81.5158, days: int = 2) -> Dict[str, Any]:
    """
    Tool: Weather API Function

    Description:
    This function retrieves forecast weather data for a specified city using the Google Weather API. 
    It accepts latitude, longitude, and the number of days for the forecast as input, makes a request to the API, and returns structured 
    weather information such as temperature, weather condition, and humidity.

    Parameters:
    - lat (float): The latitude of the location for which to retrieve weather data.
    - lon (float): The longitude of the location for which to retrieve weather data.
    - days (str): The name of the city for which to retrieve weather data.

    Returns:
    - Dict[str, Any]: A dictionary containing the current weather data, including temperature, 
      weather condition, and humidity.
    """
    minTemp = []
    maxTemp = []
    base_url = "https://weather.googleapis.com/v1/forecast/days:lookup"
    params = {
        'key': api_key,
        'location.latitude': lat,
        'location.longitude': lon,
        'days': days
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    for days in data['forecastDays']:
        maxTemp.append(days['maxTemperature']['degrees'])

    
    if response.status_code == 200:
        weather_info = {
            'maxTemperature': maxTemp
        }
        return weather_info
    else:
        return {'error': data.get('message', 'Failed to retrieve weather data')}


if __name__ == '__main__':
    print(get_weather())