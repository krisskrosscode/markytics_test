import requests
from login import auth_token
url = "https://api-smartflo.tatateleservices.com/v1/broadcast/lead/64105fa914969d7a6f695573"

headers = {
    "accept": "application/json",
    "Authorization": auth_token,
    "content-type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)