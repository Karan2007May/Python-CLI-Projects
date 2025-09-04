import requests

API_KEY = "your_api_key_here"
city = "New York"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
weather_data = response.json()

print(f"Temperature in {city}: {weather_data['main']['temp']}°C")
