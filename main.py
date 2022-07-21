import requests

NUTRITIONIX_APP_ID = "928a9c3e"
NUTRITIONIX_APP_KEY = "a0f0b15c97b41a3f83dd37514ca42a6d"
GENDER = "male"
WEIGHT = 100.5
HEIGHT = 177.64
AGE = 26

# setting parameters
secure_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

# Setting parameters
nutrition_parameters = {
    "query": input("Tell me which exercise you did?\n"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=nutrition_parameters,
                         headers=secure_header)

data = response.json()
print(response.text)
