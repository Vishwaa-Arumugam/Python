import requests
from datetime import datetime
import os

GENDER = "MALE"
WEIGHT_KG = 55
HEIGHT_CM = 170
AGE = 20

APP_ID = os.environ["NT_APP_ID"]  # "1b85cd44"
APP_KEY = os.environ["NT_API_KEY"]  # "5526f06ac5cbc31116b9127c08be17df"

exercise_endpoint = "   "
sheety_endpoint = os.environ[
    "SHEET_ENDPOINT"]  # "https://api.sheety.co/f28f92cebbb256171fecf66ded592250/workoutTracking/workouts"

basic_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"  # "Basic dmlzaHdhYTphaHRpbmExMjM0"
}

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    row_parameters = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint,
                                   json=row_parameters,
                                   auth=(
                                       "vishwaa",
                                       f"{os.environ['PASSWORD']}"
                                   )
                                   )

    print(sheet_response.text)

# a =
# print(a)
