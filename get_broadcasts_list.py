import requests
from login import auth_token
url = "https://api-smartflo.tatateleservices.com/v2/broadcasts"

headers = {
    "accept": "application/json",
    "Authorization": auth_token
}

response = requests.get(url, headers=headers)

print(response.text)