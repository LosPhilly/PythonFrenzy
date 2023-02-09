import requests
import json

API_KEY = '0b828cf0e9b183ca7277b512c65ae62a'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data



def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    temperature = weather_data['main']['temp']
    print(f"The temperature in {city} is {temperature}°F")

if __name__ == '__main__':
    main()
