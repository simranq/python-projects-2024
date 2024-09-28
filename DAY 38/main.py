import os
from datetime import datetime
import requests

#nutritionix api
API_KEY = os.environ['NT_API_KEY']                  #1bc12d958eef86ce3cc2a94229a54e90
API_ID =  os.environ['NT_API_ID']                                #"7fb4de97"

GENDER = "Female"
WEIGHT_KG = 63
HEIGHT_CM = 166
AGE = 20


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender":GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json= parameters, headers=headers)
result = response.json()
# print(result)

# sheety api
# no authentication
sheety_endpoint = os.environ['SHEETY_ENDPOINT']
#https://api.sheety.co/1042a9085326e658af96437f800c60a6/workoutTracking/workouts

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise":exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    # basic authentication
    # sheety_response = requests.post(
    #     sheety_endpoint,
    #     json=sheety_inputs,
    #     auth = (
    #         "simranq",
    #         "@Qsim1128"
    #     )
    # )

    # bearer authentication token
    TOKEN = os.environ['SHEETY_TOKEN']
    #"asdfghjklswdhwy-102=0203ufidjclslckoeiskc;"

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheety_response = requests.post(sheety_endpoint, json= sheety_inputs, headers= bearer_headers)
    print(sheety_response.text)

