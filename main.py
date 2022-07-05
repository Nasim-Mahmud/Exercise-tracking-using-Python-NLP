import requests

NUTRITIONIX_APP_ID = "928a9c3e"
NUTRITIONIX_APP_KEY = "a0f0b15c97b41a3f83dd37514ca42a6d"

secure_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

nutrition_parameters = {
    "query": input("What type of exercise?\n"),
    "gender": "male",
    "weight_kg": 100.5,
    "height_cm": 177.64,
    "age": 26
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",json=nutrition_parameters, headers=secure_header)
print(response.text)
