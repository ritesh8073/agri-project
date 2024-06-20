import requests

def get_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data['current_weather']['temperature']
        rainfall = data['current_weather'].get('precipitation', 0)
        return temperature, rainfall
    else:
        return None, None
