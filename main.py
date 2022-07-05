import requests

NUTRITIONIX_APP_ID = "928a9c3e"
NUTRITIONIX_APP_KEY = "a0f0b15c97b41a3f83dd37514ca42a6d"

secure_header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=secure_header)
print(response.text)