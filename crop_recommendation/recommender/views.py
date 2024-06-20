import json
from django.http import JsonResponse
import requests
import traceback

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

def recommend_crop(nitrogen, phosphorus, potassium, rainfall, temperature):
    crop_ranges = {
        "Wheat": {"N": (20, 40), "P": (30, 50), "K": (20, 40), "Rainfall": (0, 700), "Temperature": (10, 25)},
        "Rice": {"N": (30, 50), "P": (20, 40), "K": (30, 50), "Rainfall": (0, 2000), "Temperature": (20, 35)},
        "Corn": {"N": (40, 60), "P": (30, 50), "K": (20, 40), "Rainfall": (0, 800), "Temperature": (18, 27)},
        "Barley": {"N": (10, 30), "P": (20, 40), "K": (10, 30), "Rainfall": (0, 600), "Temperature": (7, 24)},
        "Oat": {"N": (15, 30), "P": (20, 40), "K": (15, 30), "Rainfall": (0, 800), "Temperature": (7, 25)},
        "Peanut": {"N": (20, 40), "P": (30, 50), "K": (30, 50), "Rainfall": (0, 1000), "Temperature": (20, 30)},
        "Sugarcane": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (1000, 1500), "Temperature": (20, 35)},
        "Tomato": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (0, 1200), "Temperature": (15, 30)},
        "Potato": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (300, 500), "Temperature": (10, 25)},
        "Carrot": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (0, 800), "Temperature": (10, 25)},
        "Onion": {"N": (20, 40), "P": (30, 50), "K": (20, 40), "Rainfall": (300, 500), "Temperature": (10, 25)},
        "Garlic": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (300, 500), "Temperature": (10, 25)},
        "Peas": {"N": (10, 30), "P": (20, 40), "K": (20, 40), "Rainfall": (0, 800), "Temperature": (10, 25)},
        "Beans": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (500, 800), "Temperature": (15, 30)},
        "Lettuce": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (0, 500), "Temperature": (10, 25)},
        "Spinach": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (300, 500), "Temperature": (10, 25)},
        "Cabbage": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (0, 800), "Temperature": (10, 25)},
        "Broccoli": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (500, 800), "Temperature": (10, 25)},
        "Cauliflower": {"N": (20, 40), "P": (20, 40), "K": (20, 40), "Rainfall": (500, 800), "Temperature": (10, 25)},
        "Cucumber": {"N": (30, 50), "P": (30, 50), "K": (30, 50), "Rainfall": (500, 800), "Temperature": (15, 30)},
        "Pumpkin": {"N": (30, 50), "P": (30, 50), "K": (30, 50), "Rainfall": (500, 800), "Temperature": (15, 30)},
        "Squash": {"N": (30, 50), "P": (30, 50), "K": (30, 50), "Rainfall": (500, 800), "Temperature": (15, 30)},
        "Zucchini": {"N": (30, 50), "P": (30, 50), "K": (30, 50), "Rainfall": (500, 800), "Temperature": (15, 30)},
        "Apple": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (600, 1200), "Temperature": (10, 25)},
        "Banana": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (0, 1500), "Temperature": (20, 35)},
        "Orange": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (600, 1200), "Temperature": (15, 30)},
        "Grape": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (500, 1000), "Temperature": (15, 30)},
        "Mango": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (1000, 1500), "Temperature": (20, 35)},
        "Pineapple": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (1000, 1500), "Temperature": (20, 35)},
        "Papaya": {"N": (50, 100), "P": (40, 80), "K": (50, 100), "Rainfall": (0, 1500), "Temperature": (20, 35)},
        "Soybean": {"N": (20, 40), "P": (20, 40), "K": (30, 50), "Rainfall": (400, 700), "Temperature": (15, 30)},
    }
    
    suitable_crops = []
    
    for crop, ranges in crop_ranges.items():
        if (ranges["N"][0] <= nitrogen <= ranges["N"][1] and
            ranges["P"][0] <= phosphorus <= ranges["P"][1] and
            ranges["K"][0] <= potassium <= ranges["K"][1] and
            ranges["Rainfall"][0] <= rainfall <= ranges["Rainfall"][1] and
            ranges["Temperature"][0] <= temperature <= ranges["Temperature"][1]):
            suitable_crops.append(crop)
    
    if suitable_crops:
        return f"Based on the provided N: {nitrogen}, P: {phosphorus}, K: {potassium}, Rainfall: {rainfall} mm, Temperature: {temperature} °C values, the suitable crops are: {', '.join(suitable_crops)}."
    else:
        return "No suitable crops found for the provided N, P, K, rainfall, and temperature values."

def recommend(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            latitude = float(body['latitude'])
            longitude = float(body['longitude'])
            nitrogen = float(body['nitrogen'])
            phosphorus = float(body['phosphorus'])
            potassium = float(body['potassium'])

            temperature, rainfall = get_weather_data(latitude, longitude)

            if temperature is not None and rainfall is not None:
                recommendation = recommend_crop(nitrogen, phosphorus, potassium, rainfall, temperature)
                return JsonResponse({'temperature': temperature, 'rainfall': rainfall, 'recommendation': recommendation})
            else:
                return JsonResponse({'error': 'Failed to fetch weather data'}, status=500)
        except Exception as e:
            error_message = traceback.format_exc()
            return JsonResponse({'error': f'An error occurred: {str(e)}', 'details': error_message}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
