import requests
import os

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
url = "https://api-smartflo.tatateleservices.com/v1/broadcast/end/82321"

headers = {
    "accept": "application/json",
    "Authorization": auth_token
}

response = requests.get(url, headers=headers)

print(response.text)