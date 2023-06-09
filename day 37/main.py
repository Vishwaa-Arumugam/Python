import requests
from datetime import datetime

USERNAME = "name"
TOKEN = "token"
GRAPH_Id = "graphid"
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=pixela_endpoint, json=user_parameters)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_parameters = {
    "id": GRAPH_Id,
    "name": "Cycling",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)

post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_Id}"

today = datetime(year=2023, month=4, day=24)

post_graph_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "11"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

post_graph_response = requests.post(url=post_graph_endpoint, json=post_graph_parameters, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_Id}/{today}"

new_pixel_data = {
    "quantity": "4.5"
}

# update_response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(update_response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_Id}/{today}"

delete_response = requests.delete(url=delete_endpoint, headers=headers)
