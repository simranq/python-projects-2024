<<<<<<< HEAD
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

=======
import requests
from datetime import datetime,timedelta

ID = "graph1"
TOKEN = "asdf2h3k23h23kh3k2kn"
USERNAME = "simranq"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params )
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":ID,
    "name": "Coding Graph",
    "unit": "days",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers )
# print(response.text)

# CHALLENGE : PUTTING VALUES IN MY GRAPH1

today = datetime.now()
previous_day = datetime.now()-timedelta(1)

# print(today.strftime("%Y%m%d"))

graph1_endpoint = f"{graph_endpoint}/{ID}"

graph1_config = {
    "date":today.strftime("%Y%m%d") ,
    "quantity":"4"
}
graph1_config_yesterday = {
    "date":previous_day.strftime("%Y%m%d") ,
    "quantity":"2"
}
# response = requests.post(url=graph1_endpoint, json=graph1_config_yesterday, headers=headers)
# print(response.text)

#CHALLENGE : UPDATE A PIXEL

pixel_update_endpoint = f"{graph1_endpoint}/{today.strftime("%Y%m%d")}"
update_params = {
    "quantity": "3"
}

# response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{graph1_endpoint}/{previous_day.strftime("%Y%m%d")}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
>>>>>>> 981a57b (day37)
