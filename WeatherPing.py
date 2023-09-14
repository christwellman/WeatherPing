import requests
import os


# Replace "YOUR_API_KEY" with your actual API key
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_by_zip(zip_code, country_code="us"):
    response = requests.get(BASE_URL, params={
        "zip": f"{zip_code},{country_code}",
        "appid": API_KEY
    })
    return response.json()

def get_weather_by_address(address):
    response = requests.get(BASE_URL, params={
        "q": address,
        "appid": API_KEY
    })
    return response.json()

if __name__ == "__main__":
    # Get weather by ZIP code
    # zip_code = input("Enter ZIP code: ")
    zip_code = "27502"
    weather_data = get_weather_by_zip(zip_code)
    print(weather_data)

    # # Get weather by address
    # address = input("Enter address: ")
    # weather_data = get_weather_by_address(address)
    # print(weather_data)