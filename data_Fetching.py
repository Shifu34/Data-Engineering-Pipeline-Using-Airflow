import requests
import pandas as pd

api_key = "01c705b3591b2cfc2fb27de51c0b5ad7"
city = "London"
lat = "30.3753"
lon = "69.3451"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)
weather_data = []
for entry in data['list']:
    weather_data.append({
        "date_time": entry['dt_txt'],
        "temperature": entry['main']['temp'],
        "humidity": entry['main']['humidity'],
        "wind_speed": entry['wind']['speed'],
        "condition": entry['weather'][0]['description']
    })

df = pd.DataFrame(weather_data)
df.to_csv('raw_data.csv', index=False)
