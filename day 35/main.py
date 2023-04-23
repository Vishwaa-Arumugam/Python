import requests
from twilio.rest import Client

OPEN_WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "c5d771ef6c0bad3aec43dd337c1d8e9e"
acc_sid = "ACb47ff0c6105bb7d04088e849c301cf31"
auth_token = "e0f0b9748fd3726f585b74d963c50b8b"

parameters = {
    "lat": -16.918550,
    "lon": 145.778061,
    "appid": api_key,
    "exclude": "coord,main,wind"
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
if int(weather_data) < 521:
    client = Client(acc_sid, auth_token)

    message = client.messages \
        .create(
        body="it's going to rain today. Remember to bring an ☂️",
        from_='+15076783397',
        to='+919500288874'
    )
    print("its raining")
    print(message.status)
