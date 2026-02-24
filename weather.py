import requests
import json

api_key='20d843c10e67e4e751dc40b5bb5152d4'
city=str(input("Enter your city: "))

url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response=requests.get(url)
data=response.json()

if data["cod"]==200:
    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    weather_description=data["weather"][0]["description"]
    wind_speed=data["wind"]["speed"]
    
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("City not found! Please check the city name and try again")
