from datetime import datetime
import requests

MY_LAT = 19.075983
MY_LNG = 72.877655

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
# print(iss_position)
#
#
# # print(response)
# # OUTPUT    : <Response [200]>

# API PARAMETERS

parameters = {
    'lat': MY_LAT,
    'lng' : MY_LNG,
    'formatted' :0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

now = datetime.now().hour
print(now)
print(sunset)

# print(f"NOTE: Time in hours\nSunrise: {sunrise}\nSunset: {sunset}")

# search https://api.sunrise-sunset.org/json?lat=19.075983&lng=72.877655
#       https://api.sunrise-sunset.org/json?lat=19.075983&lng=72.877655&formatted=0