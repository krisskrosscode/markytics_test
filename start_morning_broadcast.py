import requests
import os
# from login import auth_token

def get_authorization():
    username = os.environ['PAYMEE_SONATA_TATA_USERNAME']
    password = os.environ['PAYMEE_SONATA_TATA_PASSWORD']
    print(username,password)
    url = "https://api-smartflo.tatateleservices.com/v1/auth/login"

    payload = {
        "email": username,
        "password": password
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['access_token']
    else :
        return None
    
auth_token = get_authorization()

first_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/start/82183"
second_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/start/82184"
third_url = "https://api-smartflo.tatateleservices.com/v1/broadcast/start/82185"

headers = {
    "accept": "application/json",
    "Authorization": auth_token
}

start_first_broadcast_response = requests.get(first_url, headers=headers)
print(start_first_broadcast_response.text)

start_second_broadcast_response = requests.get(second_url, headers=headers)
print(start_second_broadcast_response.text)

start_third_broadcast_response = requests.get(third_url, headers=headers)
print(start_third_broadcast_response.text)