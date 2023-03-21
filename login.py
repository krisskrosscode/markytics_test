import requests

url = "https://api-smartflo.tatateleservices.com/v1/auth/login"
payload = {
    "email": "TACN2479",
    "password": "SonataFin123@@"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

auth_token = response.json()['access_token']
print(auth_token)
# return auth_token


