import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable (secure fallback if not set)
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    print("Error: API_KEY environment variable not set.")
    exit(1)
city = input("Enter city name: ").title()

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # gives Celsius
}
try:
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # converts response to a dictionary
        # Now pull out what you need:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        feel_like = data["main"]["feels_like"]
        name = data['name']
        country = data['sys']['country']
        description = data["weather"][0]["description"]
        print(f'The weather updates of {name},{country} are as follows: \nTemperature: {temp} celsius\nHumidity: {humidity} %\nWind: {wind} m/s')
        print(f"The weather feels like: {feel_like} celsius")
        print(f"Overall weather of {city} is {description}")
    elif response.status_code == 404:
        print("City not found.")
    elif response.status_code == 429:
        print("Rate Limit.")
    elif response.status_code == 401:
        print(f"Invalid API key.")
    else:
        print("Unexpected Error.")
except requests.RequestException as e:
    print(f"Network Error: {e}")


