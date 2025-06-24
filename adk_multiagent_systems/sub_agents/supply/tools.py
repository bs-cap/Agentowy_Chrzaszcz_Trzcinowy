import os
import smtplib
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
pswd = os.getenv("PSWD")


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

def send_email(products: str):
    """
    Sends an email to a supply specialist listing products that are in high demand or out of stock.

    Parameters:
    - products (str): A list of product names that are either in high demand or out of stock listed in bullet points and with tab before each insted of first one.

    Returns:
    - None
    """
    email_body = f"""
    Dear Supply Specialist,

    I hope this message finds you well.
    We have identified the following products as either in high demand or currently out of stock. Please review the list below and take the necessary steps to address the supply needs:
    {products}
    Your prompt attention to this matter is greatly appreciated. If you need further details or assistance, feel free to reach out.

    Best regards,  
    Inventory Monitoring System
    """

    email = 'testing.eemail.1337@gmail.com'
    receiver = 'testing.eemail.1337@gmail.com'

    subject = "Supply Monitoring System"
    message = email_body

    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(email, pswd)

    server.sendmail(email, receiver, text)
    print("Email sent successfully!")

    server.quit()


if __name__ == '__main__':
    print(get_weather())
    products = """ 
    - rice
    - bread
    - ice
    """
    send_email(products)