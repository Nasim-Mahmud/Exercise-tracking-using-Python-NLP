import requests
from datetime import datetime

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

# Setting SHEETY parameters and adding data to google sheets

# sheety_parameters = {
#
# }
#
# res1 = requests.post(url="https://api.sheety.co/75f004290b7a8e66b7e5741a6a9e4137/workoutTracking/workouts", json=)