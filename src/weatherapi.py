import requests
import json
from utils import read_config, kelvin_to_celsius


config_file = 'config.ini'
config = read_config(config_file)


def get_weather(city_name):
    
    # Make sure to replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = config['WeatherApi']['api_key']
    weather_api_url = config['WeatherApi']['weather_api_url']
   
    params = {
                "q": city_name,
                "APPID": api_key
             }
    
    try:
        response = requests.get(weather_api_url, params=params)
        data = json.loads(response.text)

        if response.status_code == 200:
            weather_data = {
                "city_name": city_name,
                "temperature": f"{kelvin_to_celsius(data['main']['temp'])}°C",
                "description": f"{data['weather'][0]['description']}"
            }
            return weather_data
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
