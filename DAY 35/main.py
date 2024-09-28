import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

LATITUDE =  19.287140     #18.546391
LONGITUDE = 72.868843    #-72.342789
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" # API REQUEST 3 HR-5 DAY FORECAST
API_KEY = os.environ.get('OWM_API_KEY')

account_sid = "ACd74a126cc857b8e974442bf1c0764d78"
auth_token = os.environ.get('AUTH_TOKEN')

# LOCATION = "Mumbai,India"

weather_parameters = {
    "lat": LATITUDE,
    "lon":LONGITUDE,
    "appid":API_KEY,
    "cnt":4
}

response = requests.get(OMW_ENDPOINT, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data)

will_rain = False

for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}


    client = Client(account_sid, auth_token, http_client = proxy_client)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_="+13144925361",
        to="+917021753382",
    )

    print(message.status)

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# export OWM_API_KEY=d33cdb7010d5170dbf62f69f34f13312;
# export  AUTH_TOKEN=e235bc67c10f95762d16aa35717e7c97;
# python3 main.py